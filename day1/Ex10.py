import html
data="<span class=veta_bd_t> data </span>"
out_data=html.escape(data) #escape로 태그 기능 제거
print(out_data)
c_data=html.unescape(out_data) #unescape로 제거했던 태그를 복구
print(c_data)