A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
i = []
sum = 0
avg = 0
cnt = 0

for i in A:
    sum = sum + i
    cnt += 1

avg = sum / cnt

print(avg)
