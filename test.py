def maxStipend(numOfDays, taskList):
    # WRITE YOUR CODE HERE
    return getMax(taskList)
    pass


def getMax(sub_list):
    if len(sub_list) == 0:
        return 0
    if len(sub_list) == 1:
        return sub_list[0][1]

    if len(sub_list) == 2:
        return max((sub_list[0][1] + sub_list[1][0]), sub_list[1][1])
    length = len(sub_list)

    return max(getMax(sub_list[:length - 1]) + sub_list[length - 1][0],
               getMax(sub_list[:length - 2]) + sub_list[length - 1][1])


print maxStipend(4, [[7, 10], [6, 7], [4, 6], [6, 7]])
