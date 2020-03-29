def reverStr(s):
    if len(s) <= 1:
        return s
    yuan = ['a', 'e','i', 'o', 'u', 'A', 'E','I', 'O', 'U']
    left = 0
    right = len(s) -1
    l_flag = False
    r_flag = False
    re = list(s)
    while left<right:
        if not s[left] in yuan:
            left+=1
        elif not l_flag:
            l_flag = True

        if not s[right] in yuan:
            right -=1
        elif not r_flag:
            r_flag = True
        if l_flag and r_flag:
            re[right], re[left] = re[left], re[right]
            l_flag = False
            r_flag = False
            left +=1
            right -=1

    ss = ''.join(re)
    print(ss)