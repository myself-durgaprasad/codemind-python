n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
a=[]
for i in l:
    a.append(sum(i))
print(max(a))