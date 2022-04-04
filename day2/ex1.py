import requests

r=requests.get("http://www.hanbit.co.kr/store/books/full_book_list.html")
r.raise_for_status() #접근하지 못하면 하위 코드 실행하지 않게 함
#print(r.text)
with open("data.html", "w", encoding='utf-8') as f:
    f.write(r.text)
