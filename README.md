# PoliViews
Test it out: https://poliviews.web.app/

Video Presentation: https://www.youtube.com/watch?v=UQHYVmcF8TY

## Inspiration

With the upcoming 2021 Federal Elections, our team felt no motivation to participate in voting as we were unable to find much unbiased data comparing the ideas and views of each party. We were constantly bombarded with the Liberals and Conservatives headlines, but we wanted to learn more. Therefore, we created an application which would summarize boring political documents and compare the different parties for us. PoliViews solved our problem in being uninterested in the upcoming election as it provided us with credible insights into the opinions of different parties, and essentially provided us with everything needed to make a solid decision on who should lead the country.

## What it does

PoliViews is your one-stop-shop to learn all about the views of each Canadian political party. Simply enter any political topic you are curious to learn more about (for example: vaccine passports). The articles we scrape from Google are summarized into just 2-3 sentences using NLP which outline the views of each major Canadian political party. Want to learn even more? Feel free to click "see similar articles" to find related articles as well their sentiment analysis.  We chose to include a sentiment analysis based on an article we recently came across: [link](https://www.nature.com/articles/s41599-019-0224-y.pdf) which outlines that misinformation is significantly more likely to make readers feel negative emotions.

## Samples

### Search any topic!
![poliviews](https://user-images.githubusercontent.com/69891859/133920386-f98fbaf1-8362-471a-bbf9-1da004fa7222.png)

### Get views from all main leaders!
![poliview more pic](https://user-images.githubusercontent.com/69891859/133920431-e3585473-a79e-4ad0-a202-168aa49952a9.png)


### Find related articles to learn more about specific topics!
![Screenshot 2021-09-19 041734](https://user-images.githubusercontent.com/69891859/133920519-0b004837-1806-4883-add4-7e84d28ec127.png)

## How we built it

**Frontend**: React, Chakra UI, Axios 
**API**: Flask, Python 
**Web-Scrapers**: BeautifulSoup, Google Search
**NLP**: Microsoft Azure – Abstractive Summarization and Sentiment Analysis
**Deployment**: Firebase, Heroku

## Challenges we ran into

As hackers relatively new to full-stack development, we ran into server issues pretty often, and spent a significant time debugging the dreaded '500 Internal Server Error' bugs. The deployment of our frontend website + API also took a while due to Firebase and Heroku's finicky configurations. 

## Accomplishments that we're proud of

Our group is extremely proud to complete a working product that is visual appealing to the end user in the span of only 36 hours. We were able to incorporate NLP ideologies with the traditional backend and frontend development in a creative manner that is useful to the average citizen. We were also proud of our teamwork, as we were able to brainstorm new and innovative ideas which would be implemented at a moment's notice. 

## What we learned

Using bleeding-edge technology such as Microsoft Azure and BeautifulSoup. We leveraged some really cool technologies that help make our day-to-day lives easier, and it's a great tool to have under our belt. 

## What's next for PoliViews

PoliViews is always looking to expand and make voting easier for the average person. As a result, we would like to bring PoliViews to mobile devices by allowing users to text a number, which would give them views for any Political Party on any topic on the go! Another idea is to provide location based information for ridings so that people can learn more on the MPs that will truly represent them!

In terms of improvements to current features, we hope to make our NLP summarization and sentiment analysis more accurate by acquiring more data to train our own models this time. We also hope to improve load times from webscraping by caching common results so that it is faster for users to access. Furthermore, we hope to make our website more dynamic so it is even more accessible than it is currently!
