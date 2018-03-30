class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_list = []

        mymax1 = 0
        mymap1 = {}

        mymax2 = 0
        mymap2 = {}

        for x in xrange(len(s)):
            str_list = []
            my_list.append(s[x])

            if x >= 1 and s[x] != s[x - 1]:
                idx = x + 1
                for y in list(xrange(len(my_list)))[::-1]:
                    if y == len(my_list) - 1:
                        str_list.append(s[x])
                        # if x == 0:
                        #     mymax = max(mymax, len(str_list))
                        #     mymap[mymax] = str_list
                        continue
                    else:
                        if idx < len(s):
                            if my_list[y] == s[idx]:
                                str_list.append(s[idx])
                            else:
                                break;
                            idx += 1
                        else:
                            break;
                mymax1 = max(mymax1, len(str_list))
                if not mymap1.has_key(mymax1):
                    mymap1[mymax1] = str_list
            else:
                if x < len(s) - 1 and s[x - 1] == s[x + 1]:
                    idx = x + 1
                    for y in list(xrange(len(my_list)))[::-1]:
                        if y == len(my_list) - 1:
                            str_list.append(s[x])
                            # if x == 0:
                            #     mymax = max(mymax, len(str_list))
                            #     mymap[mymax] = str_list
                            continue
                        else:
                            if idx < len(s):
                                if my_list[y] == s[idx]:
                                    str_list.append(s[idx])
                                else:
                                    break;
                                idx += 1
                            else:
                                break;
                    mymax1 = max(mymax1, len(str_list))
                    if not mymap1.has_key(mymax1):
                        mymap1[mymax1] = str_list


                else:
                    idx = x
                    for y in list(xrange(len(my_list)))[::-1]:
                        if y == len(my_list) - 1:
                            str_list.append(s[x])
                            # if x == 0:
                            #     mymax = max(mymax, len(str_list))
                            #     mymap[mymax] = str_list
                            continue
                        else:
                            if idx < len(s):
                                if my_list[y] == s[idx]:
                                    str_list.append(s[idx])
                                else:
                                    break;
                                idx += 1
                            else:
                                break;
                    mymax2 = max(mymax2, len(str_list))
                    if not mymap2.has_key(mymax2):
                        mymap2[mymax2] = str_list

        if mymax1 >= mymax2:

            re_list = mymap1[mymax1]
            re = re_list[1:]
            re.reverse()
            re = re + re_list

            return ''.join(re)
        else:
            return ''.join(mymap2[mymax2])


so = Solution()
print so.longestPalindrome('babad')
