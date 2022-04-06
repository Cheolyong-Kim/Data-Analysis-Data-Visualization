import csv
from selenium import webdriver
from bs4 import BeautifulSoup

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

op=webdriver.ChromeOptions()
op.headless=True #웹 창을 띄우지 않고 진행
op.add_argument("window-size=1920x1080") #윈도우 사이즈 지정
op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36') #유저에이전트 설정
b=webdriver.Chrome(options=op) #크롬에 옵션 추가
b.maximize_window()
b.get("http://naver.com") #네이버 켜기
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="query"]').send_keys("T1\n") #T1 검색
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click() #뉴스 탭 클릭
b.implicitly_wait(10)

a="제목","내용"
file_name="news2.csv"
li_d=[] #최종적으로 csv파일에 저장할 리스트
for i in range(1,6):
    title=[]
    contents=[]
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)") #스크롤 맨 아래로 내리기
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click() #i페이지 클릭
    b.implicitly_wait(10)
    s=BeautifulSoup(b.page_source,'html.parser')
    print(f"{i}페이지 진행 중")

    data1=s.find_all('a', attrs={"class":"news_tit"}) #뉴스 제목 추출
    data2=s.find_all('a', attrs={"class":"api_txt_lines dsc_txt_wrap"}) #뉴스 내용 추출

    for i in data1: #뉴스 제목을 하나씩 꺼내서 title리스트에 추가
        if i.text:
            title.append(i.text)

    for i in data2: #뉴스 내용을 하나씩 꺼내서 contents리스트에 추가
        contents.append(i.text)

    for i in zip(title, contents): #뉴스 제목과 뉴스 내용을 각각 zip하여 li_d리스트에 추가
        li_d.append(i)

b.quit() #웹 닫기
f(a,li_d,file_name)
print_f(file_name)


