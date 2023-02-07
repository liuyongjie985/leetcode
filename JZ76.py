# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        # write code here
        o_h = pHead
        d_dict = {}
        while pHead != None:
            if pHead.val in d_dict:
                d_dict[pHead.val] += 1
            else:
                d_dict[pHead.val] = 1
            pHead = pHead.next
        pHead = o_h
        pre = None
        result = None
        while pHead != None:
            if d_dict[pHead.val] >= 2:
                if pre != None:
                    pre.next = pHead.next
            else:
                if pre != None:
                    pre.next = pHead
                else:
                    result = pHead
                pre = pHead
            pHead = pHead.next

        return result
