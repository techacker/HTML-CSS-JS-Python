# Day 17: More Exceptions

class Calculator:
    def power(self, fNum, sNum):
        self.fNum = fNum
        self.sNum = sNum
        if self.fNum < 0 or self.sNum < 0:
            raise ValueError('n and p should be non-negative')
        return self.fNum ** self.sNum        


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
