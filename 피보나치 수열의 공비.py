an = [0, 1, 1, 2, 3]
i = 6


while abs((an[i-3] / an[i-4]) - (an[i-2] / an[i-3])) > (
    0.0000000000000000000000000000000000000001):
    an.append(an[i-2] + an[i-3])
    # print(an)
    i += 1
    # print(an[i-2] / an[i-3])


k = an[i-2] / an[i-3]
r = (1 + (5 ** 0.5)) / 2
print(k)
print(r)
print(k-r)