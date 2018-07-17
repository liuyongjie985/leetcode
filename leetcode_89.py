class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        else:
            if n == 1:
                return [0, 1]
            result = [0, 1]
            for x in xrange(n - 1):
                new_result = []
                for x in result:
                    temp = "0"
                    temp += str(x)
                    new_result.append(temp)
                for x in result[::-1]:
                    temp = "1"
                    temp += str(x)
                    new_result.append(temp)
                result = new_result

            print result
            re = []
            for x in result:
                re.append(self.TenToBinary(x))
            return re

    def TenToBinary(self, num):
        num = int(num)
        sum = num % 10
        num /= 10
        c = 1
        while num > 0:
            add = 1
            for x in xrange(c):
                add *= 2
            sum += (num % 10) * add
            num = num / 10
            c += 1

        return sum


so = Solution()
print so.TenToBinary(1000)
