
import time
import datetime
import codecs
import os
import webbrowser
import pandas as pd
import re
import fileinput
from pathlib2 import Path
from random import randrange
from threading import Thread
from random import randint
from time import strptime
from bs4 import BeautifulSoup
import requests 
import datetime as dt
import glob, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import Counter
import os.path
from pathlib import Path
import cv2
import random
import string


def crypte():
	crypte = str(random.randint(1, 9))
	for i in range(4):
		crypte += str(random.randint(1, 9))
		crypte += random.choice(string.ascii_letters)
	return crypte

datavideoimage = open("C:/Users/ebent/OneDrive/Documents/ScreenShot/imageproductdata.txt", "r")

a = datavideoimage.read()
a = a.replace('\n', '')
a = a.replace('!', '')
TableProductLink = a.split('@')
TableProductLink = [x for x in TableProductLink if x]
productValue = 0
ProdRange = str(range(len(TableProductLink)))
ProdMax = ProdRange.split(',')
ProdMax = ProdMax[1]
ProdMax = ProdMax.replace(')','')
id = datavideoimage.read()
id = a.replace('\n', '')
id = a.replace('!', '')
TableProductLink_url = id.split(')')
TableProductLink_url = [x for x in TableProductLink if x]
TableProductLink_url = [i for i in TableProductLink_url if len(i) >= 10]
i = 0
now = datetime.datetime.now()
Date_actuel = now.strftime("%Y-%m-%d")
a = 0
# printing the list using loop
for x in range(len(TableProductLink)):
	max = len(TableProductLink)
	print(str(x) + '/' + str(max))
	try:
		a+=1
		Id1 = TableProductLink[x]
		beforeExamplesShare, midleNameShare, afterNameShare = TableProductLink[x].partition('h')
		id = beforeExamplesShare
		beforeExamplesShare, midleNameShare, afterNameShare = TableProductLink[x].partition(id)
		url = afterNameShare
		#write history for any problem debug
		# history = open(r"C:/Users/ebent/OneDrive/Documents/ScreenShot/dropfinder_app/DROPFINDER/library/history/history_screen.txt", "r+")
		# history.write(str(afterNameShare))
		# history.close()
		if not "h" in url:
			print('Erreur url' + str(url))
		else:
			try:
				print(id)
				print(url)
				vallUrlLong = str(crypte()) + '-' + str(crypte())  + str(crypte()) + '-' + str(crypte()) 
				# df = pd.DataFrame([vallUrlLong])#date-id-ramdom4number-screen
				# df.to_clipboard(index=False, header=False)
				ScreenLink = "https://dropfinder.fr/content/1/SCREEN/" + vallUrlLong + '.jpg'
				options = webdriver.ChromeOptions()
				options.headless = True
				driver = webdriver.Chrome(options=options)
				#driver = webdriver.Chrome('C:/Users/Arthur/Desktop/DROPFINDER/chromedriver.exe') 
				driver.get(url)
				S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
				driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
				driver.find_element_by_tag_name('body').screenshot('C:/Users/ebent/OneDrive/Documents/ScreenShot/screen/' + vallUrlLong + ".jpg")
				driver.quit()
				print('Screenshot numéro : ' + str(a) + ' télecharger ! ')
				print("----------------------------------------------")
				# request = 'UPDATE advertiser SET screen_link = "' + ScreenLink + '" WHERE id = ' + id +  ';'
				# requestscreen = open(r"C:/Users/ebent/OneDrive/Documents/ScreenShot/dropfinder_app/DROPFINDER/library/Z_request_screen.txt", "a")
				# requestscreen.write(request)
				# requestscreen.close()
				print('---------------------------------------------------------------------------------------------')
				print('---------------------------------------------------------------------------------------------')
			except Exception as e:
				print(str(e))
				pass
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")