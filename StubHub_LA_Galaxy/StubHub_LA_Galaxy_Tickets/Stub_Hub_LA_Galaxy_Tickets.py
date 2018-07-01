
# coding: utf-8

# In[1]:


from selenium import webdriver
import time


# In[2]:


"""Setting up Chrome Webdriver for LA Galaxy game list url"""

url ='https://www.stubhub.com/la-galaxy-tickets/performer/12587/'
driver = webdriver.Chrome()
driver.get(url)


# In[3]:


"""Checks to see if there is 'See more events' tab on bottom and if there is, click. If not, move on"""

try:
    more = driver.find_element_by_class_name('EventListPanel__Footer')
    if more:
        more.click()
        time.sleep(2)
except:
    pass


"""Getting all the Game links and Parking Pass links listed"""

content = driver.find_elements_by_class_name('EventItem__Body')
sites = []
for each in content:
    links = each.find_elements_by_class_name('EventItem__TitleLink')
    for link in links:
        sites.append(link.get_attribute('href'))


# In[ ]:


"""Looping through each link in the sites list by clicking on each link and switching to the new window for game tickets"""

for each in range(0,len(sites)):
    main_window = driver.current_window_handle
    driver.execute_script('window.open("{}","_blank");'.format(sites[each]))
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[-1])
    time.sleep(2)
    
    
    """Scraping the game ticket window for ticket information"""
    
    new_content = driver.execute_script("return document.getElementsByTagName('html')[0]")
    time.sleep(2)
    event = new_content.find_element_by_class_name('header').get_attribute("innerText")

    info = new_content.find_elements_by_class_name('ticket-container')
    date = new_content.find_element_by_class_name('date-stamp-standard').get_attribute("innerText").split()
    dateinfo = ' '.join(date)
    print('\033[4m',event,' for ',dateinfo,'\033[0m')
    if not info:
        print('There are NO tickets for this')
    else:
        for each in info:
            sectioncell = each.find_element_by_class_name('sectioncell').get_attribute("innerText")

            rowcell = each.find_element_by_class_name('rowcell').get_attribute("innerText")

            pricecell = each.find_element_by_class_name('dollar-value').get_attribute("innerText")

            reach = each.find_element_by_class_name('priceEachText').get_attribute("innerText")

            tickets = each.find_element_by_class_name('ticketsText').get_attribute("innerText")

            delivery = each.find_element_by_class_name('delivery').get_attribute("innerText")

            print(sectioncell, rowcell, pricecell, reach, tickets, delivery)
    print('--'*40)
    print('\n')

    driver.close()
    driver.switch_to_window(main_window)
    

