from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

id="aaa"
pw="123"

b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("http://www.naver.com")
b.implicitly_wait(10)
lc=b.find_element_by_xpath("//*[@id='account']/a")
lc.click()
b.implicitly_wait(10)

in_id=b.find_element_by_xpath("//*[@id='id']")
b.implicitly_wait(10)
in_id.click()
pyperclip.copy(id) #클립보드에 복사
in_id.send_keys(Keys.CONTROL, 'v') #붙여넣기
b.implicitly_wait(10)

in_pw=b.find_element_by_xpath("//*[@id='pw']")
b.implicitly_wait(10)
in_pw.click()
pyperclip.copy(pw) #클립보드에 복사
in_pw.send_keys(Keys.CONTROL, 'v') #붙여넣기
b.implicitly_wait(10)

b.find_element_by_id("log.login").click() #로그인
b.implicitly_wait(10)

news=b.find_element_by_xpath("//*[@id='NM_FAVORITE']/div[1]/ul[2]/li[2]/a") #뉴스 들어가기
news.click()
b.implicitly_wait(10)

news=b.find_element_by_xpath("/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[6]/a/span") #IT/과학 들어가기
news.click()
b.implicitly_wait(10)

news=b.find_element_by_xpath("//*[@id='snb']/ul/li[4]/a") #IT/일반 들어가기
news.click()
b.implicitly_wait(10)

data_l=[]
for i in range(1,11): #기사제목 10개 수집
    data_l.append(b.find_element_by_xpath(f"//*[@id='main_content']/div[2]/ul[1]/li[{i}]/dl/dt[2]/a").text)
    b.implicitly_wait(10)

for i in data_l: #수집한 기사제목 출력
    print(i)