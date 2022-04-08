import csv
import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from bs4 import BeautifulSoup

def f(i,n): #입력한 n만큼 i를 next_sibling하여 데이터를 텍스트로 추출하는 함수
    for n in range(n):
        i=i.next_sibling
    return i.text.strip()

op=webdriver.ChromeOptions()
op.headless=True #웹 창을 띄우지 않고 진행
op.add_argument("window-size=1920x1080") #윈도우 사이즈 지정
op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36') #유저에이전트 설정
b=webdriver.Chrome(options=op) #크롬에 옵션 추가
b.maximize_window()
b.get("http://naver.com") #네이버 켜기
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="query"]').send_keys("금융\n") #금융 검색
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="web_1"]/div/div[2]/div[2]/a').click() #네이버 금융 클릭
b.implicitly_wait(10)

b.switch_to.window(b.window_handles[1]) #새 창으로 전환
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a/span').click() #시장지표 탭 클릭
b.implicitly_wait(10)

b.execute_script("window.scrollTo(0,700)") #스크롤 내리기
b.implicitly_wait(10)

b.find_element_by_xpath('//*[@id="tab_section"]/ul/li[2]/a/span').click() #국제시장 환율 탭 클릭
b.implicitly_wait(10)

e=b.find_element_by_id("frame_ex2") #내가 원하는 프레임 찾기
b.implicitly_wait(10)

b.switch_to.frame(e) #찾은 프레임으로 이동

li_d=[] #최종 저장할 리스트
header="통화명","심볼","현재가","전일대비","등락율"
for page in range(1,5):
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)") #스크롤 내리기
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'/html/body/div/div/a[{page}]').click() #page페이지 클릭
    print(f"{page}페이지 진행 중")
    s=BeautifulSoup(b.page_source, 'html.parser') #프레임 소스 가져오기

    data=s.find_all('tr')

    cos=[] #통화명 리스트
    sb=[] #심볼 리스트
    cp=[] #현재가 리스트
    dtd=[] #전일대비 리스트
    fr=[] #등락율 리스트
    for i in data:
        if i.td:
            cos.append(i.td.text.strip())
            sb.append(f(i.td,2))
            cp.append(f(i.td,4))
            if i.img['alt']=="상승": #이미지의 alt태그값이 상승이라면
                dtd.append('+'+f(i.td,6)) #+를 붙여서 저장
            elif i.img['alt']=="하락": #이미지의 alt태그값이 하락이라면
                dtd.append('-'+f(i.td,6)) #-를 붙여서 저장
            else: #보합의 경우는 추가없이 저장
                dtd.append(f(i.td,6))
            fr.append(f(i.td,8).replace('\n','').replace('\t','').replace(' ',''))

    for i in zip(cos, sb, cp, dtd, fr):
        li_d.append(i)
b.quit() #웹 닫기

fp=open('data.csv','w',encoding='utf-8-sig',newline='') #파일 쓰기
writer=csv.writer(fp)
writer.writerow(header) #헤더 입력
writer.writerows(li_d) #내용 입력
fp.close() #파일 닫기

df=pd.read_csv("data.csv",encoding='utf-8-sig')
df=DataFrame(df)
print(df)

t1=df[(df['등락율']>'-') & (df['등락율']!='0.00%')].reset_index(drop='index')
t2=df[df['등락율']<'-'].reset_index(drop='index')

print(t1)
print('')
print(t2)