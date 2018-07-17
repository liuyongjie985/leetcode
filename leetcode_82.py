# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        before = None
        now = head
        while now.next != None:
            if now.next.val == now.val:
                if before == None:
                    while now.next != None and now.next.val == now.val:
                        now = now.next
                    head = now.next
                else:
                    while now.next != None and now.next.val == now.val:
                        now = now.next
                    before.next = now.next

            before = now
            now = now.next
        return head
