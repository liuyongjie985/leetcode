# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        less_list = None
        large_list = None

        # origin = head

        before = None
        while head != None:
            if head.val < x:
                less_list = self.insert(less_list, head.val)
                head = self.pop(before, head)

                continue
            else:
                large_list = self.insert(large_list, head.val)
                before = head
            head = head.next

        move = less_list
        if move == None:
            if large_list != None:
                return large_list
            else:

                return move

        while move.next != None:
            move = move.next
        move.next = large_list

        return less_list

    def pop(self, before, head):

        if before == None:
            return head.next
        else:
            before.next = head.next
            return before.next

    def insert(self, less_list, my_value):
        move = less_list
        if move == None:
            less_list = ListNode(my_value)
        else:
            while move.next != None:
                move = move.next
            move.next = ListNode(my_value)
        return less_list


head = ListNode(1)
origin = head

# head = ListNode(1)
# origin = head
# head.next = ListNode(4)
# head = head.next
# head.next = ListNode(3)
# head = head.next
# head.next = ListNode(2)
# head = head.next
# head.next = ListNode(5)
# head = head.next
# head.next = ListNode(2)

so = Solution()
head = so.partition(origin, 0)


def myPrint(head):
    out = ""
    while head != None:
        out += str(head.val) + "\t"
        head = head.next
    print out


myPrint(head)
