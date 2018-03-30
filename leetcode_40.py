# coding:utf-8

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = list()
        temp = list()

        candidates.sort()

        word = dict()

        new_candidates = list()

        for x in candidates:
            if not word.has_key(x):
                word[x] = 1
                new_candidates.append(x)
            else:
                word[x] += 1

        self.find(0, len(new_candidates), target, temp, result, new_candidates, word)

        return result

    def find(self, i, max, rest, temp, result, candidates, word):
        for x in xrange(i, max):
            if rest - candidates[x] == 0:
                temp.append(candidates[x])
                temp_dict = {}

                for y in temp:
                    if temp_dict.has_key(y):
                        temp_dict[y] += 1
                    else:
                        temp_dict[y] = 1

                add_sign = True
                for y in temp_dict.keys():
                    if temp_dict[y] > word[y]:
                        add_sign = False
                        break;
                if add_sign == True:
                    result.append(list(temp))
                temp.pop(-1)
                return True

            else:
                if rest - candidates[x] > 0:
                    temp.append(candidates[x])
                    self.find(x, max, rest - candidates[x], temp, result, candidates, word)
                    temp.pop(-1)
                else:
                    return False


so = Solution()
print so.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
