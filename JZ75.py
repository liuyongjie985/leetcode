# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.index = -1
        self.c = ""
        self.d_dict = {}

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        if self.index < len(self.c) and self.index != -1:
            return self.c[self.index]
        else:
            return "#"

    def Insert(self, char):
        # write code here
        self.c += char
        if char in self.d_dict:
            self.d_dict[char] += 1
            if char == self.c[self.index]:
                while self.index < len(self.c) and self.d_dict[self.c[self.index]] >= 2:
                    self.index += 1
                    continue
        else:
            self.d_dict[char] = 1
            if self.index == -1:
                self.index += 1


so = Solution()
so.Insert("a")
print(so.FirstAppearingOnce())
so.Insert("b")
print(so.FirstAppearingOnce())
so.Insert("c")
print(so.FirstAppearingOnce())
so.Insert("d")
print(so.FirstAppearingOnce())
so.Insert("e")
print(so.FirstAppearingOnce())
so.Insert("e")
print(so.FirstAppearingOnce())
