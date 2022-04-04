import sqlite3

data=[{"name":"에이비프로바이오", "PER":"-21.48"}]
db="data.db"

def save(db,data):
    conn = sqlite3.connect(db)
    c=conn.cursor()
    c.execute('DROP TABLE IF EXISTS data')
    c.execute('''
        CREATE TABLE data (
            name text,
            PER text
            )'''
        )
    c.executemany('INSERT INTO data VALUES (:name, :PER)',data)
    conn.commit()
    conn.close()

def print_d(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM data')  # 저장한 데이터를 추출
    for i in c.fetchall():  # 쿼리의 결과를 fetchall메소드로 추출
        print(i)

save(db,data)
print_d(db)