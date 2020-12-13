def myAtoi(s):
    MAX = 2147483648
    answer = 0
    sign = 1
    start_flag = 0
    valid = {str(i) for i in range(10)}
    for i in range(len(s)):
        c = s[i]
        if c == " " and start_flag== 0:
            continue
        elif start_flag == 0:
            start_flag = 1
            if c == "-":
                sign = -1
                continue
            elif c == "+":
                sign = 1
                continue

        if start_flag == 1 and c not in valid:
            break
        elif c in valid:
            answer = answer* 10 + int(c)
    print(sign, answer)
    if sign == 1 and answer >= MAX:
        return MAX - 1
    if sign == -1 and answer > MAX:
        return -MAX
    return sign * answer