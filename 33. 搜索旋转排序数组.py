def search(nums, target):
    left = 0
    right =len(nums) - 1
    while left <= right:
        mid = int((right + left) / 2)

        if nums[left] <= nums[mid]:
            if nums[mid] == target:
                return mid
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        elif nums[mid] < nums[right]:
            if nums[mid + 1] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid
        else:
            return mid if nums[mid] == target else -1
    return -1