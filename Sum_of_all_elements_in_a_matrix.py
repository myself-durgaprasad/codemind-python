r,c=map(int,input().split())
s=0
for i in range(r):
    l=list(map(int,input().split()))
    s=s+sum(l)
print(s)