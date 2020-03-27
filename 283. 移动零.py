def exchange(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

def moveZeroes(nums):
    notzero = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            exchange(nums, i ,notzero)
            notzero += 1

    print(nums)

moveZeroes([1,5,0,0,1,0,3,12])