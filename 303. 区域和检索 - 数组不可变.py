class NumArray:
    def __init__(self, nums):
        self.n = [0]
        for index in range(len(nums)):
            self.n.append(self.n[index] + nums[index])
        #print(self.n)
    def sumRange(self, i: int, j: int) -> int:
        return self.n[j+1] - self.n[i]