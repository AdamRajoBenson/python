v=input()
b=0
c=0
for i in v:
  if(i.isnumeric()):
    b=b+1
  elif(i.isalpha()):
    c=c+1
if(b>1 and c>1):
  print("yes")
else:
  print("no")
