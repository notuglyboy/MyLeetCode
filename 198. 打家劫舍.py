def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    r = max(nums[:2])
    max1 = [nums[0],r]
    index = 2
    end = len(nums) - 1
    while  index <= end:
        t = max1[index -2] + nums[index]
        r = max(r, t)
        max1.append(r)
        index += 1
    return r
        
def rob1(nums):
    premax = 0
    currentmax = 0
    for i in nums:
        tmp = currentmax
        currentmax = max(premax + i, currentmax)
        premax = tmp
    return currentmax

f= rob1([1,1,6,103])
print(f)