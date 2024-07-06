list  = [1, 2, 4, 6, 10, 11, 15, 16, 20, 22, 26]


search = 1

a = 0
b = len(list) - 1

while (a <= b):
    k = int((a+b) / 2)

    if (list[k] == search):
        print(f"found, at index: {k}")
        break

    if(list[k] < search):
        a = k + 1

    else:
        b = k - 1