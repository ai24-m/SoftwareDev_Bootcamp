class MathDojo:
    def __init__(self) :
        self.result=0
    def _add(self, *num):
        self.add = 0
        for i in num:
            self.add += i
        self.result += self.add
        return self
    def subtract(self, *nums):
        self.sub = 0
        for x in nums:
            self.sub += x
        self.result -= self.sub
        return self

    # def add(self,*num):
    # for i in num
    #     self.result= int(num) + int(nums)
    #     return self.result

    # def substrac(self,*nums):
    # for x in nums
    #     self.nums = nums 
    #     self.nums2 =nums


md = MathDojo()

x = md._add(2)._add(2,5,1).subtract(3,2).result
print(x)