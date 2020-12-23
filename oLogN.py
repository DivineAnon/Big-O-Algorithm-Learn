num = 10

def divide(num):
    while  num > 1:
        num /= 2
        print(num)
    return num

print("\n","O(log n): ", divide(num), "\n")