import time
from random import randint

# print("출력")
# time.sleep(1) #입력한 초만큼 기다렸다가 다음 코드 실행
# print("종료")

#고정된 시간간격으로 크롤링해도 의심받을 수 있기 때문에 시간간격을 랜덤으로 준다.
print("출력")
for i in range(10):
    p=randint(3,10)
    print(p)
    time.sleep(p)
print("종료")