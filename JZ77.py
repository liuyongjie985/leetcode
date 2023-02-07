class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#
class Solution:
    def Print(self, pRoot: TreeNode):
        # write code here
        if pRoot == None:
            return []
        squeue = [pRoot]
        temp = []
        result = []
        temp_r = []
        while len(squeue) > 0 or len(temp) > 0:
            if len(squeue) == 0:
                squeue = temp
                temp = []
                result.append(temp_r)
                temp_r = []

            now = squeue.pop(0)
            temp_r.append(now.val)
            if now.left != None:
                temp.append(now.left)
            if now.right != None:
                temp.append(now.right)
        if len(temp_r) != 0:
            result.append(temp_r)

        for i, x in enumerate(result):
            if i % 2 == 1:
                result[i] = x[::-1]
        return result


