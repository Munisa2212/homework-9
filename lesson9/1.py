lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]
N = int(input("Son kiriting: "))
lst_big = []

for i in range(len(lst)//N):
    ind_start = i * N
    ind_end = ind_start + N
    lst_new = lst[ind_start:ind_end]
    lst_big.append(lst_new)
print(lst_big)
