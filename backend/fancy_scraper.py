#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re
import urllib
from time import sleep

# Input: Search query string (ie: 'climate change')
# Return: Array of strings, each string is an entire paragraph that contains relevant keyword
def get_liberal_info(query):
    query = query.lower()
    url = 'https://liberal.ca/our-platform/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    keys = get_synonyms(query)
    result = []
    
    for i in range(1,8): # loop through accordion elements
        b = soup.select('.accordion > li:nth-child('+str(i)+') > div > div > div > div > div')[0].find_all('p')
        
        for p in b: # loop through paragraphs
            p = p.decode_contents().strip()
            
            if query in p.lower(): # try search query in paragraph
                result.append(p)
            elif keys is not None:
                for k in keys: # try each key in the paragraph
                    if k in p.lower():
                        result.append(p)
                        break
    
    return result

# Input: String with one or multiple keywords
# Return: Array of strings, each string a single keyword relevant to input
def get_synonyms(s):
    
    # wordbank for keywords
    words = {}
    words[0] = ['covid','pandemic','corona','virus','vaccine']
    words[1] = ['housing','home','house','family']
    words[2] = ['economy','jobs','work','busines','finance','financial']
    words[3] = ['equal','diversity','diverse','equity','lgbtq']
    words[4] = ['climate','pollution','nature','environment']
    words[5] = ['indigenous','reconciliation','colonialism']
    words[6] = ['justice','police','policing','policy','safe','safety']
    words[7] = ['fairness','growth','fiscal']
    
    # if a keyword appears in the querry, return that keyword group
    for row in words:
        for i in words[row]:
            if i in s:
                return words[row]