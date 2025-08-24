s = "hello"

from collections import Counter

x = Counter(s)

print(x)

# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])

# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)


arr = [5, 4, 7, 3, 8]
arr.sort(reverse=True)
print(arr)


# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)