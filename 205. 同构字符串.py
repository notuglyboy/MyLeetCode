def isIsomorphic(s: str, t: str):
    replace = {}
    s_len = len(s)
    new_s = ''
    for i in range(s_len):

        if replace.get(s[i]):
            if t[i] != replace[s[i]]:
                return False
        else:
            replace[s[i]] = t[i]
        print(s[i], t[i], replace)

    if len(set(replace.values())) != len(replace):
        return False
    return True

p =isIsomorphic('ab', 'aa')
print(p)









