user = [int(x) for x in input().split(" ",4)]

x1, v1, x2, v2 = user[0], user[1], user[2], user[3]
def kangaroo(x1,v1,x2,v2):
    if x1 < x2:
        a = True
        while a == True:
            x1 += v1
            x2 += v2
            if x1 == x2:
                print("YES")
                break
            if (x1 > x2) or (v1 < v2) or (v1==v2):
                a = False
        if x1 != x2:
            print("NO")
    elif(x1 > x2):
        a = True
        while a == True:
            x1 += v1
            x2 += v2
            if x1 == x2:
                print("YES")
                break
            if (x1 < x2) or (v1 > v2) or (v1==v2):
                a = False
        if x1 != x2:
            print("NO")

kangaroo(x1,v1,x2,v2)
