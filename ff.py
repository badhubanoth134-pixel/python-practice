    # Write a program to find number of digits in a given number
 #input: 5235
 #op: 4

num=6574
count=0 
while num!=0:           # 0 !=0
    num=num//10         # 6//10  --> 0
    count=count+1        # 4
print("Number of digits : ",count)
 