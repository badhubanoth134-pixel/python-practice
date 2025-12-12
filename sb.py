 # Write a program to print count of factors of a given number
# 10
  #  1 2 5

# 50  -- 5
count=0
num=int(input("Enter your number to print count of factors :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        count=count+1

print("number of factors: ",count)
        



