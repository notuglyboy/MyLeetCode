class stack(object):
    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def top(self):
        if self.s:
            return self.s[-1]
        else:
            return ''

    def push(self,value):
        if value:
            self.s.append(value)

    def isempty(self):
        return len(self.s) == 0

    def stackprint(self):
            print(self.s)

priority_dict = {
    '': 0,
    '*':2,
    '/':2,
    '+':1,
    '-':1,
}
s1 = stack()
s2 = stack()
def cal(str1):

    now_op = ''
    i = 0
    # while i < len(str1):
    for s in str1:
        # s = str1[i]
        print(s, now_op)
        print(s2.s)
        print(s1.s)
        if s.isdigit():
            s1.push(s)
            s2.push(now_op)

        elif s == '(':
            s2.push(now_op)
            s2.push(s)
            now_op = ''
        elif s == ')':
            while s2.top() != '(':
                t = s2.pop()
                s1.push(t)
            s2.pop()
            now_op = s2.top() if s2.top() != '(' else ''
        else:
            if priority_dict[s] < priority_dict[now_op]:
                while not s2.isempty() and priority_dict[s2.top()] >= priority_dict[s]:
                    s1.push(s2.pop())

            elif priority_dict[s] == priority_dict[now_op]:
                if not s2.isempty():
                    s1.push(s2.pop())

            now_op = s
        i += 1

    #s2.stackprint()
    while not s2.isempty():
        t = s2.pop()
        s1.push(t)


def decode(stack1):
    result = stack()
    cal1 = 0
    for i in stack1:
        print(i)
        if i.isdigit():
            # pass
            result.push(i)
        else:
            print('is not di')
            r = float(result.pop())
            l = float(result.pop())
            if i == '+':
                t = l + r
            if i == '-':
                t = l - r
            if i == '*':
                t = l * r
            if i == '/':
                t = l / r
            result.push(t)
        result.stackprint()
    return result.top()

cal("(9-5)+2")
s1.stackprint()