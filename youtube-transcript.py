import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


fp=open('url.txt')
urls=fp.readlines()
fp.close()
driver = webdriver.Firefox()

for url in urls:
	try:
		url1=url.split('=')
		url1[1]=url1[1].split('\n')
	
		out=open(url1[1][0],"wb")
		driver.get(url)
		k=driver.find_element_by_xpath("//*[@id='action-panel-overflow-button']")
		k.send_keys('\n')
		k=driver.find_element_by_xpath("//*[@data-trigger-for='action-panel-transcript']")
		k.send_keys('\n')
		t=driver.find_elements_by_xpath("//*[@class='caption-line-text']")
		while(len(t)==0):
			t=driver.find_elements_by_xpath("//*[@class='caption-line-text']")
		for l in t:
			out.write(l.text.encode('utf-8'))
			print(l.text.encode('utf-8'))
  
		
	except:
		print("error")
	out.close()
driver.close()
	
