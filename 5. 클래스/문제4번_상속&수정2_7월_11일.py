class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self,val):
        if val >= 100:
            print(0)

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
