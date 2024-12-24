import random

m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]
m28 = [2]
# month = 0
# day = 0
pb = [] #people birthday

def birth():
    month = random.randint(1, 12)
    if month in m31:
        day = random.randint(1, 31)
    elif month in m30:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 28)
    return (month, day)


# N = int(input("몇 명? : "))
# cnt = 0
# len = 1000000
# k = 1
while True:
    cnt = 0
    len = 1000000
    N = int(input("몇 명? : "))

    if N == 0: 
        break

    for k in range(len):
        pb.clear()
        i = 1
        while i <= N:
            i += 1
            x = birth()
            pb.append(x)
            pb.sort()
        # print(pb)   
        #pb의 길이는 (N-1), 
        # 두 쌍씩 묵으면 리스트 0부터 N-2
        for d in range(0, N-2):
            if pb[d] == pb[d+1]:
                # print(pb, pb[d], pb[d+1])
                cnt += 1
                break
            else:
                pass
    
    cnt = cnt / (len) * 100
    cnt = round(cnt, 4)
    print(f"{cnt}%")