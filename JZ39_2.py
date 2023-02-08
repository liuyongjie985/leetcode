#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self, numbers) -> int:
        # write code here
        findnum = -1
        findtime = -1
        for x in numbers:
            if findnum == -1:
                findnum = x
                findtime = 1
            else:
                if findnum == x:
                    findnum = x
                    findtime += 1
                else:
                    findtime -= 1
                    if findtime == 0:
                        findnum = x
                        findtime = 1
        return findnum
