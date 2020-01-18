
new = []
def add(x,n):
    a = x**n
    new.append(a)
    x = x -1
    if x != 0:
        add(x,n)
    return a

x = 10
n = 2
add(x,n)


for i in new:
    for j in new:
        if i + j == x:
            print(i,j)




        
        
        



