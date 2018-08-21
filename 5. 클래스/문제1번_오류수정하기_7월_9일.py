
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):          # 문제에서는 (self,)가 빠져있어서 값을 받을 수 가 없었음. 하지만 (self,)를 추가하여 값을 할당 받을 수 있도록 해줌.
        self.value += val

cal = Calculator()
cal.add(3)
cal.add(4)

print(cal.value)
