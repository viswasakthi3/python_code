

#reverse

a=789
b=0
while(a>0):
    b = (b * 10) +(a%10)
    a=a//10
#print(b)    



a = "how are you are"
word = a.split(' ')
joins =numpy.unique(word)
print(joins)
ab =' '.join(reversed(joins))
print(ab)








#factorial
e=5
v=1
for i in range(1,e+1):
    v=v*i
    
print(v)    


a= 0
if a % 2 ==0:
    print("odd")
elif a%3==0:
    print("e")   


   #pallindrome
     
s="malayalm"
if s == s[::-1]:
    print("yes")
else:
    print("f")     