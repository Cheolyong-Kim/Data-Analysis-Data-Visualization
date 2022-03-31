#meta 태그에서 인코딩 방식 추출하기

import sys
import re
from urllib.request import urlopen
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
bytes_content = f.read()
scanned_text = bytes_content[:1024].decode('ascii', errors='replace') #응답 본문 앞부분 1024바이트를 ascii문자로 디코딩

match = re.search(r'charset=["\']?([\w-]+)', scanned_text) #디코딩한 문자열에서 정규 표현식으로 charset값을 추출

if match:
    encoding = match.group(1)
else: #charset이 명시돼 있지 않으면 utf-8사용
    encoding = 'utf-8'
print('encoding:', encoding, file=sys.stderr) #추출한 인코딩을 표준 오류에 출력
text = bytes_content.decode(encoding) #추출한 인코딩으로 다시 디코딩
print(text) #디코딩한 내용을 출력