from selenium import webdriver
from bs4 import BeautifulSoup

op=webdriver.ChromeOptions()
op.headless=True #간접적으로 창을 열어서 확인
op.add_argument("window-size=1920x1080") #윈도우 사이즈 지정
op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36')
b=webdriver.Chrome(options=op)
b.maximize_window()
b.get("https://biz.chosun.com/it-science/ict/2022/04/04/KKSP7ZV6MFFLLINOIU4NN7QINE/?utm_source=naver&utm_medium=original&utm_campaign=biz")
s=BeautifulSoup(b.page_source, 'html.parser')
b.quit()