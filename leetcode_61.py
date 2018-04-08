# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        length, last = self.getLength(head)

        if length <= 1:
            return head

        if k > length:
            k = k % length
        if k == 0:
            return head
        index = length - k

        if index == 0:
            return head
        now = head
        for x in xrange(index - 1):
            now = now.next

        target = now.next
        now.next = None
        last.next = head
        return target

    def getLength(self, head):
        now = head
        length = 0
        before = None
        while now != None:
            before = now
            now = now.next
            length += 1
        return length, before


def my_print(head):
    while head != None:
        print head.val
        head = head.next


# 1->2->3->4->5->NULL and k = 2
# temp1 = ListNode(5)

# temp1.next = None
# temp2 = ListNode(4)
# temp2.val = 4
# temp2.next = temp1
# temp1 = ListNode(3)
# temp1.val = 3
# temp1.next = temp2
temp2 = ListNode(2)
temp2.val = 2
temp2.next = None
temp1 = ListNode(1)
temp1.val = 1
temp1.next = temp2

so = Solution()
my_print(so.rotateRight(temp1, 2))
