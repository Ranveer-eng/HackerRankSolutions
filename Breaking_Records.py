
n = int(input())
scores = [int(x) for x in input().split(" ",n)]

highest = []
lowest = []

def breakingRecords(scores):
    highest.append(scores[0])
    lowest.append(scores[0])
    for x in scores:
        if (x not in highest) and (x > highest[-1]):
            highest.append(x)
        if (x not in lowest) and (x < lowest[-1]):
            lowest.append(x)
        a = len(highest) - 1
        b = len(lowest) - 1
    print(a,b)

breakingRecords(scores)
