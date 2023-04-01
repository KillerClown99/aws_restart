#1) Largest among three numbers 

 

num1= input("Enter the first number :") 
num2= input("Enter the second number :") 
num3= input("Enter the last number :") 
 
if num1>= num2 and num1>= num3 : 
    print ("The largest number is "+ str(num1)) 
elif num2>= num1 and num2>= num3 : 
    print ("The largest number is "+ str(num2)) 
else : 
    print ("The largest number is "+ str(num3)) 

 

#2) Find the number is odd or even 

num= int(input("Enter the number: ")) 
 
if (num % 2)==0 : 
    print ("{} is even".format(num)) 
else : 
    print("{} is odd".format(num)) 

 

#3) Swap two variables 

 

x = input("Enter a value : ") 

y = input("Enter another value : ") 

 

temp = x 

x = y 

y = temp 

 

print("The of x after swapping is {}". format(x)) 

print("The of y after swapping is {}". format(y)) 

 

#4) Prime no. Or not 

Number = int(input(" Please Enter any Number: ")) 

count = 0 

 

for i in range(2, (Number//2 + 1)): 

    if(Number % i == 0): 

        count = count + 1 

        break 

 

if (count == 0 and Number != 1): 

    print(" %d is a Prime number" %Number) 

else: 

    print(" %d is composite number" %Number) 

 

#5) Find the factorial 

 

number = int(input(" Please enter any Number : ")) 

fact = 1 

 

for i in range(1, number + 1): 

    fact = fact * i 

print("The factorial of %d  = %d" %(number, fact)) 

 

#6) Print individual letters of a string using for loop 

 

value = input(" Please enter any value : ") 

 

for i in value : 

    print(i) 

 

#7) Iteration of list using for loop 

 

list1 =[ "apple", "banana", "pineapple", "grapes", "cucumber", "watermelon", "orange"] 

 

for i in list1 : 

    print(i) 

 

#8) Print multiplication table using range function 

 

num = int(input("Enter a number : ")) 

for i in range(1,11) : 

    j = i * num 

    print(str(i) + " * " + str(num) + " = " + str(j)) 

 

#9) Print 1 to n using while loop 

 

num = int(input("Enter a number : ")) 

i = 1 

while i <= num: 

    print (i) 

    i+=1 

 

#10) Fibonacci Sequence 

 

n_terms = int(input ("How many terms the you wants to print?  "))   

n1 = 0   

n2 = 1   

count = 0   

   

   

if n_terms <= 0:   

    print ("Please enter a positive integer")   

 

elif n_terms == 1:   

    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")   

    print(n1)   

 

else:   

    print ("The fibonacci sequence of the numbers is:")   

    while count < n_terms:   

        print(n1)   

        nth = n1 + n2   

       

        n1 = n2   

        n2 = nth   

        count += 1  

     

 