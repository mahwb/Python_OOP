class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, num, *nums):
        if isinstance(num, int):
            self.sum += num
        else:
            for i in range(0, len(num)):
                self.sum += num[i]
        for i in range(0, len(nums)):
            if isinstance(nums[i], int):
                self.sum += nums[i]
            else:
                for j in range(0, len(nums[i])):
                    self.sum += nums[i][j]
        return self

    def subtract(self, num, *nums):
        if isinstance(num, int):
            self.sum -= num
        else:
            for i in range(0, len(num)):
                self.sum -= num[i]
        for i in range(0, len(nums)):
            if isinstance(nums[i], int):
                self.sum -= nums[i]
            else:
                for j in range(0, len(nums[i])):
                    self.sum -= nums[i][j]
        return self
    
    def result(self):
        print self.sum
        return self

MathDojo().add(2).add(2, 5).subtract(3, 2).result()
MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
