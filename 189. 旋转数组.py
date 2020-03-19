def rotate(nums, k):
    start = 0
    end = len(nums) -1
    m = k % len(nums)
    reverse(nums, 0, end)
    reverse(nums, 0, m-1)
    reverse(nums, m,end)

def reverse(nums, s, e):
    print(s, e)
    while s < e:

        tmp = nums[s]
        nums[s] = nums[e]
        nums[e] = tmp
        s += 1
        e -= 1

nums = [1,2]
#reverse(nums, 0 ,6)
rotate(nums, 2) # [3,4,5,6,7, 1,2]
print(nums)