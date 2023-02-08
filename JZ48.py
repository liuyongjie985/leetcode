#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # write code here
        d_dict = {}
        max_length = 0
        record_index = 0
        for x in s:
            if x in d_dict:
                max_length = max(max_length, len(d_dict))
                new_dict = {}
                for k in d_dict:
                    if d_dict[k] > d_dict[x]:
                        new_dict[k] = d_dict[k]
                new_dict[x] = record_index
                d_dict = new_dict
            else:
                d_dict[x] = record_index

            record_index += 1
        return max(max_length, len(d_dict))


so = Solution()
print(so.lengthOfLongestSubstring("abcabcbb"))
