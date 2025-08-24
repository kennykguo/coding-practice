list  = [1, 2, 4, 6, 10, 11, 15, 16, 20, 22, 26]

k = 0

search = 16

n = len(list)

b = int(len(list) / 2)

while (b >= 1):
    while(k + b < n and list[k + b] <= search):
        k += b
    b = b//2

if (list[k] == search):
    print(f"found at index {k}")

