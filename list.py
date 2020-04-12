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
    return head, tail

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

def getIntersectionNode(headA: ListNode, headB: ListNode):
    if not headA or not headB:
        return None
    l1 = headA
    l2 = headB
    l1_flag = False
    l2_flag = False

    while l1 and l2:
        if l1 == l2 and l1 != None:
            return l1.val 

        if not l1_flag and not l1.next:
            l1 = headB
            l1_flag = True
        else:
            l1 = l1.next


        if not l2_flag and not l2.next:
            l2_flag = True
            l2 = headA   
        else:
            l2 = l2.next
    return None

def getIntersectionNode1(headA: ListNode, headB: ListNode):
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA 

def revergeList(head):

    tmp = head
    old_n = tmp.next
    tmp.next = None
    while old_n:
        new_n = old_n.next
        old_n.next = tmp
        tmp = old_n
        old_n = new_n
    return tmp

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_index = l1
    l2_index = l2
    jin = 0
    head = None
    result_index = None
    while l1_index or l2_index or jin :
        l1_num = l1_index.val if l1_index else 0
        l2_num = l2_index.val if l2_index else 0
        tmp = l1_num + l2_num + jin
        jin = 1 if tmp >= 10 else 0
        r = tmp % 10
        #print(tmp, jin, r)
        if not result_index:
            result_index = ListNode(r)
            head = result_index
        else:
            result_index.next = ListNode(r)
            result_index = result_index.next
        if l1_index:
            l1_index = l1_index.next
        if l2_index:
            l2_index = l2_index.next
    return head



l1, _ = buildlist([9,9,9,9])
l2, _ = buildlist([1])
n=addTwoNumbers(l1, l2)
printlist(n)
#printlist(l2)