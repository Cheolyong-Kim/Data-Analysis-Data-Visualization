import sqlite3
conn = sqlite3.connect("data.db")
c=conn.cursor()
c.execute('DROP TABLE IF EXISTS cities') #cities 테이블이 이미 존재한다면 제거
c.execute('''
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
''') #테이블 생성
#데이터 저장↓
c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '상하이', 24150000))
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
          {'rank': 2, 'city': '카라치', 'population': 23500000})
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city': '베이징', 'population': 21516000},
    {'rank': 4, 'city': '텐진', 'population': 14722100},
    {'rank': 5, 'city': '이스탄불', 'population': 14160467},
])
c.executemany('INSERT INTO cities VALUES (?, ?, ?)', [(1, '상하이', 24150000),(1, '상하이', 24150000),(1, '상하이', 24150000),(1, '상하이', 24150000)])
conn.commit()

c.execute('SELECT * FROM cities') #저장한 데이터를 추출
for i in c.fetchall(): #쿼리의 결과를 fetchall메소드로 추출
    print(i)
    #print(type(i))
conn.close()