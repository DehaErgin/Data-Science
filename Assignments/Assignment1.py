#Data Types
name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height: "))

Math = 85
Physics = 90
Chemistry = 100
Average = (Math + Physics + Chemistry)/3
print(float(Average))

string = "String"
firstCharacter = string[0]
lastCharacter = string[-1]
lenght = len(string)
reverse = string[::-1]
print(f"First Character: {firstCharacter},\nLast Character: {lastCharacter},\nLenght: {lenght}, \nReverse: {reverse}")

#Operations
num1 = float(input("Enter any number: "))
num2 = float(input("Enter one more number: "))
sumOfNumbers = num1 + num2
subtractionOfNumbers = num1 - num2
productOfNumbers = num1*num2
divisionOfNumbers = num1/num2
modOfNumbers = num1 % num2
print(f"subtractionOfNumber: {subtractionOfNumbers} ,\nsubtractionOfNumber: {subtractionOfNumbers},\nproductOfNumber: {productOfNumbers},\ndivisionOfNumbers: {divisionOfNumbers},\nmodOfNumbers: {modOfNumbers}")

studentGPA = 70
if (studentGPA >= 50):
    print("passed")
else:
    print("failed")

Age = input("Enter your age: ")
if(Age > 18):
    print("You can get a driver's license")
else:
    print("You cannot get a driver's license")

productPrice = float(input("Enter the price: "))
discountRate = float(input("Enter the discount rate: "))
amountOfDiscount = (productPrice * discountRate)/100
discountedPrice = productPrice - amountOfDiscount
print(discountedPrice)

x = True
y = False
print(x and y)
print(x or y)

#Mini Project
product1 = float(input("Enter the product1 price: "))
product2 = float(input("Enter the product2 price: "))
product3 = float(input("Enter the product3 price: "))
sumOfProducts = product1+product2+product3
if (sumOfProducts > 200):
    discountRate = (sumOfProducts * 10)/100
    discountedPrice = sumOfProducts - discountRate
    print(discountedPrice)

birthYear = input("Enter your birth year: ")
currentYear = 2025
yourAge = currentYear - float(birthYear)

if(yourAge<13):
    print("you are a child")
elif(yourAge>12 and yourAge<18):
    print("you are a young")
else:
    print("you are an adult")




