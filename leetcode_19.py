# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1

        getl = head
        while getl.next != None:
            length += 1
            getl = getl.next

        fun = length - n

        before = None
        temp = head
        for x in xrange(fun):
            before = temp
            temp = temp.next

        if before != None:
            before.next = temp.next
            return head
        else:
            return head.next


test1 = ListNode(1)
test2 = ListNode(2)
test3 = ListNode(3)
test4 = ListNode(4)
test5 = ListNode(5)
test1.next = test2
test2.next = test3
test3.next = test4
test4.next = test5

so = Solution()

print so.removeNthFromEnd(test1, 2)
