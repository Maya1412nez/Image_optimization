f = 1
for i in range(3):
    for j in range(5):
        print(i, j)
        if i == 2 and j == 4:
            f = 0
        if f == 0:
            break