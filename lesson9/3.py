lst = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
dict1 = {}
for x in lst:
    counter = 0
    if x in dict1:
        dict1[x] += 1
    else:
        dict1[x] = 1

print(dict1)
