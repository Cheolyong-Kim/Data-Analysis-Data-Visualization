#정규식 표현
#.=문자
#^=시작
#$=끝
#정규식: 원하는 형태에 따른 문자열 선택할 수 있게 해줌
#match("문자열"): 처음부터 일치하는지 검사
#search("문자열"): 일치하는 문자가 있는지 검사
#findall("문자열"): 일치하는 모든 것의 리스트 출력

import re

def print_t(str):
    if str:
        print("일치문자", str.group())
        print("입력문자", str.string)
        print("일치문자 시작", str.start())
        print("일치문자 끝", str.end())
        print("일치문자 시작, 끝", str.span())
    else:
        print("일치 없음")

l=['abcd','adcd','accd','abdc', 'casdfd', 'cabcdd', 'c1234d', 'cddddd']
ck=re.compile('^c....d$')
for i in l:
    str=ck.match(i)
    print_t(str)
    str=ck.search(i)
    print_t(str)
    str=ck.findall(i)
    print(str)

# print('\n')
# ck=re.compile('^ab')
# for i in l:
#     print("시작: ", ck.match(i))
#     print("일치: ", ck.search(i))
#     print("all_data: ", ck.findall(i))
#
# print('\n')
# ck=re.compile('cd$')
# for i in l:
#     print("시작: ", ck.match(i))
#     print("일치: ", ck.search(i))
#     print("all_data: ", ck.findall(i))

