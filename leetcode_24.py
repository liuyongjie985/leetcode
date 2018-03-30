def my_print(out):
    while out != None:
        print out.val
        out = out.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        before = head
        now = head
        be_before = None
        first = True
        i = 0
        while now != None:
            temp = now.next
            if i % 2 == 1:
                before.next = now.next
                now.next = before
                temp2 = before
                before = before.next
                if be_before != None:
                    be_before.next = now

                be_before = temp2
                if first:
                    head = now
                    first = False
            now = temp
            i += 1
        return head


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

my_print(so.swapPairs(node1))
