class ListNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Mytree:
    def __init__(self, n):
        self.root = None
        self.min = None
        self.max = n
        self.len = 0


    def insert(self, x):
        print(x, self.len, self.min)
        if not self.root:
            self.root = ListNode(x)
            self.min = x
            self.len += 1
            return

        if self.len < self.max:
            tmp = self.root
            while tmp:
                if x < tmp.val:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = ListNode(x)
                        self.min = x
                        break
                else:
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = ListNode(x)
                        break
            self.len += 1

        elif x > self.min:
            tmp = self.root
            while tmp:
                if x < tmp.val:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = ListNode(x)
                        break
                else:
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = ListNode(x)
                        break

            t = self.root
            last = None
            while t.left:
                last = t
                t = t.left

            if last:
                last.left = None
                self.min = last.val

            if t == self.root:
                self.root = t.right
                self.min = t.right.val

    def frontprintStack(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)

def thirdMax(nums):
    t = Mytree(4)
    for n in nums:
        t.insert(n)
    t.frontprintStack()
    print(t.min)


thirdMax([7,5,9,36,1,4,8,10])