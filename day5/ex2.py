from selenium import webdriver
from bs4 import BeautifulSoup

b=webdriver.Chrome()
b.implicitly_wait(10)

b.get("http://naver.com") #네이버 접속
b.implicitly_wait(10)

c=b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click() #뉴스 클릭
b.implicitly_wait(10)

c2=b.find_element_by_xpath('/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[6]/a/span').click() #IT/과학 클릭
b.implicitly_wait(10)

c3=b.find_element_by_xpath('//*[@id="snb"]/ul/li[4]/a').click() #IT/일반 클릭
b.implicitly_wait(10)

for i in range(1,6):
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)") #스크롤 맨 아래로 내리기
    b.implicitly_wait(10)
    html = b.page_source
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'//*[@id="main_content"]/div[3]/a[{i}]').click() #i페이지 클릭
    b.implicitly_wait(10)

    s=BeautifulSoup(html, 'html.parser')
    data=s.select('dl')

    for i in data:
        if i.a:
            print(i.dd.previous_sibling.previous_sibling.a.text.strip()) #뉴스 제목
            print(i.dd.span.text.strip()) #뉴스 내용
            print('')