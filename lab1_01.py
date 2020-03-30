print ("Set room width: ")
width = input()
print ("Set room length: ")
length = input()
firstWallSign = '*'
secondWallSign = '|'

for i in range(0, int(width)):
    firstWallSign = firstWallSign + ' - '
    secondWallSign = secondWallSign + ' . '
firstWallSign = firstWallSign + '*'
secondWallSign = secondWallSign + '|'

print(firstWallSign)
for i in range(0, int(length)):
    print(secondWallSign)
print(firstWallSign)
