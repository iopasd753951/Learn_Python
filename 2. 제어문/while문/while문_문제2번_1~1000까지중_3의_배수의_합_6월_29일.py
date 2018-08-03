a = 1
cnt = 0
sum = 0

while 1:
    a += 1
    if a % 3 == 0:
        sum += a
    cnt += 1    
    if cnt == 1000:
        break

print("1~100중 3의 배수들의 합은 %d이다." % sum)
