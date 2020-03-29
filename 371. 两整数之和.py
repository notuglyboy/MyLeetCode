def getSum(a: int, b: int) -> int:
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    while b:
        carry = a & b
        a ^= b
        b = ((carry) << 1) & 0xFFFFFFFF
        # print((a, b))
    return a if a < 0x80000000 else ~(a^0xFFFFFFFF)



d = getSum(-12, -8)
print(d)