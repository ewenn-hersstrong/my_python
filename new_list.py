from math import sqrt
L = [2, 4, 9, 16, 25]

L1 = []
for i in range(len(L)):
    L1.insert(i,sqrt(L[i]))

L2 = []
L2 = list(map(lambda x: sqrt(x), L))

L3 = []
L3 = [sqrt(L[i]) for i in range(len(L))]
print('',L1,'\n',L2,'\n',L3)
