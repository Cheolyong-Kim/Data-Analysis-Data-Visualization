import csv
with open("data.csv",'w',newline='') as f:
    wd=csv.writer(f)
    wd.writerow(["data1","data2","data2"]) #단순히 문자열로 써짐. 키 값이 아님
    wd.writerows([[10,20],[10,20],[10,20],[10,20],[10,20]]) #데이터가 이미 1차원보다 크면 writerows를 쓰지만 1차원이라면 writerow를 반복문으로 사용해도 됨.