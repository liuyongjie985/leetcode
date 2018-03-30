class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        list = []
        list0 = ['']
        list1 = ['']
        list2 = ['a', 'b', 'c']
        list3 = ['d', 'e', 'f']
        list4 = ['g', 'h', 'i']
        list5 = ['j', 'k', 'l']
        list6 = ['m', 'n', 'o']
        list7 = ['p', 'q', 'r', 's']
        list8 = ['t', 'u', 'v']
        list9 = ['w', 'x', 'y', 'z']

        list.append(list0)
        list.append(list1)
        list.append(list2)
        list.append(list3)
        list.append(list4)
        list.append(list5)
        list.append(list6)
        list.append(list7)
        list.append(list8)
        list.append(list9)

        re = ['']
        for x in digits:
            num = int(x)
            new_re = []
            for z in re:
                for y in list[num]:
                    new_re.append(z+y)
            re = new_re
        return new_re


so = Solution()
print so.letterCombinations('23')