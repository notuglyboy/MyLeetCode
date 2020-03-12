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