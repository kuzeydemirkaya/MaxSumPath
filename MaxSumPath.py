triangle = """215
193 124
117 237 442
218 935 347 235
320 804 522 417 345
229 601 723 835 133 124
248 202 277 433 207 263 257
359 464 504 528 516 716 871 182
461 441 426 656 863 560 380 171 923
381 348 573 533 447 632 387 176 975 449
223 711 445 645 245 543 931 532 937 541 444
330 131 333 928 377 733 017 778 839 168 197 197
131 171 522 137 217 224 291 413 528 520 227 229 928
223 626 034 683 839 053 627 310 713 999 629 817 410 121
924 622 911 233 325 139 721 218 253 223 107 233 230 124 233"""

lines = triangle.split("\n")
text = ' '.join(lines)
numbers = list(map(int, (list(text.split(" ")))))

noprimelist = []
for s in numbers:
    if s > 1:
        for i in range(2, s):
            if (s % i) == 0:
                noprimelist.append(s)
                break
        else:
            noprimelist.append(0)
    elif s == 1:
        noprimelist.append(s)

rowamount1 = int((((8*(len(noprimelist)) + 1)** 0.5) - 1)//2)

rowlist = []
for a in range(rowamount1):
    b = a + 1
    x = (a*(a + 1))//2
    y = (b*(b +1))//2
    rowlist.append(noprimelist[x:y])

for t in range(len(rowlist)):
    if t == 0 and sum(rowlist[t]) == 0:
        del rowlist[0: len(rowlist)]
        rowlist.append([0])
        break
    if t > 0 and sum(rowlist[t]) == 0:
        del rowlist[t: (len(rowlist))]
        break
    else:
        pass
g = len(rowlist)-1

s = 0
nextrange = range(g-1, -1, -1)
for n in nextrange:
    while s <= n:
        if rowlist[n][s] != 0:
            if (rowlist[n+1][s] + rowlist[n+1][s+1]) > 0:
                rowlist[n][s] = max((rowlist[n][s] + rowlist[n+1][s]), (rowlist[n][s] + rowlist[n+1][s+1]))
            elif (rowlist[n+1][s] + rowlist[n+1][s+1]) == 0:
                rowlist[n][s] = 0
        s = s + 1
    s = 0
print("Maximum sum:", rowlist[0][0])
