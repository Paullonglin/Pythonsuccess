list = [1, 2, 3, 4]
listend = []
for bai in list:
    for shi in list:
        for ge in list:
            num = bai * 100 + shi * 10 + ge
            if (bai != shi) and (shi != ge) and (bai != ge):
                listend.append(num)
print(listend)
print(len(listend))
