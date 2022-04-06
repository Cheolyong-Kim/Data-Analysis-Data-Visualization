from selenium import webdriver
from bs4 import BeautifulSoup

b=webdriver.Chrome()
b.implicitly_wait(10)

b.get("http://naver.com") #네이버 접속
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="query"]').send_keys("2021 챔스\n") #2021 챔스 검색
b.implicitly_wait(10)

b.execute_script("window.scrollTo(0,document.body.scrollHeight)") #스크롤 맨 아래로
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="main_pack"]/div[3]/div/div/a[2]').click() #2페이지 클릭

for i in range(3,7):
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    html=b.page_source
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click()
    s=BeautifulSoup(html,'html.parser')
    data=s.select('a.link_tit')

    for i in data:
        print(i.text)
