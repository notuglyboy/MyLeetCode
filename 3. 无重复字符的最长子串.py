def test(str1):
    if not str1:
        return 0
    start = 0
    max_len = 0
    str_max =0
    hash_list = [None for i in range(128)]
    for index, s in enumerate(str1):
        if hash_list[ord(s)] != None:
            max_len = max(str_max, max_len)
            start = max(hash_list[ord(s)] + 1, start)
            str_max = index - start + 1
        else:
            str_max+=1
        hash_list[ord(s)] = index

    max_len = max(str_max, max_len)
    return max_len