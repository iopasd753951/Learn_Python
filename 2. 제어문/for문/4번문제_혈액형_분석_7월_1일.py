blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
A = 0
B = 0
O = 0
AB = 0
i = 0

for i in blood :
    if i == 'A':
        A += 1
    elif i == 'B':
        B += 1
    elif i == 'O':
        O += 1
    elif i == 'AB':
        AB += 1

print("A형은 %d명" % A)
print("B형은 %d명" % B)
print("O형은 %d명" % O)
print("AB형은 %d명" % AB)
