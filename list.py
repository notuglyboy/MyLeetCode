class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildlist(list):
    if not list:
        return None
    head = None
    tail = None
    for i in list:
        t = ListNode(i)
        if not head:
            head = t
            tail = t
        else:
            tail.next = t
            tail = t
    return head

def printlist(l):
    index = l
    while index:
        print(index.val)
        index = index.next

s = buildlist([1,4,5,7])
printlist(s)