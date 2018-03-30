# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_a = []
        while True:
            list_a.append(l1.val)
            if l1.next == None:
                break;
            else:
                l1 = l1.next

        list_b = []
        while True:
            list_b.append(l2.val)
            if l2.next == None:
                break;
            else:
                l2 = l2.next

        list_a.reverse()
        list_b.reverse()

        l1 = len(list_a)
        l2 = len(list_b)
        if l1 > l2:
            for x in xrange(l1 - l2):
                list_b = [0] + list_b
        else:
            for x in xrange(l2 - l1):
                list_a = [0] + list_a

        c = [list_a[i] + list_b[i] for i in range(min(len(list_a), len(list_b)))]

        for x in list(xrange(len(c)))[::-1]:
            i = 0

            # sign = True
            # i = 0
            # while sign == True:
                # if c[x - i] >= 10:
                #     c[x - i] = c[x - i] % 10
                #     if x - i == 0:
                #         c.reverse()
                #         p = c + [1]
                #         c = p
                #         c.reverse()
                #     else:
                #         c[x - 1 - i] += 1
                #         if c[x - 1 - i] < 10:
                #             sign = False
                #         i += 1
                # else:
                #     sign = False
            if c[x - i] >= 10:
                c[x - i] = c[x - i] % 10
                if x - i == 0:
                    c.reverse()
                    p = c + [1]
                    c = p
                    c.reverse()
                else:
                    c[x - 1 - i] += 1


        re = ListNode(c[0])
        re.next = None
        before = re

        c.remove(c[0])

        for x in c:
            re = ListNode(x)

            re.next = before
            before = re

        return re


a1 = ListNode(9)

next = ListNode(9)
next.next = a1

# a1 = ListNode(2)
# a1.next = next

a2 = ListNode(9)

next2 = ListNode(9)
next2.next = a2
#
# a2 = ListNode(5)
# a2.next = next

# a1 = ListNode(5)
# a1.next = None
#
# a2 = ListNode(5)
# a2.next = None

al = Solution()
re = al.addTwoNumbers(next, next2)
print re
