class Calculator:
    def __init__(self, value):      # value 값을 0으로 해주거나, 
        self.value = value

    def add(self, val):
        self.value += val

cal = Calculator(0)             # Calculator에 아무값이나 넣어준다.
cal.add(3)
cal.add(4)

print(cal.value)
