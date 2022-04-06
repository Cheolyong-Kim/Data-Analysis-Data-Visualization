from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
id="aaa"
pw="123"

b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("http://www.naver.com")
b.implicitly_wait(10)
lc=b.find_element_by_class_name("link_login")
lc.click()
b.implicitly_wait(10)

in_id=b.find_element_by_id('id')
b.implicitly_wait(10)
in_id.click()
pyperclip.copy(id) #클립보드에 복사
in_id.send_keys(Keys.CONTROL, 'v') #붙여넣기
b.implicitly_wait(10)

in_pw=b.find_element_by_id('pw')
b.implicitly_wait(10)
in_pw.click()
pyperclip.copy(pw) #클립보드에 복사
in_pw.send_keys(Keys.CONTROL, 'v') #붙여넣기
b.implicitly_wait(10)

b.find_element_by_id("log.login").click()
b.implicitly_wait(10)

news=b.find_element_by_class_name('nav')
news.click()
b.implicitly_wait(10)