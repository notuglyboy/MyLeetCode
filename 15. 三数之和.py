def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    left = 0
    len1 = len(nums)
    result = []
    for first in range(len1):
        if first >= 1 and nums[first] == nums[first - 1]:
            continue
        third = len1 - 1
        for second in range(first + 1, len1):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while second < third and nums[first] + nums[second] > -nums[third]:
                third -= 1

            if second >= third:
                break
            if nums[first] + nums[second] + nums[third] == 0:
                result.append([nums[first],nums[second], nums[third]])
    return result