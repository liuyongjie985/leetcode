#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        # write code here
        target = n
        n = 0
        s = 0
        while target > s:
            n += 1
            s += self.getBit(n)
        last = target - (s - self.getBit(n))
        shang = last // n
        yu = last % n
        now = shang + 10 ** (n - 1) - 1
        if yu == 0:
            return str(now)[-1]
        else:
            return self.getResult(now, yu)

    def getBit(self, n):
        return n * 9 * 10 ** (n - 1)

    def getResult(self, now, yu):
        return str(now + 1)[yu - 1]


so = Solution()
print(so.findNthDigit(1))
