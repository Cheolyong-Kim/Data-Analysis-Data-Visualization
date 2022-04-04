import sqlite3
import requests
from bs4 import BeautifulSoup

def f(i,x):
    for n in range(x):
        i=i.next_sibling
    return i.text.strip()

def save_d(db,data):
    conn = sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
        CREATE TABLE data (
            name text,
            cp text,
            ft text,
            fr text,
            tv text,
            ta text,
            bp text,
            ap text,
            mc text,
            PER text,
            ROE text
            )'''
        )
    c.executemany('INSERT INTO data VALUES (:name, :cp, :ft, :fr, :tv, :ta, :bp, :ap, :mc, :PER, :ROE)', data)
    conn.commit()
    conn.close()

def print_d(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')  # 저장한 데이터를 추출
    for i in c.fetchall():  # 쿼리의 결과를 fetchall메소드로 추출
        print(f"종목명: {i[0]} | 현재가: {i[1]} | 전일비: {i[2]} | 등락률: {i[3]} | 거래량: {i[4]} | 거래대금: {i[5]} | 매수호가: {i[6]} | 매도호가: {i[7]} | 시가총액: {i[8]} | PER: {i[9]} | ROE: {i[10]}")

def main():
    url="https://finance.naver.com/sise/sise_quant.naver?sosok=1"
    r=requests.get(url)

    soup=BeautifulSoup(r.text, "html.parser")
    data=soup.select("td")

    li_d=[]
    db="data.db"
    for i in data:
        if i.a:
            li_d.append({"name":f"{i.a.text}", "cp":f"{f(i,2)}", "ft":f"{f(i,4)}", "fr":f"{f(i,6)}", "tv":f"{f(i,8)}"
                        , "ta":f"{f(i,10)}", "bp":f"{f(i,12)}", "ap":f"{f(i,14)}", "mc":f"{f(i,16)}", "PER":f"{f(i,18)}", "ROE":f"{f(i,20)}"})

    save_d(db,li_d)
    print_d(db)

if __name__=="__main__":
    main()

