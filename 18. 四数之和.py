def fourSum(nums, target):
    nums = sorted(nums)
    print(nums)
    nums_l = len(nums)
    result = []
    if nums_l == 4 and sum(nums) == target:
        return nums
    for left in range(nums_l - 2):
        if left > 0 and nums[left] == nums[left -1]:
            continue
        for first in range(left + 1,nums_l - 1):

            if first - 1 >left and  nums[first] == nums[first - 1]:
                continue
            third = nums_l - 1
            fixed = nums[left] + nums[first]
            second = first + 1

            while second < third:
                comp_num = fixed +  nums[second] + nums[third]

                if second > first + 1 and nums[second] == nums[second -1]:
                    second += 1
                    continue
                if comp_num > target:
                    third -= 1
                    continue

                elif comp_num == target:
                    result.append([nums[left], nums[first], nums[second], nums[third]])
                    third -= 1
                second += 1
    return result