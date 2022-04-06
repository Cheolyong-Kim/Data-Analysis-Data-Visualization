import time
from selenium import webdriver

b=webdriver.Chrome()
b.maximize_window() #크기 결정
b.implicitly_wait(10)

b.get("http://www.google.com") #구글 접속
b.implicitly_wait(10)

b.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("뉴스\n") #검색창에 뉴스 입력
b.implicitly_wait(10)

b.execute_script("window.scrollTo(0,500)") #스크롤 내리기
b.find_element_by_xpath('//*[@id="rso"]/div[2]/div/div/div[1]/div/a/h3').click() #구글 뉴스 클릭
b.implicitly_wait(10)

while True: #스크롤 계속 내리기
    info_n = b.execute_script("return document.body.scrollHeight")
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

    next_n=b.execute_script("return document.body.scrollHeight")
    if info_n==next_n: #모든 내용을 담고 있는 최하단
        break


