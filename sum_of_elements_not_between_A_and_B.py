n=int(input())
s=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in l:
    if i<a or i>b:
        s+=i
print(s)