import sqlite3
import requests
from bs4 import BeautifulSoup

def save_d(db,data):
    conn = sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
        CREATE TABLE data (
            title text,
            reviewer text,
            review text
            )'''
        )
    c.executemany('INSERT INTO data VALUES (:title, :reviewer, :review)', data)
    conn.commit()
    conn.close()

def print_d(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    for i in c.fetchall():
        print(f"{i[0]}\n{i[2]}\t{i[1]}\n")
    conn.close()

def init_li():
    title = [] #영화 제목 데이터를 추출해서 넣을 리스트
    reviewer = [] #리뷰한 사람의 닉네임의 데이터를 추출해서 넣을 리스트
    review = [] #리뷰 내용 데이터를 추출해서 넣을 리스트
    m_dic_li = [] #얻은 데이터들로 만든 딕셔너리를 넣을 리스트
    url = "https://movie.naver.com/movie/point/af/list.naver?&page=10"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    data1=soup.select("a.movie.color_b") #영화 제목
    data2=soup.select("a.author") #리뷰어
    data3=soup.find_all("td", "title") #리뷰

    for i in data1:
        title.append(i.text)

    for i in data2:
        reviewer.append(i.text)

    for i in data3:
        review.append(i.br.next_sibling.strip())

    for i in range(len(data1)):
        m_dic_li.append({"title":title[i], "reviewer":reviewer[i], "review":review[i]})

    return m_dic_li

def main():
    init_li()
    save_d("data.db", init_li())
    print_d("data.db")

if __name__=="__main__":
    main()
