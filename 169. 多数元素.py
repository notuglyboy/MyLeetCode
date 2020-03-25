# 摩尔投票法
def majorityElement(nums):
    maj = nums[0]
    s = 1
    for n in nums[1:]:
        if s == 0:
            maj = n
        if n == maj:
            s+=1
        else:
            s-=1

    return maj


n = find_distributor_level([1,3,5,6], 2)
print(n)