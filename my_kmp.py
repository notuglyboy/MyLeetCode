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


o="ababcaababcaabc"
p="ababcaabc"
n = kmp_next(p)
r = kmp_search(o,p,n)
#r =strStr(o, p)
print(r)