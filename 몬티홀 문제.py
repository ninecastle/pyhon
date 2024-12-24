import random

sh1 = [0, 1, 2]

def rd():
    return random.randint(0, 2)

# print(random.choice(자리))
k = 0   #선택한 자리 수
x = 0   #자리 제거 변수
cnt = 0 #횟수 세기
ch = 0

i = 1
while i <= 100000000:
    i += 1
    ch = rd()
    k = rd()
    sh1 = [0, 1 ,2]
    sh1[k] = 100
    
    if ch == k:
        pass
        
    else:
        cnt += 1

print(cnt/(i-1))