def test(str1):
    if len(str1) <= 1:
        return str1
    max_len = 0
    return_left = 0
    return_right = 0
    for i, s in enumerate(str1[:-1]):

        max_tmp = 1
        left = i -1
        right = i + 1

        while left >= 0 and str1[left] == s:
            left -= 1
            max_tmp += 1

        while right <= len(str1) - 1 and str1[right] ==s :
            right += 1
            max_tmp += 1

        while left >= 0 and right <= len(str1) -1:
            if str1[left] == str1[right]:
                max_tmp += 2
                left -= 1
                right += 1
            else:
                break
        if max_tmp > max_len:
            return_left = left + 1
            return_right = right 
            max_len = max_tmp
    return str1[return_left: return_right]
