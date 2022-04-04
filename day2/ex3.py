import requests
from bs4 import BeautifulSoup

url="http://www.hanbit.co.kr/store/books/full_book_list.html"
r=requests.get(url) #html 가져오기

soup=BeautifulSoup(r.text, "html.parser") #가져온 html 정리
#print(soup.title.get_text())
#print(soup.a['href'])
#print(soup.find('a', attrs={"href":"/store/books/look.php?p_code=B9483006177"}).get_text())
#print(soup.find('a', attrs={"href":"/store/books/look.php?p_code=B5744853316"}).get_text())
#print(soup.find(attrs={"href":"/store/books/look.php?p_code=B5744853316"}))
#print(soup.find('div', attrs={'class': "full_book_list_wrap"}))
#print(soup.find_all('div')) #설정한 태그를 포함한 모든 내용을 찾음
t=soup.find("div")
sub_t=list(t)[:2]
for i in sub_t:
    print(i.get_text())
    print("---")
