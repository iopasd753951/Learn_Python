class Calculator:
    def __init__(self):     # __init__ == 생성자, 처음 만들 때 설정해준다. 처음 만들고 끄읕
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()     # Calculater 클래스를 전부 상속 받음.
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
