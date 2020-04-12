# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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