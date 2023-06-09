n=int(input())
for i in range(n):
    m=input()
    c=0
    for i in m:
        if i in '1234567890':
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes") 