n=int(input())
se=0
so=0
l=list(map(int,input().split()))
for i in range(n):
    if i%2==0:
        se+=l[i]
    else:
        so+=l[i]
if se>so:
    print(se-so)
else:
    print(so-se)
        