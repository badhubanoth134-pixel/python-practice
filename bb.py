   # Write a program to check given number is perfect number or not
# 6      :  1+2+3  ==6
# 28     : 1+2+4+7+14===28
# 10     : 1+2+5  ===> 8

sum=0
num=int(input("Enter your number to check it is perfect number or not :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        sum=sum+i

if sum==num:
    print(num," is perfect number")
else:
    print(num," is not a perfect number")