#This program will create a series of prime number

max=int(input("Enter maximum limit: "))
for a in range(2,max+1):
    count=0
    for b in range(2,a//2):
        if(a%b==0):
            count=count+1
    if(count<=0):
        print(a)