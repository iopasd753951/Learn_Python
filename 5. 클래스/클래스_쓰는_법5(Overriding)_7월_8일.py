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

class SafeFourCal(FourCal):    # 상속을 먼저 해줌
        def div(self):          # overriding == 덮어쓰기 == div를 써서 수정가능하게 해
            if self.second == 0:
                return 0
            else:
                return self.first / self.second

a = SafeFourCal(3, 0)

print(a.div())
