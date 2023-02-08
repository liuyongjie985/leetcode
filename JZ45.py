#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return string字符串
#
class Solution:
    def PrintMinNumber(self, numbers) -> str:

        # write code here
        l = self.quicksort(numbers)
        s = ""
        for x in l:
            s += str(x)
        return s

    def quicksort(self, l):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        front = []
        middle = []
        behind = []
        for x in l:
            if self.compare(x, l[mid]) == "less":
                front.append(x)
            else:
                if self.compare(x, l[mid]) == "more":
                    behind.append(x)
                else:
                    middle.append(x)

        return self.quicksort(front) + middle + self.quicksort(behind)

    def compare(self, a, b):
        if int(str(a) + str(b)) < int(str(b) + str(a)):
            return "less"
        else:
            if int(str(a) + str(b)) == int(str(b) + str(a)):
                return "equal"
            else:
                return "more"


so = Solution()
print(so.PrintMinNumber([3, 32, 321]))
