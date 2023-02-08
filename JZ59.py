#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self, num, size: int):
        # write code here
        if size == 0 or size > len(num):
            return []
        else:
            deque = []
            for x in range(size):
                while len(deque) > 0 and num[deque[-1]] <= num[x]:
                    deque.pop(-1)
                deque.append(x)

            result = []
            result.append(num[deque[0]])
            x = size
            while x < len(num):
                while len(deque) > 0 and num[deque[-1]] <= num[x]:
                    deque.pop(-1)
                deque.append(x)
                if deque[0] + size <= x:
                    deque.pop(0)
                result.append(num[deque[0]])
                x += 1
            return result


so = Solution()
print(so.maxInWindows([9, 10, 9, -7, -3, 8, 2, -6], 5))
