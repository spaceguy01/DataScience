
# coding: utf-8

# ***Using Selenium to scrape World Cup 2018 Games played, scores and schedule from ESPN World Cup information***

# In[ ]:


# Import Selenium webdriver, and the modules needed to display flags of teams

from selenium import webdriver
from IPython.display import Image
from IPython.core.display import display


# Setting up Selenium Webdriver to get all the dates of World Cup 2018

driver = webdriver.Chrome()
base_url = 'http://www.espn.com/soccer/scoreboard/_/league/FIFA.WORLD/date/201806'
dates = range(14,29)

# Looping through all the dates

for each in dates:
    url = base_url+str(each)
    driver.get(url)
    date = driver.find_element_by_id('sbpDate')


# Getting all the scoreboxes of each game

    scorebox = driver.find_elements_by_class_name('competitors')
    for each in range(0,int(len(scorebox)),2):

# Getting all the flags of each country

        images = scorebox[each].find_elements_by_tag_name('img')
        urls1 = images[0].get_attribute('src')
        urls2= images[1].get_attribute('src')
        flag1 = Image(url=urls1)
        flag2 = Image(url=urls2)

# Getting the fullname and abbreviations of each team

        teamfullname = scorebox[each].find_elements_by_xpath(".//span[@class='short-name']")
        team1fullname = teamfullname[0].get_attribute('textContent')
        team2fullname = teamfullname[1].get_attribute('textContent')

        team = scorebox[each].text.split()
        team1name = team[0]
        team1score = team[1]
    
# Separate Finished Games vs Unplayed and Currently Playing games
    
        if "'" in team[3]:
            team2name = team[5]
            team2score = team[4]
            gamestatus = team[3]
        else:
            team2name = team[4]
            team2score = team[3]
            gamestatus = team[2]
        
        
# Listing each team names and showing flags

        print('\n')
        print('\033[1m',date.text,'\033[0m')
        print('\n')
        print('Team 1 is: ',team1name,' : ',team1fullname)
        display(flag1)
        print('*'*40)
        print('\n')
        print('Team 2 is: ',team2name,' : ',team2fullname)
        display(flag2)
        print('*'*40)        
        print('\n')

    
# If game is Finished (FT), then list score and who won
        
        if gamestatus == 'FT':
            gamestatus+=' = Finished Game'
            print(team1fullname,' ',team1score,' : ',team2score,' ',team2fullname)
            print('\n')
            print('Status of game is :',gamestatus)
            print('\n')
            if team1score > team2score:
                print ('\033[1m',team1fullname,' has WON the game!','\033[0m')
            elif team1score < team2score:
                print ('\033[1m',team2fullname,' has WON the game!','\033[0m')
            else:
                print('\033[1m',"It's a TIE GAME!",'\033[1m')
            print('\n')
            print('-'*80)

        
# If gamestatus is not FT (Finished) then it's either playing right now or scheduled to play
    
    
            
        
    # Game currently playing
        elif len(team)==6:
            network = scorebox[each].find_element_by_xpath('//span[@href="#"]').text
            time = scorebox[each].find_element_by_class_name('time').text
            print("Game is current playing and at : ",time,' Minutes into the match')
            print('\n')
            print(team1fullname,' ',team1score,' : ',team2score,' ',team2fullname)
            print('\n')
            if team1score > team2score:
                print ('\033[1m',team1fullname,' is currently winning!','\033[0m')
            elif team1score < team2score:
                print ('\033[1m',team2fullname,' is currently winning!','\033[0m')
            else:
                print('\033[1m',"It's a TIE GAME right now!",'\033[0m')
            print('\n')
            print('-'*80)

    # Game scheduled to play
        else:            
            network = scorebox[each].find_element_by_xpath('//span[@href="#"]').text
            time = scorebox[each].find_element_by_class_name('time').text
            print('\033[1m',team1fullname,'\033[0m',' and ','\033[1m',team2fullname,'\033[0m',' is schedule to play on network ','\033[1m',network,' at ',time,'\033[0m')
            print('\n')
            print("Don't miss the game!")
            print('\n')
            print('-'*80)


# In[ ]:




