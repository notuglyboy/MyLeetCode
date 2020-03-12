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

def cyclelist(head, n):
    tmp =head
    reentry = None
    i = 0
    while tmp:
        if i == n:
            reentry = tmp
        if not tmp.next:
            tmp.next = reentry
            break
        tmp = tmp.next
        i+=1

def hascycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow and fast:
        if not slow or not fast or not fast.next:
            return False
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

head = buildlist([1, 2])
cyclelist(head, -1)
f = hascycle(head)
print(f)