# coding:utf-8

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = list()
        temp = list()

        self.find(0, len(candidates), candidates, target, result, temp)

        return result

    def find(self, i, length, candidates, rest, result, temp):
        for x in xrange(i, length):
            if rest - candidates[x] == 0:
                temp.append(candidates[x])
                result.append(list(temp))
                temp.pop(-1)
                return True
            else:
                if rest - candidates[x] > 0:

                    temp.append(candidates[x])

                    if self.find(x, length,candidates, rest - candidates[x], result, temp) == False:
                        temp.remove(candidates[x])
                        continue
                    else:
                        temp.pop(-1)
                else:
                    return False
        return False


so = Solution()
print so.combinationSum([2, 3, 6, 7], 7)
