import time
from random import randint
import csv
import requests
from bs4 import BeautifulSoup

url="https://land.naver.com/news/region.naver?page="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}
li=[] #csv파일로 만들 리스트

def init_li(): #li리스트 초기화 함수
    for page in range(1,6):
        print(f"{page} 페이지 크롤링 중")
        title=[]
        contents=[]
        r=requests.get(url+str(page), headers=headers)
        r.raise_for_status()
        soup=BeautifulSoup(r.text, "html.parser")
        data1=soup.find_all('dt') #뉴스 제목
        data2=soup.find_all('li') #뉴스 내용

        for i in data1:
            if i.a:
                if len(i.a.text)!=0: #이미지들 거름
                    title.append(i.a.text)

        for i in data2:
            if i.dd:
                t=i.dd.text.strip()
                index=t.rfind('...') #...이 마지막에 등장하는 위치를 찾음
                contents.append(t[:index+3]) #...까지만 저장

        for i in range(len(title)):
            li.append([title[i], contents[i]])

        time.sleep(randint(3,6)) #크롤링 간격은 3~6초

def f(data): #파일 저장 함수
    f=open("data.csv", 'w', encoding='utf-8-sig', newline='')
    writer=csv.writer(f)
    writer.writerows(data)
    f.close()

def print_f(): #파일 출력 함수
    f=open("data.csv", 'r', encoding='utf-8-sig', newline='')
    reader=csv.reader(f)
    for i in reader:
        print(i)

def main():
    init_li()
    f(li)
    print_f()

if __name__=="__main__":
    main()