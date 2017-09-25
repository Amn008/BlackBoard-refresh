# BlackBoard-refresh
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

//place where chrome webdriver is placed
driver=webdriver.Chrome('Z:\python\chromedriver.exe')

//link of the particular bb page or subject
driver.get('https://learn.upes.ac.in/webapps/blackboard/execute/modulepage/view?course_id=_12703_1&cmp_tab_id=_28037_1&mode=view')

//no of times you want the loop
for x in range(0, 10):
	time.sleep(40)
	driver.refresh()
