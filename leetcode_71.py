class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        now = ['/']

        item_list = path.split("/")

        for index, x in enumerate(item_list):
            x.replace('/', "")
            if x == '.' or x == '':
                continue
            if x == '..':
                if len(now) > 1:
                    now.pop(-1)
                    now.pop(-1)
                continue

            now.append(x)

            now.append('/')
        if len(now) > 1:
            now.pop(-1)
        result = ""
        for x in now:
            result += x
        return result


so = Solution()
print so.simplifyPath("/a/./b/../../c/")

print so.simplifyPath("/home/")

print so.simplifyPath("/home//foo/")

print so.simplifyPath("/..//../../ab/")
print so.simplifyPath("/")