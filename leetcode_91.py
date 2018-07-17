# coding:utf-8
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        result = []
        for i, x, in enumerate(s):
            if i == 0:
                if x == "0":
                    return 0
                else:
                    result.append(1)
                    continue
            if i == 1:
                # "00" s[i] = 0
                if s[i - 1] == "0" and s[i] == "0":
                    result.append(0)
                    continue
                # 01-09 s[i] = s[i-1]
                if s[i - 1] == "0" and int(s[i]) >= 1 and int(s[i]) <= 9:
                    result.append(result[-1])
                    continue
                # 10 20 s[i] = s[i-2]
                if s[i] == '0':

                    if (s[i - 1] == "1" or s[i - 1] == "2"):
                        result.append(1)
                    else:
                        result.append(0)
                    continue

                # 11-19 21-26 s[i] = s[i-2]+s[i-1]
                if (s[i - 1] == "1" and int(s[i]) >= 1 and int(s[i]) <= 9) or (
                        s[i - 1] == "2" and int(s[i]) >= 1 and int(s[i]) <= 6):
                    result.append(2)
                    continue
                # 27-99
                result.append(result[-1])
                continue
            # "00" s[i] = 0
            if s[i - 1] == "0" and s[i] == "0":
                result.append(0)
                continue
            # 01-09 s[i] = s[i-1]
            if s[i - 1] == "0" and int(s[i]) >= 1 and int(s[i]) <= 9:
                result.append(result[-1])
                continue
            # 10 20 s[i] = s[i-2] 30-90 s[i]=0
            if s[i] == '0':
                if (s[i - 1] == "1" or s[i - 1] == "2"):
                    result.append(result[-2])
                else:
                    result.append(0)
                continue

            # 11-19 21-26 s[i] = s[i-2]+s[i-1]
            if (s[i - 1] == "1" and int(s[i]) >= 1 and int(s[i]) <= 9) or (
                    s[i - 1] == "2" and int(s[i]) >= 1 and int(s[i]) <= 6):
                result.append(result[-1] + result[-2])
                continue
            # 27-99 不包括整十数
            result.append(result[-1])

        return result[-1]


so = Solution()
print so.numDecodings("301")
