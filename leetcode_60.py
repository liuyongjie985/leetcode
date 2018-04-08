class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"

        my_list = []
        for x in xrange(n):
            my_list.append(x + 1)

        for x in xrange(k - 1):
            my_list = self.getNext(my_list)

        result = ""
        for x in my_list:
            result += str(x)
        return result

    def getNext(self, my_list):
        ok = []
        i = 2
        while i <= len(my_list):
            pre = my_list[:len(my_list) - i]
            sub_list = my_list[len(my_list) - i:]

            sub_list = self.nextPermutation(sub_list)

            if sub_list != []:
                ok = pre + sub_list
                break;
            i += 1

        return ok

    def nextPermutation(self, sub_str):
        i = len(sub_str) - 1
        while i >= 1:

            j = i - 1
            while j >= 0:
                if sub_str[j] < sub_str[i]:
                    temp = sub_str[j]
                    sub_str[j] = sub_str[i]
                    sub_str[i] = temp

                    pre = list(sub_str[:j + 1])
                    suffix = list(sub_str[j + 1:])
                    suffix.reverse()
                    return pre + suffix

                j -= 1
            i -= 1
        return []


so = Solution()
# print so.getPermutation(3, 2)
# print so.getPermutation(1, 1)
# print so.getPermutation(2, 1)

# 1,2,3
# 1,3,2
# 2,1,3
# 2,3,1
# 3,1,2
# 3,2,1

print so.getPermutation(9, 171669)
