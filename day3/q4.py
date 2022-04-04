import time
import csv
import requests
from bs4 import BeautifulSoup

url='https://news.naver.com/main/list.naver?mode=LS2D&sid2=228&sid1=105&mid=shm&date=20220404&page='
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
li_d=[] #csv파일에 저장할 리스트

def init_li_d(): #li_d를 초기화하는 함수
    for page in range(1, 6): #5페이지까지
        title=[] #뉴스 제목을 저장하는 리스트
        sh=[] #뉴스 소제목을 저장하는 리스트
        print(f"{page}페이지 크롤링 중")
        r=requests.get(url + str(page), headers=headers)
        r.raise_for_status()
        soup=BeautifulSoup(r.text, "html.parser")
        data1=soup.select("dt") #뉴스 제목
        data2=soup.find_all("span", "lede") #뉴스 소제목

        for i in data1:
            if i.text.strip()!='' and i.text.strip()!="동영상기사": #뉴스제목 이외의 것들을 제외
                title.append(i.text.strip())

        for i in data2:
            sh.append(i.text.strip())

        for i in range(len(title)):
            li_d.append([title[i], sh[i]])

        time.sleep(5) #크롤링은 5초 간격으로

def f(data):
    f=open("data.csv", 'w', encoding='utf-8-sig', newline='')
    writer=csv.writer(f)
    writer.writerows(data)
    f.close()

def main():
    init_li_d()
    f(li_d)

if __name__=="__main__":
    main()