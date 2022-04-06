from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b=webdriver.Chrome()
b.implicitly_wait(10)

b.get("http://www.google.com") #구글 접속
b.implicitly_wait(10)

s=b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') #검색창 위치
s.send_keys('파이튜터') #검색어 입력
s.send_keys(Keys.ENTER) #엔터 입력
b.implicitly_wait(10)

l=b.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3') #파이튜터 링크 위치
l.click() #클릭
b.implicitly_wait(10)

l2=b.find_element_by_xpath('//*[@id="learnPane"]/p[1]/a/b') #파이썬 튜터 링크 위치
l2.click()
b.implicitly_wait(10)
