from selenium import webdriver
from bs4 import BeautifulSoup
import csv

def f(a,li_d,file_name): #파일 저장 함수
    f=open(file_name, 'w', encoding='utf-8-sig', newline='')
    writer=csv.writer(f)
    writer.writerow(a)
    writer.writerows(li_d)
    f.close()

def print_f(file_name): #파일 출력 함수
    f=open(file_name, 'r', encoding='utf-8-sig', newline='')
    reader=csv.reader(f)
    skip=True
    for i in reader:
        if skip:
            skip = False
            continue
        print(i[0])
        print(i[1])
        print('')
    f.close()

b=webdriver.Chrome()
b.implicitly_wait(10)

b.get("http://naver.com") #네이버 접속
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="query"]').send_keys("암호화폐\n") #암호화폐 검색
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click() #뉴스 클릭
b.implicitly_wait(10)


li_d=[] #csv파일 만들때 사용할 리스트
a="제목", "내용"
for i in range(1,6):
    title = []  # 기사 제목 리스트
    contents = []  # 기사 내용 리스트
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 스크롤 맨 아래로 내리기
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click()  # i페이지 클릭
    b.implicitly_wait(10)
    html=b.page_source
    b.implicitly_wait(10)
    print(f"{i}페이지 진행중")

    s=BeautifulSoup(html,'html.parser')
    data1=s.find_all('a', attrs={"class":"news_tit"})
    data2=s.find_all('a', attrs={"class":"api_txt_lines dsc_txt_wrap"})

    for i in data1: #기사 제목 추출
        if i.text:
            title.append(i.text)

    for i in data2: #기사 내용 추출
        contents.append(i.text)

    for i in range(len(title)):  # 2차원 리스트 만들기
        li_d.append([title[i], contents[i]])

f(a,li_d,"news.csv")
print_f("news.csv")



