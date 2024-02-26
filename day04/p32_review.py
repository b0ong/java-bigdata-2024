# file: p32_review.py
# desc: 되새김 문제

## Q1

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val
        
        
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
    
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

## Q2

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.val > 100:
            self.value = 100    
cal.add(50)
cal.add(60)
print(cal.value)