#Python Program to Find Armstrong Number in an Interval
c=0
for i in range(10,100):
    for j in range(1,i+1):
        c=c+(j%10)**3
        print(c)
        j=j//10



