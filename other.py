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
        #print(index, i,patterm[index], patterm[i])
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

    #print(next_arr)
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

def convert(s: str, numRows: int) -> str:
    if numRows <= 1:
        return s
    index = 0
    result = ""
    step = 2 * numRows - 2
    for i in range(numRows, 0, -1):
        step_t = step
        print_index = numRows - i
        step_first = step_t - (numRows - i) * 2
        while print_index < len(s):
            result += s[print_index]
            if step_first <= 0:
                step_first = step_t
            print_index +=  step_first
            step_first = step_t - step_first

    return result

def judge(data, func):
    for d in data:
        f = func(d[0])
        if f != d[1]:
            print('error data {}, retuen {}'.format(d, f))
            return

def test222():
    for f,arg in zip(a, b):
        arg_str = [str(t) for t in arg]
        arg_str = ','.join(arg_str)
        st = 'lru.{}({})'.format(f, arg_str)
        print(st)

def myprint(func):
    def f(*arg, **kargs):
        r = func(*arg, **kargs)
        print(arg)
        print('arg is  fun result is {}'.format(r))
    return f

def printlist(l):
    index = l
    while index:
        print(index.key)
        index = index.next




class stack(object):
    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def top(self):
        return self.s[-1]

    def push(self,value):
        if value:
            self.s.append(value)

    def isempty(self):
        return len(self.s) == 0

    def stackprint(self):
        for i in self.s:
            print(i)

priority_dict = {
    '': 0,
    '*':2,
    '/':2,
    '+':1,
    '-':2,
}


s1 = stack()
s2 = stack()
def cal(str1):

    now_op = ''
    for s in str1:
        if s.isdigit():
            s1.push(s)
            s2.push(now_op)

        elif s == '(':
            s2.push(now_op)
            s2.push(s)
            now_op = ''
        elif s == ')':
            while s2.top() != '(':
                t = s2.pop()
                s1.push(t)
            s2.pop()
            if s2.top() != '(':
                s2.push(s2.pop())
            #s1.push(s2.pop())
            now_op = ''
        else:
            if priority_dict[s] > priority_dict[now_op]:
                now_op = s

    while not s2.isempty():
        t = s2.pop()
        s1.push(t)


cal('4+(5+6)*7*3+5/2')
s1.stackprint()



