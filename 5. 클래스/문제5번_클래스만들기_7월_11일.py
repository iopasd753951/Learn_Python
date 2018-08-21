class Calculator:
    def __init__(self, val):
        self.val = val

    def sum(self):
        result = 0
        
        for i in self.val:
            result += i

        return result

    def avg(self):
        total = self.sum()

        return total / len(self.val)

cal1 = Calculator([1,2,3,4,5])

print(cal1.sum())
print(cal1.avg())
