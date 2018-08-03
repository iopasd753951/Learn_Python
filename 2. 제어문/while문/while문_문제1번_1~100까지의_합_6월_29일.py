a = 1
cnt = 1
sum = 0

while 1:
    sum += a
    a += 1
    cnt = cnt + 1
    if cnt == 101:
        break


print("1 ~ 100까지의 총 합은 %d이다" % sum)
