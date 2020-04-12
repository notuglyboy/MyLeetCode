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


list1 = [1,3]
def find_index(n):
    start = 0
    end = len(list1) -1 
    while start <= end:
        #print(start)
        mid = int((start + end) / 2)
        if list1[mid] > n:
            end = mid - 1
        elif list1[mid] < n:
            start = mid + 1
        else:
            return mid
    return start


def kmp_next(patterm):
    next_arr = [0]
    index = 0
    i = 1
    while i < len(patterm):
        print(index, i,patterm[index], patterm[i])
        if patterm[i] == patterm[index]:
            next_arr.append(index + 1)
            index += 1
            i +=1
        else:
            if index >= 1:
                index = next_arr[index]
                continue
            if index == 0:
                i+=1
                next_arr.append(0)
                continue

    print(next_arr)
    return next_arr


def kmp_search(o_str, patterm, next_arr):
    o_index = 0
    p_index = 0
    while o_index < len(o_str):
        #print(o_index, p_index, o_str[o_index], patterm[p_index])
        if o_str[o_index] == patterm[p_index]:
            p_index += 1
            o_index += 1
        else:

            if p_index >= 1:
                p_index = next_arr[p_index-1]
                continue

            if p_index == -1 or p_index == 0:
                o_index +=1
                p_index = 0
                continue

        if p_index >= len(next_arr):
            #print(o_index, p_index)

            return o_index - len(next_arr)
    return -1

def strStr(o_str: str, patterm: str) -> int:
    if not patterm:
        return 0
    next_arr = [0]
    index = 0
    i = 1
    while i < len(patterm):
        if patterm[i] == patterm[index]:
            next_arr.append(index + 1)
            index += 1
            i +=1
        else:


            if index >= 1:
                index = next_arr[index-1]
                continue
            if index == 0:
                i+=1
                next_arr.append(0)
                continue
    o_index = 0
    p_index = 0
    #for i, s in enumerate(o_str):
    while o_index < len(o_str):
        #print(o_index, p_index, o_str[o_index], patterm[p_index])
        if o_str[o_index] == patterm[p_index]:
            p_index += 1
            o_index += 1
        else:

            if p_index >= 1:
                p_index = next_arr[p_index-1]
                continue

            if p_index == -1 or p_index == 0:
                o_index +=1
                p_index = 0
                continue

        if p_index >= len(next_arr):
            #print(o_index, p_index)

            return o_index - len(next_arr)
    return -1


# o="mississippi"
# p="sippi"
o="ababcaababcaabc"
p="ababcaabc"
n = kmp_next(p)
r = kmp_search(o,p,n)
#r =strStr(o, p)
print(r)

