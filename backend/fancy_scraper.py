#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re
import urllib
from time import sleep
import tika
tika.initVM()
from tika import parser
from itranslate import itranslate as itrans
from googlesearch import search

# Scraper for liberal.ca
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
            p = p.get_text()
            
            if query in p.lower(): # try search query in paragraph
                result.append(p)
            elif keys is not None:
                for k in keys: # try each key in the paragraph
                    if k in p.lower():
                        result.append(p)
                        break
    
    return result

# Scraper for conservative.ca
# Input: Search query string (ie: 'COVID-19')
# Return: Array of strings, each string is an entire paragraph that contains relevant keyword
def get_conservative_info(query):
    start = time.time()
    query = query.lower()
    url = 'https://www.conservative.ca/plan/'
    sub_pages = ['jobs','accountability','mental-health','secure-the-country','economy','secure-the-environment']
    
    keys = get_synonyms(query)
    result = []
    
    for sp in sub_pages: # first check via page titles
        if sp in query or (keys is not None and sp in keys):
            check_page_conservative(url+sp+'/', query, keys, result)
        if len(result) > 0:
            return result
    
    for sp in sub_pages: # loop through sub-pages
        check_page_conservative(url+sp+'/', query, keys, result)
        if len(result) > 2: # once we have enough results no need to continue
            break
        if time.time() - start > 10:
            break
        
    return result

def check_page_conservative(url, query, keys, result):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    b = soup.select('body > main')[0].find_all('p')

    for p in b: # loop through paragraphs
        p = p.get_text()
        if query in p.lower(): # try search query in paragraph
            result.append(p)
        elif keys is not None:
            for k in keys: # try each key in the paragraph
                if k in p.lower():
                    result.append(p)
                    break
        if len(result) > 2: # once we have enough results no need to continue
            break

# Scraper for ndp.ca
# Input: Search query string (ie: 'COVID-19')
# Return: Array of strings, each string is an entire paragraph that contains relevant keyword
def get_ndp_info(query):
    start = time.time()
    query = query.lower()
    url = 'https://www.ndp.ca/'
    sub_pages = ['commitments','affordability','economy','climate-action','better-care','reconciliation','communities','courage']
    
    keys = get_synonyms(query)
    result = []
    
    for sp in sub_pages: # first check via page titles
        if sp in query or (keys is not None and sp in keys):
            check_page_ndp(url+sp, query, keys, result)
        if len(result) > 0:
            return result
    
    for sp in sub_pages: # loop through sub-pages
        check_page_ndp(url+sp, query, keys, result)
        if len(result) > 2: # once we have enough results no need to continue
            break
        if time.time() - start > 10:
            break
        
    return result

def check_page_ndp(url, query, keys, result):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    b = soup.select('.page--content-cached')[0].find_all('p')

    for p in b: # loop through paragraphs
        p = p.get_text()
        if '<p>' not in p:
            if query in p.lower(): # try search query in paragraph
                result.append(p)
            elif keys is not None:
                for k in keys: # try each key in the paragraph
                    if k in p.lower():
                        result.append(p)
                        break
        if len(result) > 2: # once we have enough results no need to continue
            break

# Scraper for peoplespartyofcanada.ca
# Input: Search query string (ie: 'COVID-19')
# Return: Array of strings, each string is an entire paragraph that contains relevant keyword
def get_peoplesparty_info(query):
    start = time.time()
    query = query.lower()
    url = 'https://www.peoplespartyofcanada.ca/'
    sub_pages = ['pipelines','indigenous-issues','internal-trade','housing','firearms','equalization','covid-health-measures','health-care','public-finance','global-warming-environment','freedom-of-expression','economy','veterans','canadian-identity','refugees','immigration','foreign-policy','supply-management']
    
    keys = get_synonyms(query)
    result = []
    
    for sp in sub_pages: # first check via page titles
        if sp in query or (keys is not None and sp in keys):
            check_page_peoplesparty(url+sp, query, keys, result)
        if len(result) > 0:
            return result
    
    for sp in sub_pages: # loop through sub-pages
        check_page_peoplesparty(url+sp, query, keys, result)
        if len(result) > 2: # once we have enough results no need to continue
            break
        if time.time() - start > 10:
            break
    return result

def check_page_peoplesparty(url, query, keys, result):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    b = soup.select('#intro > div > div > div.col-md-8.platform')[0].find_all('p')

    for p in b: # loop through paragraphs
        p = p.get_text()
        if query in p.lower(): # try search query in paragraph
            result.append(p)
        elif keys is not None:
            for k in keys: # try each key in the paragraph
                if k in p.lower():
                    result.append(p)
                    break
        if len(result) > 2: # once we have enough results no need to continue
            break

# Scraper for greenparty.ca
# Input: Search query string (ie: 'COVID-19')
# Return: Array of strings, each string is an entire paragraph that contains relevant keyword
def get_greenparty_info(query):
    start = time.time()
    query = query.lower()
    url = 'https://www.greenparty.ca/en/platform/'
    sub_pages = ['message-from-leader','green-future','life-with-dignity','just-society']
    
    keys = get_synonyms(query)
    result = []
    
    for sp in sub_pages: # first check via page titles
        if sp in query or (keys is not None and sp in keys):
            check_page_greenparty(url+sp, query, keys, result)
        if len(result) > 0:
            return result
    
    for sp in sub_pages: # loop through sub-pages
        check_page_greenparty(url+sp, query, keys, result)
        if len(result) > 2: # once we have enough results no need to continue
            break
        if time.time() - start > 10:
            break
    return result

def check_page_greenparty(url, query, keys, result):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    b = soup.select('#document-content > div.region.region-content').find_all('p')

    for p in b: # loop through paragraphs
        p = p.get_text()
        if query in p.lower(): # try search query in paragraph
            result.append(p)
        elif keys is not None:
            for k in keys: # try each key in the paragraph
                if k in p.lower():
                    result.append(p)
                    break
        if len(result) > 3: # once we have enough results no need to continue
            break

# Scraper for blocquebecois.org
# Input: Search query string (ie: 'pandemic')
# Return: Array of strings, each string is an entire paragraph that contains relevant keyword
def get_bloc_quebecois_info(query):
    raw = parser.from_file('blocqc-Plateforme-2021-planche.pdf')['content'].strip() # Read from PDF file
    raw = raw[raw.index('Une campagne électorale') : raw.index('dans les plus brefs délais.')+28]

    keys = get_synonyms(query)
    result = []
    
    splitted = []
    
    for i in range(0, 13):
        splitted.append(raw[5000*i : min(len(raw), 5000*(i+1))])
    
    #print(splitted[0])
    translated = ''
    
    for s in splitted:
        t = itrans(s, to_lang="en")
        #print('.')
        translated += t
    
    #print(translated)
    
    splat = translated.split("\n\n") # split into paragraphs
    
    for p in splat:
        #p = itrans(p, to_lang="en")
        #print(p)
        if query in p.lower(): # try search query in paragraph
            result.append(p)
        elif keys is not None:
            for k in keys: # try each key in the paragraph
                if k in p.lower():
                    result.append(p)
                    break
        if len(result) > 3: # once we have enough results no need to continue
            break
    return result

# Input: query and party as strings
# Return: Array of arrays, each array looks like this [url, title, image_url]
def get_related_articles(query, party):
    result = []
    urls = list(search(party + ' ' + query, tld="co.in", num=3, stop=3, pause=2))

    for u in urls:
        page = requests.get(u)
        soup = BeautifulSoup(page.text, 'html.parser')
        title = soup.find_all('title')[0].decode_contents().strip()
        image = u[:u.index('/', 10)] + soup.find_all('img')[0].get('src')
        result.append([u, title, image])
    return result

# Input: String with one or multiple keywords
# Return: Array of strings, each string a single keyword relevant to input
def get_synonyms(s):
    
    # wordbank for keywords
    words = {}
    words[0] = ['covid','pandemic','corona','virus','vaccine']
    words[1] = ['housing','home','house','family']
    words[2] = ['economy','jobs','work','busines','finance','financial','tax']
    words[3] = ['equal','diversity','diverse','equity']
    words[4] = ['climate','pollution','nature','environment','climate-action','climate-change','secure-the-environment','emission','carbon','polluter','green-future','pipeline']
    words[5] = ['indigenous','reconciliation','colonialism']
    words[6] = ['justice','police','policing','policy','safe','safety']
    words[7] = ['fairness','growth','fiscal']
    words[8] = ['accountability','transparency','conflict of interest']
    words[9] = ['mental health','suicide','euthanasia']
    words[10] = ['liberal','trudeau','martin','chrétien','chretien']
    words[11] = ['conservative','harper','o\'tool',]
    words[12] = ['ndp','democrat','singh','mulcair','layton']
    words[13] = ['pig','cow','chicken','sheep','goat','livestock','meat','steak','pork','animal']
    words[14] = ['medicine','medication','health care','doctor','hospital']
    words[15] = ['education','school','teacher','teaching','tuition','college','university','student']
    words[16] = ['abortion','pregnancy','pregnant','fetus','embryo','birth']
    words[17] = ['lgbt','gay','marriage','gender','transgender']
    words[18] = ['death penalty','capital punishment','death sentence']
    
    # if a keyword appears in the querry, return that keyword group
    for row in words:
        for i in words[row]:
            if i in s:
                return words[row]

# Input: Some kind of party identifier (ie: 'Trudeau', 'NDP')
# Return: Name of party (ie: Input='Trudeau' --> Return='liberal')
def get_party(s):
    s.lower()
    words = {}
    words[0] = ['liberal','trudeau','justin','libéral']
    words[1] = ['conservative','o\'tool','erin']
    words[2] = ['new democratic party','singh','jagmeet','ndp','democratic','démocratique','democratique']
    words[3] = ['bloc québécois','québéc','quebec','blanchet','yves','françois']
    words[4] = ['green','paul','annamie','vert']
    
    for i in words:
        for w in words[i]:
            if w in s:
                return words[i][0] # first element is the name we'll be using