testList = [1, 43, 31, 21, 6, 96, 48, 13, 25, 5]

def bubbleSort(testList):
    for i in range(len(testList)):
        for j in range(i+1, len(testList)):
            if testList[j] < testList[i]:
                testList[j], testList[i] = testList[i], testList[j]
            print(testList)

print("O(n**2): ", "\n")
bubbleSort(testList)
print()