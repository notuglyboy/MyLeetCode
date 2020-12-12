def divide(dividend: int, divisor: int):
    MAX = 2147483648
    fu = 0
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        fu = 1

    divisor = abs(divisor)
    dividend = abs(dividend)
    if dividend < divisor:
        return 0
    answer = 0
    bei = dividend
    chu = divisor
    yin = 1
    # print(bei, divisor)
    while bei >=  divisor:
        if chu <= bei:
            answer += yin
            bei -= chu
            chu = chu << 1
            yin =yin << 1
        else:
            chu = divisor
            yin = 1
        # print(bei, chu, answer)
    if fu == 1:
        if answer < -MAX:
            return MAX
        return -answer
    if answer >= MAX:
        return MAX -1
    return answer