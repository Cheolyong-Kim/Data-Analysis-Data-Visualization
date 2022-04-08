l=[1,2,3,4]
l1=[1,2,3]
l2=[1,2]
al=[l,l1,l2]
print(l+l1) #리스트 연결

import numpy as np
a=np.array([1,2,3,4])
a1=np.array([1,2,3,4])
print(a+a1) #넘파이 배열 덧셈

l=[[1,2,3,4],[1,2,3]]
# np.array(l) #각 값의 메모리 크기가 같아야함
np.full((2,2),10)