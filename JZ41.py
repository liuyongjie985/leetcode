# -*- coding:utf-8 -*-

class MaxHeap(object):
    def __init__(self):
        self.save = []
        self.num = 0

    def insert(self, target, max=True):
        self.num += 1
        self.save.append(target)
        xiao_num = self.num
        while xiao_num > 1:
            if max:
                if self.save[xiao_num - 1] > self.save[xiao_num // 2 - 1]:
                    temp = self.save[xiao_num - 1]
                    self.save[xiao_num - 1] = self.save[xiao_num // 2 - 1]
                    self.save[xiao_num // 2 - 1] = temp
                    xiao_num = xiao_num // 2
                else:
                    break
            else:
                if self.save[xiao_num - 1] < self.save[xiao_num // 2 - 1]:
                    temp = self.save[xiao_num - 1]
                    self.save[xiao_num - 1] = self.save[xiao_num // 2 - 1]
                    self.save[xiao_num // 2 - 1] = temp
                    xiao_num = xiao_num // 2
                else:
                    break

    def downshirt(self, max=True):
        start = 1
        while start <= self.num // 2:
            if max:
                if start * 2 < self.num and self.save[start * 2 - 1] < self.save[start * 2]:
                    ex = start * 2
                else:
                    ex = start * 2 - 1

                if self.save[start - 1] < self.save[ex]:
                    temp = self.save[start - 1]
                    self.save[start - 1] = self.save[ex]
                    self.save[ex] = temp
                    start = ex + 1
                else:
                    break

            else:
                if start * 2 < self.num and self.save[start * 2 - 1] > self.save[start * 2]:
                    ex = start * 2
                else:
                    ex = start * 2 - 1

                if self.save[start - 1] > self.save[ex]:
                    temp = self.save[start - 1]
                    self.save[start - 1] = self.save[ex]
                    self.save[ex] = temp
                    start = ex + 1
                else:
                    break


class Solution:
    max_heap = MaxHeap()
    max_num = 0
    min_heap = MaxHeap()
    min_num = 0

    def Insert(self, num):
        # write code here
        if self.max_num > 0:
            # 放入小堆
            if self.max_num <= self.min_num:
                if num <= self.min_heap.save[0]:
                    self.max_heap.insert(num)
                else:
                    temp = self.min_heap.save[0]
                    self.min_heap.save[0] = num
                    self.min_heap.downshirt(False)
                    self.max_heap.insert(temp)
                self.max_num += 1
            else:
                # 给出最大元素给大堆
                if num >= self.max_heap.save[0]:
                    self.min_heap.insert(num, False)
                else:
                    temp = self.max_heap.save[0]
                    self.max_heap.save[0] = num
                    self.max_heap.downshirt()
                    self.min_heap.insert(temp, False)
                self.min_num += 1

        else:
            self.max_heap.insert(num)
            self.max_num += 1

    def GetMedian(self):
        # write code here
        if self.max_num == self.min_num:
            return (self.max_heap.save[0] + self.min_heap.save[0]) / 2
        else:
            return self.max_heap.save[0]


# -*- coding:utf-8 -*-

class Solution2:
    def __init__(self):
        self.minNums = []
        self.maxNums = []

    def maxHeapInsert(self, num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i - 1) // 2]:
                t = self.maxNums[(i - 1) // 2]
                self.maxNums[(i - 1) // 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) // 2
            else:
                break

    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def minHeapInsert(self, num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) // 2]:
                t = self.minNums[(i - 1) // 2]
                self.minNums[(i - 1) // 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) // 2
            else:
                break

    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def Insert(self, num):
        if (len(self.minNums) + len(self.maxNums)) & 1 == 0:
            if len(self.maxNums) > 0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums) > 0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)

    def GetMedian(self, n=None):
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen == 0:
            return -1
        if allLen & 1 == 1:
            return self.minNums[0]
        else:
            return (self.maxNums[0] + self.minNums[0] + 0.0) / 2


so = Solution()
so2 = Solution2()
a = [383, 886, 777, 915, 793, 335, 386, 492, 649, 421, 362, 27, 690, 59, 763, 926, 540, 426, 172, 736, 211, 368, 567,
     429, 782, 530, 862, 123, 67, 135, 929, 802, 22, 58, 69, 167, 393, 456, 11, 42, 229, 373, 421, 919, 784, 537, 198,
     324, 315, 370, 413, 526, 91, 980, 956, 873, 862, 170, 996, 281, 305, 925, 84, 327, 336, 505, 846, 729, 313, 857,
     124, 895, 582, 545, 814, 367, 434, 364, 43, 750, 87, 808, 276, 178, 788, 584, 403, 651, 754, 399, 932, 60, 676,
     368, 739, 12, 226, 586, 94, 539, 795, 570, 434, 378, 467, 601, 97, 902, 317, 492, 652, 756, 301, 280, 286, 441,
     865, 689, 444, 619, 440, 729, 31, 117, 97, 771, 481, 675, 709, 927, 567, 856, 497, 353, 586, 965, 306, 683, 219,
     624, 528, 871, 732, 829, 503, 19, 270, 368, 708, 715, 340, 149, 796, 723, 618, 245, 846, 451, 921, 555, 379, 488,
     764, 228, 841, 350, 193, 500, 34, 764, 124, 914, 987, 856, 743, 491, 227, 365, 859, 936, 432, 551, 437, 228, 275,
     407, 474, 121, 858, 395, 29, 237, 235, 793, 818, 428, 143, 11, 928, 529, 776, 404, 443, 763, 613, 538, 606, 840,
     904, 818, 128, 688, 369, 917, 917, 996, 324, 743, 470, 183, 490, 499, 772, 725, 644, 590, 505, 139, 954, 786, 669,
     82, 542, 464, 197, 507, 355, 804, 348, 611, 622, 828, 299, 343, 746, 568, 340, 422, 311, 810, 605, 801, 661, 730,
     878, 305, 320, 736, 444, 626, 522, 465, 708, 416, 282, 258, 924, 637, 62, 624, 600, 36, 452, 899, 379, 550, 468,
     71, 973, 131, 881, 930, 933, 894, 660, 163, 199, 981, 899, 996, 959, 773, 813, 668, 190, 95, 926, 466, 84, 340, 90,
     684, 376, 542, 936, 107, 445, 756, 179, 418, 887, 412, 348, 172, 659, 9, 336, 210, 342, 587, 206, 301, 713, 372,
     321, 255, 819, 599, 721, 904, 939, 811, 940, 667, 705, 228, 127, 150, 984, 658, 920, 224, 422, 269, 396, 81, 630,
     84, 292, 972, 672, 850, 625, 385, 222, 299, 640, 42, 898, 713, 298, 190, 524, 590, 209, 581, 819, 336, 732, 155,
     994, 4, 379, 769, 273, 776, 850, 255, 860, 142, 579, 884, 993, 205, 621, 567, 504, 613, 961, 754, 326, 259, 944,
     202, 202, 506, 784, 21, 842, 868, 528, 189, 872, 908, 958, 498, 36, 808, 753, 248, 303, 333, 133, 648, 890, 754,
     567, 746, 368, 529, 500, 46, 788, 797, 249, 990, 303, 33, 363, 497, 253, 892, 686, 125, 152, 996, 975, 188, 157,
     729, 436, 460, 414, 921, 460, 304, 28, 27, 50, 748, 556, 902, 794, 697, 699, 43, 39, 2, 428, 403, 500, 681, 647,
     538, 159, 151, 535, 134, 339, 692, 215, 127, 504, 629, 49, 964, 285, 429, 343, 335, 177, 900, 238, 971, 949, 289,
     367, 988, 292, 795, 743, 144, 829, 390, 682, 340, 541, 569, 826, 232, 261, 42, 360, 117, 23, 761, 81, 309, 190,
     425, 996, 367]
temp = []
for i, x in enumerate(a):
    if i == 33:
        print("debug")
    so.Insert(x)
    so2.Insert(x)
    m = so.GetMedian()
    n = so2.GetMedian()
    print(i, m, n)
