l=[]
for i in range(0,10):
  l.append(int(input()))
  if(l[i]>l[i-1]):
    a=l[i]
print(a)
