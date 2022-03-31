#HTTP 헤더에서 인코딩 방식 추출하기

import sys
from urllib.request import urlopen
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
encoding = f.info().get_content_charset(failobj="utf-8") #HTTP 헤더를 기반으로 인코딩 방식을 추출, 명시돼있지 않을 경우 utf-8사용
print('encoding:', encoding, file=sys.stderr) #인코딩 방식을 표준 오류에 출력
text = f.read().decode(encoding) #추출한 인코딩 방식으로 디코딩
print(text) #디코딩한 내용을 출력