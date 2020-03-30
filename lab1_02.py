sourceList = []

for i in range(1, 101):
    sourceList.append(i)

a = slice(3, 100, 3)
print(sourceList[a])

reverseList = []

for i in reversed(sourceList):
    reverseList.append(i)

print(reverseList)

b = slice(-1, -100, -2)
print(sourceList[b])
