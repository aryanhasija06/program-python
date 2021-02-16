import random
a=random.randint(10,30)
print(a,'is the number')
i=2
flag=0
for i in range(2,a//2):
    if a%i == 0:
        flag=0
        break
    else:
        flag=1

if flag==1:
    print(a,'is a prime number')  
else:
    print(a,'is not a prime number')
