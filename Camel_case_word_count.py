n=input()
s=0
for i in n:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        s+=1
    
if n[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(s)
else:
        print(s+1)