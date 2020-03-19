def rotate(nums, k1):
    k =  k1 % len(nums)
    left = 0
    right = len(nums) - k
    print(left, k, right)
    for i in range(k):
        left_tmp = nums[left]
        right_tmp = nums[right]
        nums[right] = left_tmp
        nums[left] = right_tmp
        right +=1
        left += 1
        print(nums)
nums = [1,2, 3,4,5,6,7]
rotate(nums, 5) # [3,4,5,6,7, 1,2]
print(nums)