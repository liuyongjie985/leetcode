# coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        origin = head
        end = None
        i = 1
        front = None
        while head != None:
            if i == m:
                dummy = front
                end = head
            if i > m and i < n:
                temp = head.next
                head.next = front
                front = head
                head = temp
                i += 1
                continue

            if i == n:
                temp = head.next
                head.next = front
                end.next = temp
                if dummy == None:
                    begin = head
                    print begin
                    return begin

                else:
                    dummy.next = head
                    print origin
                    return origin

                break;
            i += 1
            front = head
            head = head.next
            print "第" + str(i) + "个"


def myprint(head):
    while head != None:
        print head.val
        head = head.next


h = ListNode(1)
origin = h
h.next = ListNode(2)
h = h.next
h.next = ListNode(3)
h = h.next
h.next = ListNode(4)
myprint(origin)
so = Solution()
re = so.reverseBetween(origin, 1, 4)
myprint(re)
