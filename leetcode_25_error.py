def my_print(out):
    while out != None:
        print out.val
        out = out.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 到k为止，前面的反转，后面的不变
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head

        x = 0
        go = head
        while go != None:
            x += 1
            go = go.next
        if x < k:
            return head

        i = 0
        if head == None:
            return None

        before = head
        temp = head.next
        while i < k - 1 and temp != None:
            now = temp
            temp = now.next
            now.next = before
            before = now
            i += 1
        head.next = temp

        return before


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

so = Solution()

my_print(so.reverseKGroup(None, 2))
