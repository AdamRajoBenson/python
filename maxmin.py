a=int(input())
l=[]
for i in range(a):
   l.append(int(input())) 
l.sort(key=int) 
print(l[0],l[-1]) 
