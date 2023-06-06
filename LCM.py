a,b=map(int,input().split())
for i in range(2,a**b):
    if i%a==0 and i%b==0:
        print(i)
        break
else:
    print("1")