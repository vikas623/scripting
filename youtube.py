from selenium import webdriver
from os import system, name
import time
from getpass import getpass
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def search():
	clear()
	username = input("Enter username: ")

	browser = webdriver.Chrome()
	
	login_url = "http://youtube.com"
	browser.get(login_url)
	search_box = browser.find_element_by_id('search')
	search_box.send_keys(username)
	search_bttn = browser.find_element_by_id('search-icon-legacy')
	search_bttn.click()
	time.sleep(10)

search()