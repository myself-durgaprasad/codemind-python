n=input()
s=0
for i in n:
    if i in '1234567890':
        s=s+int(i)
        
print(s)