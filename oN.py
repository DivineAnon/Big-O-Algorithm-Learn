num = 10

def addOnesToTestList(num):
    testList = []
    for i in range(0, num):
        testList.append("x")
        print(testList)
    return testList

print("O(n): ", "\n")
addOnesToTestList(num)
print("\n")