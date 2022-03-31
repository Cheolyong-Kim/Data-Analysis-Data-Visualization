from urllib.request import urlopen
f=urlopen("http://www.hanbit.co.kr")
print(f.read()) #HTTP 응답 본문(bytes 자료형)
print(f.status) #HTTP 응답 코드
print(f.getheader("Content-Type")) #HTTP 헤더