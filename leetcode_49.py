class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = dict()
        for x in strs:
            temp = str(x)
            temp = self.quickSort(temp)
            if result.has_key(temp):

                result[temp].append(x)
            else:
                result[temp] = [x]
        my_list = []
        for x in result.values():
            my_list.append(x)
        return my_list

    def quickSort(self, my_str):
        if len(my_str) <= 1:
            return my_str
        mid = my_str[len(my_str) / 2]

        left_list = ""
        mid_list = ""
        right_list = ""

        for x in my_str:
            if x < mid:
                left_list += x
            if x == mid:
                mid_list += x
            if x > mid:
                right_list += x
        return self.quickSort(left_list) + mid_list + self.quickSort(right_list)


so = Solution()
print so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
