# coding:utf-8
def my_print(out):
    while out != None:
        print out.val
        out = out.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
        # x即为链表的长度

        num = x / k

        if head == None:
            return None

        head_list = []
        tail_list = []

        for p in xrange(num):
            head1, tail, head2 = self.reverseNode(head, k)


            head_list.append(head1)
            tail_list.append(tail)

            head = head2

        for p in xrange(len(head_list) - 1):
            tail_list[p].next = head_list[p + 1]

        return head_list[0]

    def reverseNode(self, head, k):
        before = head
        temp = head.next
        i = 0
        while i < k - 1 and temp != None:
            now = temp
            temp = now.next
            now.next = before
            before = now
            i += 1

        head.next = temp

        return before, head, temp


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

my_print(so.reverseKGroup(node1, 2))
