import time
from random import randint
import csv
import requests #수집
from bs4 import BeautifulSoup #정리

url="https://movie.naver.com/movie/point/af/list.naver?&page=" #파일이름

#파일 내용 정리
title="영화명","평점","리뷰"
f=open("save.csv", 'w', encoding='utf-8-sig', newline='') #한글 저장하려면 utf-8-sig로 인코딩할 것
writer=csv.writer(f)
writer.writerow(title)
in_data=[]

#data 수집
for page in range(1,6):
    print(f"{page}페이지 크롤링 중")
    r=requests.get(url+str(page))
    r.raise_for_status() #접속 상태 확인 (접속 코드 200 아닐시 예외 발생)
    soup=BeautifulSoup(r.text,"html.parser")
    data=soup.find_all("td",attrs={"class":"title"})
    
    #파일 정리
    for i in data:
        if i.a:
            #단일 입력
            #in_data=[i.a.text, i.em.text, i.br.next_sibling.strip()]
            #writer.writerow(in_data)
            in_data.append([i.a.text, i.em.text, i.br.next_sibling.strip()])
    time.sleep(randint(5,10)) #sleep을 추가하지 않으면 IP밴 당할 수도 있음

#저장
writer.writerows(in_data)