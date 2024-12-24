l1 = [1] 
l2 = []    #표현되는 리스크 값값
i = 1       #n번쨰 줄
n = int(input("(x+1)^n, n = "))
# n번쨰 줄까지지
r = 2   #반복 횟수 구하기기
k = 0
print(l1)
l1 = [1, 1]
if r >= 2:
    print(l1)

while r < n:
    l2 = [1, 1]
    k = 0

    while k < len(l1)-1:
        l2.insert(k+1, (l1[k] + l1[k+1]))
        k += 1
    
    l1 = l2
    print(l1)
        

    r += 1

