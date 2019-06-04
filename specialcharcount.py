a=input()
count=0
for i in a:
  if i.isalpha()!=True and i.isnumeric()!=True:
    count+=1
print (count)
