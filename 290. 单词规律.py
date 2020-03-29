def wordPattern(pattern, str):
    str_map = {}
    str_list = str.split()
    for p, s in zip(pattern, str_list):
        if str_map.get(p):
            if s != str_map[p]:
                return False
        else:
            str_map[p] = s

    if len(set(str_list)) != len(str_map) or len(pattern) != len(str_list):
        return False
    return True

d = wordPattern('aba', "cat cat cat dog")
print(d)