class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) <= 0:
            return 0
        set = {}
        max_length = 0
        left = 0
        right = 0
        max_right = -1
        max_left = -1
        while right < len(s):
            if set.has_key(s[right]):

                if max_length < right - left:
                    max_length = right - left;
                    max_right = right
                    max_left = left

                while s[left] != s[right]:
                    set.pop(s[left]);
                    left += 1

                left += 1

            else:

                set[s[right]] = 1

            right += 1
        # max_length = max(max_length, right - left)
        if max_length < right - left:
            max_length = right - left;
            max_right = right
            max_left = left
        return max_left, max_right, max_length;


so = Solution()
print so.lengthOfLongestSubstring("ADOBECODEBANC")
