
def guess(n):
    f = 6
    if n> f:
        return -1
    elif n < f:
        return 1
    else:
        return 0

def guessNumber(n: int) -> int:
    start = 1
    end = n
    while start <= end:
        mid = int((start + end) / 2)
        print(mid)
        if guess(mid) == -1:
            end = mid - 1 
        elif  guess(mid) == 1:
            start = mid + 1
        else:
            return mid

f = guessNumber(10)
print(f)