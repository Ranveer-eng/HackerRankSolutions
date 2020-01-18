n = int(input())
s = [int(x) for x in input().split(" ",n)]
date = [int(x) for x in input().split(" ",2)]

d, m = date[0], date[1]

for z in s:
    if s.count(z) >1:
        s.remove(z)

def birthday(s,d,m):
    cout = 0
    for i in range(len(s) - m + 1):
        stattNum = 0
        su = 0
        for j in range(m):
           su += s[stattNum]
           stattNum += 1
           if (d == su):
               cout += 1
    return cout

print(birthday(s,d,m))

