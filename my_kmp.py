def kmp_next(patterm):
    next_arr = [0]
    # prefix_index处在字符串前缀，
    prefix_index = 0
    i = 1
    while i < len(patterm):
        if patterm[i] == patterm[prefix_index]:
            next_arr.append(prefix_index + 1)
            prefix_index += 1
            i +=1
        else:
            # 如果不相等，prefix_index回溯到它的上一个位置
            if prefix_index >= 1:
                prefix_index = next_arr[prefix_index - 1]
                continue
            
            # 如果prefix_index为0说明前缀和后缀没有相同的串
            if prefix_index == 0:
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


p="aabaac"
n = kmp_next(p)
#r = kmp_search(o,p,n)
#r =strStr(o, p)
print(n)