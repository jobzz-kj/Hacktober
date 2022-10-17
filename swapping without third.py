num1,num2= map(int,input('Enter inputs : ').split())
num1,num2 = num2,num1
print(num1,num2)

# OR

num2 = num1 + num2
num1 = num2 - num1
num2 = num2 - num1
print(num1,num2)
