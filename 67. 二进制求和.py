def addBinary(a: str, b: str) -> str:
    a_index = len(a) - 1
    b_index = len(b) - 1
    max_len = max(len(a), len(b))
    #result = '0' * max_len
    result = []
    jin = 0
    while a_index >= 0 or b_index >= 0 or jin:
        a_num = int(a[a_index]) if a_index >= 0 else 0
        b_num = int(b[b_index]) if b_index >= 0 else 0
        r = a_num + b_num + jin
        jin = 1 if r >= 2 else 0
        print(a_num, b_num,r, jin)
        result.append(str(r) if r < 2 else str(r - 2))
        #result[result_index] = str(r) if r < 2 else str(r - 2)
        a_index -= 1
        b_index -= 1
    if len(result) == 1:
        return result[0]
    result_str = ''.join(result[::-1]) if result[-1] == '1' else ''.join(result[-2:-1-len(result):-1])
    return result_str
