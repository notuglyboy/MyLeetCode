def strStr(self, o_str: str, patterm: str) -> int:
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