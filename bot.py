import time;
from selenium import webdriver;



#Download chrome webdriver
#Download Selenium with pip iinstall selenium




#Time to refresh page
Timer = 3    #(3 Seconds)


#Youtube link
link = 'Insert link'
#Number of views

views = 10
driver = webdriver.Chrome('C:\Python27\chromedriver')
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
