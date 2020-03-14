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