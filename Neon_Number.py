n=int(input())
s=n*n
d=n
a=0
while s:
    a=a+s%10
    s=s//10
if a==d:
    print("Neon Number")
else:
    print("Not Neon Number")