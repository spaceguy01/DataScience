## Stub Hub Los Angeles Galaxy Tickets Scrape

### Using Selenium Webdriver, scraped Stub Hub website to get list of tickets available for Los Angeles Galaxy of Major League Soccer

Website URL : https://www.stubhub.com/la-galaxy-tickets/performer/12587/

#### When scraping, the webpage detects and puts up a human verification check similar to CAPTCHA test

<img src='images/Human_Check.png'>

#### Once human verification check is completed, the Stub Hub website showing games are displayed

#### Sample view of Stub Hub page

<img src='images/Sample_Games_Site.png'>

#### When the scraper is run, it will click on each game links, then scrape the tickets page to get the list of tickets available

<img src='images/Sample_Tickets_Site.png'>

#### Scraper will go through each ticket site, and get the information of tickets available, seating, how many left, cost, etc.


<img src='images/Sample_Tickets_Output.png'>


#### This mini project was done just for Los Angeles Galaxy games, but similar coding style can be used for other team games in the website
