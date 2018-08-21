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

class MoreFourCal(FourCal):        # 상속
    def pow(self):
        result = self.first ** self.second
        return result
        
a = MoreFourCal(4, 2)

print(a.pow())
