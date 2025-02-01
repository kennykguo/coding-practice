list = [5, 6, 4, 3, 2, 1]

for i in range(len(list)):
    for j in range(len(list) -  1):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print(len(list))
print(list)