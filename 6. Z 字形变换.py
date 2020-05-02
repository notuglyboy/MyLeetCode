def convert(s: str, numRows: int) -> str:
    if numRows <= 1:
        return s
    index = 0
    result = ""
    step = 2 * numRows - 2
    for i in range(numRows, 0, -1):
        step_t = step
        # if i != numRows and i != 1:
        #     step_t =  step - 1
        
        print_index = numRows - i
        step_first = step_t - (numRows - i) * 2
        print(print_index, step_t, i, step_first)
        while print_index < len(s):
            print(step_first)
            result += s[print_index]
            if step_first <= 0:
                step_first = step_t
            print_index +=  step_first
            step_first = step_t - step_first

    return result