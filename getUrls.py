import sys, time, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get(arg1, arg2, arg3):
	url = arg1
	numVids = int(arg2)
	channelid = url.split('/')[4]
	if arg3 == 'edge':
		driver = webdriver.Edge('./drivers/msedgedriver.exe')
	elif arg3 == 'firefox':
		driver = webdriver.Firefox('./drivers')
	else:
		print("Browser not specified or not supported")
		sys.exit()
	chrome_options = Options()
	chrome_options.add_argument("--user-data-dir=chrome-data")
	driver.get(url)
	time.sleep(5)
	dt=datetime.datetime.now().strftime("%Y%m%d%H%M")
	height = driver.execute_script("return document.documentElement.scrollHeight")
	lastheight = 0

	while True:
		if lastheight == height:
			break
		lastheight = height
		driver.execute_script("window.scrollTo(0, " + str(height) + ");")
		time.sleep(2)
		height = driver.execute_script("return document.documentElement.scrollHeight")

	user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
	f = open(channelid+'-'+dt+'.list', 'a+')
	for i in user_data[0:numVids]:
		link = (i.get_attribute('href'))
		f.write(link + '\n')
	f.close()
	driver.close()
