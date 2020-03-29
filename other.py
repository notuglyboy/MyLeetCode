def binaryfind(target):
    d = [1,3,4,6,9,13,45,77]
    start = 0
    end = len(d) -1
    while start <= end:
        mid = int((start + end) / 2)

        if d[mid] > target:
            end = mid-1
        elif d[mid] < target:
            start= mid+1
        else:
            return True
    return False




def test(target):
    d = [1,3,4,6,9,13,45]
    start = 0
    end = len(d) -1
    while start <= end:
        mid = int((start + end) / 2)
        if d[mid] > target:
            end = mid-1
        elif d[mid] < target:
            start= mid+1

    return end+1

import random
def verfi():
    nums = []
    
    len_n = random.randint(1,100)
    for i in range(len_n):
        nums.append(random.randint(0, 1000))
    quicksort(nums, 0, len(nums) -1)
    last = nums[0]
    for i in nums[1:]:
        if i< last:
            return False
        last = i
    return True

def exchange(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

def quicksort(nums, start, end):
    if start >= end:
        return

    flag = nums[end]
    index = start
    i = start
    j = end -1 
    while i <= j:
        if flag > nums[index]:
            i+= 1
            index += 1
        else:
            exchange(nums, i, j)
            j-=1
    exchange(nums, i, end)

    quicksort(nums, start, i-1)
    quicksort(nums, i+1, end)

def quicksort2(nums, start, end):
    if start >= end:
        return
    flag = nums[end]
    index = start
    i = start
    while index < end:
        if flag > nums[index]:
            exchange(nums, i, index)
            i += 1
        index += 1
    exchange(nums, i, end)
    quicksort(nums, start, i - 1)
    quicksort(nums, i + 1, end)

def quicksort_with_stack(nums, start1, end1):
    stack = [(start1, end1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        flag = nums[end]
        index = start
        i = start
        while index < end:
            if flag > nums[index]:
                exchange(nums, i, index)
                i += 1
            index += 1
        exchange(nums, i, end)
        stack.append((start, i - 1))
        stack.append((i + 1, end))
    print(nums)

def binary():
    nums = [True, False]
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = int((start + end) / 2)
        if not nums[mid]:
            end = mid
        else:
            start = mid + 1

    return start


def fun(n):
    start = 0
    end = n
    while start <= end:
        mid = int((start + end) / 2)
        if mid * mid > n:
            end = mid - 1
        elif mid * mid < n:
            start = mid + 1
        else:
            return True
    return False



d = fun(64)
print(d)

