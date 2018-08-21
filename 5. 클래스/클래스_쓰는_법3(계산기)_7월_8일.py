class FourCal:
    
    def __init__(self, first, second):   # init == 생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
b = FourCal(5, 10)

print(a.mul())
print(b.mul())
