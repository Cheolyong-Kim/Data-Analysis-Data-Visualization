import sqlite3
import requests
from bs4 import BeautifulSoup

def save_d(db,data):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
        CREATE TABLE data (
            rank text,
            team text,
            win text,
            lose text,
            winrate text,
            gl text
            )'''
        )
    c.executemany('INSERT INTO data VALUES (:rank, :team, :win, :lose, :winrate, :gl)', data)
    conn.commit()
    conn.close()

def print_d(db):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('SELECT * FROM data')
    print("순위 | 팀명 | 승 | 패 | 승률 | 득실")
    for i in c.fetchall():
        print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]}")
    conn.close()

def init_li():
    ranking=[]
    d_li=[]
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjFE&pkid=475&os=25567154&qvt=0&query=2022%20LoL%20%EC%B1%94%ED%94%BC%EC%96%B8%EC%8A%A4%20%EC%BD%94%EB%A6%AC%EC%95%84%20%EC%8A%A4%ED%94%84%EB%A7%81%20%EC%A0%95%EA%B7%9C%EC%88%9C%EC%9C%84"
    r = requests.get(url)

    soup=BeautifulSoup(r.text, "html.parser")
    data=soup.select("td")

    for i in data:
        ranking.extend(i.text.split('    '))

    for i in range(0,len(ranking),6):
        d_li.append({"rank":ranking[i].lstrip(), "team":ranking[i+1].rstrip(), "win":ranking[i+2], "lose":ranking[i+3], "winrate":ranking[i+4], "gl":ranking[i+5]})

    return d_li

def main():
    init_li()
    save_d("data.db",init_li())
    print_d("data.db")

if __name__=="__main__":
    main()

