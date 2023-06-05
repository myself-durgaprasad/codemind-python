r,c=map(int,input().split())
l=[]
a=[]
for i in range(r):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(c):
    s=0
    for j in range(r):
        s=s+l[j][i]
    a.append(s)
print(max(a))
    