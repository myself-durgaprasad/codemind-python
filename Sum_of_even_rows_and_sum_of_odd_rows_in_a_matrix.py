r,c=map(int,input().split())
e=0
o=0
for i in range(r):
    if i%2==0:
        l=list(map(int,input().split()))
        e+=sum(l)
    if i%2!=0:
        l=list(map(int,input().split()))
        o+=sum(l)
print(e,o)