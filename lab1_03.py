sourceList = [1, 1, 2, 2, 3, 4, 5, 6, 5, 8, 7, 11, 3, 4, 5, 6, 2, 3, 1, 8, 6, 7, 5]
print(sourceList)


def removeDuplicates(list):
    tempList = []
    for i in list:
        if i not in tempList:
            tempList.append(i)

    return tempList


print (removeDuplicates(sourceList))
