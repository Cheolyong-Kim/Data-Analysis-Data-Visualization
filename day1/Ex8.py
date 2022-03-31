import csv
with open("data.csv",'w',newline='') as f:
    wd = csv.DictWriter(f,["key1","key2","key3"]) #파일에 입력하는게 아니라 키 값을 설정하는 것
    wd.writeheader() #키 값이 헤더로 설정되고 파일 첫 줄에 입력됨.
    wd.writerow({"key1":10,"key2":20,"key3":30})
    wd.writerows(({"key1":10,"key2":20,"key3":30},
                 {"key1":10,"key2":20,"key3":30},
                 {"key1":10,"key2":20,"key3":30},
                 {"key1":10,"key2":20,"key3":30}))
    # 헤더로 설정한 키 중에 없는 키에 값을 넣으려고 하면 에러 발생. 딕셔너리처럼 키 값을 생성해서 값을 넣지 않음