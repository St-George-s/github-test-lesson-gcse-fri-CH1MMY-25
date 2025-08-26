num = int(input("Input number: "))  
#automatialy prints one for 0 or 1
if num == 0 or num == 1:
    print(1)  
else:
    factorial = 1
    for i in range(1, num + 1):  
        #multiplies num+1 by value of 1
        factorial *= i
    print("Factorial of {num} is {factorial}") 
    print(num)
    print(" is ")  
    print(factorial) 