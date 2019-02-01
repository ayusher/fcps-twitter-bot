#Written by Ayush Rautwar

import urllib.request as ur
import datetime
from datetime import date

out = ""
s = ur.urlopen("https://twitter.com/RyanLMcElveen")
sl = str(s.read())
a = date.today()
b = a + datetime.timedelta(days=1)

if ("will be closed tomorrow, "+a.strftime('%A')+", "+a.strftime('%B')+" "+str(a.day)+".") in sl:
    out = out +("No school today!")
elif("will now be closed today, "+a.strftime('%A')+", "+a.strftime('%B')+" "+str(a.day)+".") in sl:
    out = out +("Update: No school today!")
elif ("will open two hours late tomorrow, "+a.strftime('%A')+", "+a.strftime('%B')+" "+str(a.day)+".") in sl:
    out = out +("Two hour delay today!")
else:
    out = out+("Nothing on today yet!")

if ("will be closed tomorrow, "+b.strftime('%A')+", "+b.strftime('%B')+" "+str(b.day)+".") in sl:
    out = out+ "\n"+("No school tomorrow!")
elif ("will open two hours late tomorrow, "+b.strftime('%A')+", "+b.strftime('%B')+" "+str(b.day)+".") in sl:
    out = out+ "\n"+("Two hour delay tomorrow!")
else:
    out = out+ "\n"+("Nothing on tomorrow yet!")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https://bigassmessage.com/")
#driver.maximize_window()
#msg = driver.find_element_by_id('msgInput')
#msg.send_keys(out)
#go = driver.find_element_by_id('PREVIEW')
#go.click()

driver.get("https://messenger.com/")
driver.maximize_window()
username = driver.find_element_by_id('email')
username.send_keys("EMAIL")
pwd = driver.find_element_by_id('pass')
pwd.send_keys("PASSWORD")
go = driver.find_element_by_id('loginbutton')
go.click()
#hello = driver.find_element_by_id("row_header_id_thread:1582359595202485")
#hello.click()
textbox = driver.find_element_by_xpath("//*[@data-editor]")
textbox.click()
actions = ActionChains(driver)
actions.send_keys(out+ '\n')
actions.perform()
