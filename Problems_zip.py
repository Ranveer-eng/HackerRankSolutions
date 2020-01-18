def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   print(n>=1)

pascal_triangle(5)



name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 

# using zip() to map values 
mapped = zip(name,roll_no,marks) 

# converting values to print as set 
mapped = set(mapped) 

# printing resultant values 
print ("The zipped result is : ",end="") 
print (mapped) 


# initializing list of players. 
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ] 
  
# initializing their scores 
scores = [100, 15, 17, 28, 43 ]

for i,j in zip(players,scores):
    print("player:",i,"         ","score:",j)
    
m = [[1,2],[2,3],[3,4],[4,5]]
# for l,m in m:
    # print(l,m)

a = [1,2,3,4,5]
b = [6,7,8,9,0]
for i,j in zip(a+b,b+a):
    print(i,j)






