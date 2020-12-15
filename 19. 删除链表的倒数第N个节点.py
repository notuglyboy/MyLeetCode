def removeNthFromEnd(head, n):
    tmp = head
    fast_index = 1
    slow_index = 1
    delete_node= head
    pre_delete = head
    while tmp:
        if fast_index > n:
            pre_delete = delete_node
            delete_node = delete_node.next
        fast_index += 1
        tmp = tmp.next
    if delete_node == head:
        head = delete_node.next
    else:
        pre_delete.next = delete_node.next
    return head