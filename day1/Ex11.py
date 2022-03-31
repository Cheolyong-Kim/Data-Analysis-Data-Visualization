from urllib.request import urlopen
import re
from html import unescape
import sqlite3

def fetch(url):
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8") #HTTP헤더로 인코딩 방식 추출
    html = f.read().decode(encoding) #추출한 인코딩 방식으로 디코딩
    return html #디코딩한 결과를 반환

def scrape(html):
    data=[]
    for i in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        url = re.search(r'<a href="(.*?)">',i).group(1) #도서의 URL을 추출
        url="http://www.hanbit.co.kr"+url
        title = re.sub(r'<.*?>', '',i) #태그를 제거해 도서의 제목 추출
        title = unescape(title)
        data.append({'url':url,"title":title})
    return data

def save(db,data):
    conn = sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data') #data 테이블이 존재하면 제거
    c.execute('''
            CREATE TABLE data (
                title text,
                url text
            )
        ''') #테이블 생성
    c.executemany('INSERT INTO data VALUES (:title, :url)', data) #데이터 저장
    conn.commit()
    conn.close()

def print_db(db): #도서들과 주소를 출력
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(i)

if __name__=="__main__":
    html=fetch("http://www.hanbit.co.kr/store/books/full_book_list.html")
    books=scrape(html)
    save('books.db', books)
    print_db('books.db')
