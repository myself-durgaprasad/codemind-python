def c(n):
    if n<0:
        n=-1*n
    return len(str(n))


n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    print(c(l[i]),end=" ")
    