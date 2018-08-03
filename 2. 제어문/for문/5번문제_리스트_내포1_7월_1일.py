number = [1, 2, 3, 4, 5]
result = []

'''
for n in number:
    if n % 2 == 1:
        result.append(n*2)
'''

result = [n*2 for n in number if n % 2 == 1]

print(result)
