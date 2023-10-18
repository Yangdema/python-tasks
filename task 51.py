num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number: "))
sum_of_numbers = 0
for i in range(num1, num2 + 1):
    sum_of_numbers += i
    print("the sum of all the numbers between", num1, "and", num2, "is:",sum_of_numbers)