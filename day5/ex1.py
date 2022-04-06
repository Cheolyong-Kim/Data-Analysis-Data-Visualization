from selenium import webdriver

b=webdriver.Chrome()
b.implicitly_wait(10)

b.get("http://naver.com")
b.implicitly_wait(10)

