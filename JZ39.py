
3 45 6
class Solution:
    def MoreThanHalfNum_Solution(self, numbers) -> int:
        # write code here
        target = int(len(numbers) / 2)
        return self.ABC(numbers, 0, len(numbers) - 1, target)

    def ABC(self, numbers, start, end, k):
        index = start
        start += 1
        origin_end = end
        while start <= end:
            temp = int((start + end) / 2)
            if numbers[temp] < numbers[index]:
                c = numbers[start]
                numbers[start] = numbers[temp]
                numbers[temp] = c
                start += 1
            else:
                c = numbers[end]
                numbers[end] = numbers[temp]
                numbers[temp] = c
                end -= 1

        temp = numbers[start - 1]
        numbers[start - 1] = numbers[index]
        numbers[index] = temp
        if start - 1 == k:
            return numbers[start - 1]
        else:
            if start - 1 < k:
                return self.ABC(numbers, start, origin_end, k)
            else:
                return self.ABC(numbers, index, start - 2, k)


so = Solution()
print(so.MoreThanHalfNum_Solution([9]))
