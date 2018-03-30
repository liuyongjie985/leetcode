# Definition for singly-linked list.

def my_print(out):
    while out != None:
        print out.val
        out = out.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        my_re = None
        num_list = []

        for x in lists:
            temp = x
            num_list.append(temp)

        while 1:
            if self.isOK(num_list):
                break;

            my_min = None
            i = 0
            x = 0
            while x < len(num_list):
                if num_list[x] == None:
                    num_list.remove(num_list[x])
                    if len(num_list) == 0:
                        break;
                    continue
                if my_min == None:
                    my_min = num_list[x]
                    i = x
                else:
                    if num_list[x].val < my_min.val:
                        my_min = num_list[x]
                        i = x
                x += 1
            if len(num_list) != 0:
                if my_re == None:
                    my_re = num_list[i]
                    head = num_list[i]

                else:
                    my_re.next = num_list[i]
                    my_re = my_re.next
                num_list[i] = num_list[i].next
        return head

    def isOK(self, list):
        re = True
        for x in list:
            if x != None:
                re = False
                break;
        return re


test = []

node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node6 = ListNode(6)

node7 = ListNode(2)
node8 = ListNode(3)
# node9 = ListNode(4)
# node10 = ListNode(5)
# node11 = ListNode(7)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6

node7.next = node8
# node8.next = node9
# node9.next = node10
# node10.next = node11

test.append(node1)
test.append(node7)

so = Solution()
my_print(so.mergeKLists(test))
