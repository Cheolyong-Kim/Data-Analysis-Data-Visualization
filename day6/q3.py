import numpy as np

scores=np.random.randint(0,100,100)
print(scores)

if scores.mean()>=50:
    print("전원 통과")

if (scores>=50).all():
    print("학년 1등반")

if (scores==100).any():
    print("학년 1등반")