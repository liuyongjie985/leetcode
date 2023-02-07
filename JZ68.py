# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # write code here
        if root == None:
            return None
        p_path, p_root = self.searchPath(root, p)
        if p_root == None:
            return None
        q_path, q_root = self.searchPath(root, q)
        if q_root == None:
            return None
        d_dict = {}
        for x in p_path:
            d_dict[x] = 1

        for x in q_path[::-1]:
            if x in d_dict:
                return x
        return None

    def searchPath(self, root, target_i):
        p_path = []
        p_root = root
        while p_root != None and p_root.val != target_i:
            p_path.append(p_root.val)
            if p_root.val < target_i:
                p_root = p_root.right
            else:
                p_root = p_root.left
        if p_root == None:
            return []
        p_path.append(p_root.val)
        return p_path, p_root
