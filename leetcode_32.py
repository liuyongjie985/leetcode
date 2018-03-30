class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        stack.append(-1)
        max = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char == '(':
                stack.append(i)
                i += 1
                continue
            if char == ')':

                stack.pop(len(stack) - 1)
                if len(stack) == 0:
                    stack.append(i)
                now_top = stack[-1]
                length = i - now_top
                if length > max:
                    max = length



                i += 1
                continue
            i += 1
        return max

so = Solution()
# print so.longestValidParentheses("()(())")
# print so.longestValidParentheses("()(()")
# print so.longestValidParentheses("(()")
# print so.longestValidParentheses("(()(((()")
