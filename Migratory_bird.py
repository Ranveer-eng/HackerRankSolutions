def migratory(arr):
    name = []
    cnt = []
    for i in arr:
        if i not in cnt:
            cnt.append(i)
            x = arr.count(i)
            name.append([x,i])
    print(name)
    name.sort()
    maximum = name[-1][0]
    new = []
    for j in name:
        if j[0]==maximum:
            new.append(j)
    new.sort()
    return new[0][1]

print(migratory([1,1,2,2,3]))
print(migratory([1,2,3,4,5,4,3,2,1,3,4]))
