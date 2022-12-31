a=5665
c=a
b=0
while(a>0):
    b=(a%10)+ (b*10)
    a=a//10
print(c,b)    
if c==b:
    print("f y")
else:
    print("f")    