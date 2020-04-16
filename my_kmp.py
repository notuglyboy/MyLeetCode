def kmp_next(patterm):
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
                index = next_arr[index]
                continue
            if index == 0:
                i+=1
                next_arr.append(0)
                continue

    return next_arr


def kmp_search(o_str, patterm, next_arr):
    o_index = 0
    p_index = 0
    while o_index < len(o_str):
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
            return o_index - len(next_arr)
    return -1


o="abcabcbb"
p="baar"
n = kmp_next(p)
#r = kmp_search(o,p,n)
#r =strStr(o, p)
print(n)