'''This program takes file of a engineering subject 
which consist of all the course number line by line
one course number each line. The output is set of files
each having all the youtube urls

date: Jan 13 , 2014
====================
removed the bug '\n'
''' 
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
driver = webdriver.Firefox()
courseFile=sys.argv[1]
fp_courseFile=open(courseFile)
courseNos=fp_courseFile.readlines()

for courseNo in courseNos:
	try:
		courseNo=courseNo.split('\n')
		courseNo=courseNo[0]
		course='http://nptel.ac.in/courses/'+courseNo+'/'

		NoOfLec=100
		count=1
		
		fp=open(courseNo,'w')
		while(count<NoOfLec):
			try:
				url=course+str(count)
			
				'''driver = webdriver.PhantomJS()'''
				driver.get(url)
				k=driver.find_element_by_xpath("//param[@name='movie']")
				link=k.get_attribute('value')
				link=link.split('?')
				link=link[0]
				link=link.split('/v/')
				m=link[0]+ "/watch?v=" +link[1]
				fp.write(m)
				fp.write('\n')
				print(m)
			
			
			except:
				print("error"+count)
			
		
		
			count=count+1
		
		fp.close()
	except:
		print("course completed")

driver.close()



