from selenium import webdriver #웹 컨트롤러
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get("http://www.google.com")
l=browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
l.send_keys("뉴스") #검색어
l.send_keys(Keys.RETURN) #검색(엔터)
browser.implicitly_wait(10) #화면이 나올때까지 대기
ck=browser.find_element_by_xpath("//*[@id='rso']/div[2]/div/div/div[1]/div/a/h3")
ck.click() #클릭
browser.implicitly_wait(10)
browser.execute_script("window.scrollTo(0, 500);") #스크롤 이동
