from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import system, name
import time
from getpass import getpass
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def login():
	clear()
	usr = input('enter user name')
	pd = getpass('enter pass')

	browser = webdriver.Chrome()
	login_url = "http://facebook.com"
	browser.get(login_url) 

	user_box = browser.find_element_by_id('email') 
	user_box.send_keys(usr)
	pas_box = browser.find_element_by_id('pass')
	pas_box.send_keys(pd)
	pas_box.send_keys(Keys.ENTER)
	time.sleep(600)

login()