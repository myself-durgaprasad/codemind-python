r,c=map(int,input().split())
e=0
o=0
for i in range(r):
    l=list(map(int,input().split()))
    for j in l:
        if j%2==0:
            e+=j
        else:
            o+=j
print(e,o)
