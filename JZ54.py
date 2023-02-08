class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param proot TreeNode类
# @param k int整型
# @return int整型
#
class Solution:
    def KthNode(self, proot: TreeNode, k: int) -> int:
        # write code here
        if proot == None:
            return -1

        result = self.midorder(proot)
        if k <= 0 or k > len(result):
            return -1
        else:
            return result[k - 1]

    def midorder(self, t):
        step = t
        stack = []
        result = []
        while step != None or len(stack) > 0:
            if step != None:
                stack.append(step)
                step = step.left
            else:
                step = stack.pop(-1)
                result.append(step)
                step = step.right

        return result


t = TreeNode(1)

so = Solution()
print(so.KthNode(t, 1))
