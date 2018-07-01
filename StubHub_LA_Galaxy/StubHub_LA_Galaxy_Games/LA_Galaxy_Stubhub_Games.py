
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[7]:


"""Setting up Chrome webdriver to use LA Galaxy game list url"""

url ='https://www.stubhub.com/la-galaxy-tickets/performer/12587/'
driver = webdriver.Chrome()
driver.get(url)


# In[ ]:


"""If there is 'See More Events tab on bottom to show more games, click. Otherwise, continue"""
try:
    more = driver.find_element_by_class_name('EventListPanel__Footer')
    if more:
        more.click()
except:
    pass

"""Collecting all the ticket page links for each game"""
sites = []


"""Scraping each game information and printing them out to screen"""

content = driver.find_elements_by_class_name('EventItem__Body')

for info in content:
        
    details = info.find_element_by_class_name('EventItem__Details')
    day = info.find_element_by_class_name('DateStamp__Day').text
    date = info.find_element_by_class_name('DateStamp__MonthDate').text
    print('Day : ',day,' on Date : ',date)
    gameinfo = details.find_element_by_tag_name('a')
    print(gameinfo.text)
    state = details.find_element_by_class_name('EventItem__MixInfo').text.split()
    
    """If time is TBD (To be determined), which is basically all the Parking Pass tabs"""
    if state[0] == 'TBD':
        time = ' '.join(state[0:1])
        city = ' '.join(state[6:])
#         stadium =' '.join(state[3:6]).replace(',','')
        venue = details.find_element_by_class_name('EventItem__VenueInfo').text
        print('Time: ',time,' -',venue)
#         print('Time: ',time,' at',stadium,',',city)
    else:
        time = ' '.join(state[0:2])
        venue = details.find_element_by_class_name('EventItem__VenueInfo').text
#         city = ' '.join(state[5:])
#         stadium = ' '.join(state[3:5]).replace(',','')
        print('Time: ',time,' at',venue)
    
    """Show how much the ticket prices start from, and how many tickets are left if available"""
    try:
        tickets = details.find_element_by_class_name("EventItem__Price").text
        print('There are tickets available from: ',tickets)
    except:
        pass
    try:
        ticksleft = info.find_element_by_class_name("EventItem__Urgency").text
        if ticksleft:
            print('There are ',ticksleft)
    except:
        pass
    
    """Grab the links for each games that will take you to ticket purchase for each game. **Optional**"""
    link = details.find_element_by_class_name('EventItem__TitleLink')
    link_url = link.get_attribute('href')
    print(link.get_attribute('href'))
    sites.append(link_url)
    print('\n')
    

    
"""Print out ticket links for each game **Optional**"""
for each in sites:
    print(each)
    print('\n')
    

