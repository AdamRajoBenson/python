#swap using bitwise operator
l=int(input())
m=int(input())
l=l^m
m=l^m
l=l^m
print(l,m)
