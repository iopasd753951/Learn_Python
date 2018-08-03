A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
i = 0
sum = 0
cnt = 0

while 1:
    if A[i] >= 50:
        sum = sum + A[i]
    i += 1
    cnt += 1
    if cnt == 9:
        break
    
print(sum)        
        
