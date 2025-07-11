#Solution 1.


num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))

if num1 > num2:
	print("The Maximum out of the two numbers is: ", num1)

elif num2 > num1:
	print("The Maximum out of the two numbers is: ", num2)

else:
	print("Both are Equal!")

print()
print()


#Solution 2.
n1 = int(input("Enter first Number: "))
n2 = int(input("Enter second Number: "))
n3 = int(input("Enter third Number: "))

if n1 > n2 and n1 > n3:
	print("The Maximum out of the three numbers is: ", n1)

elif n2 > n1 and n2 > n3:
	print("The Maximum out of the three numbers is: ", n2)

elif n3 > n1 and n3 > n2:
	print("The Maximum out of the three numbers is: ", n3)

elif n1 == n2 and n1 == n3:
	print("All the numbers are Equal!")

print()
print()


#Solution 3.
num = int(input("Enter a Number: "))

if num % 2 == 0:
	print("It is an Even Number!")

else:
	print("It is an Odd Number!")

print()
print()

#Solution 4.
num4 = int(input("Enter a Number: "))
if num4 >= 0:
	print("The Number is Positive!")
else:
	print("The Number is Negative!")
print()
print()

#Solution 5.
operands = ["+", "-", "*", "/", "%", "^"]
sen = input("Enter the Calculation in [integer1 operand integer2] format: ")
s = sen.split()
s0 = int(s[0])
s2 = int(s[2])

if s[0].isnumeric() and s[2].isnumeric() and s[1] in operands:
	if s[1] == "+":
		result = s0 + s2
		print(result)

	elif s[1] == "*":
		result = s0 * s2
		print(result)

	elif s[1] == "-":
		result = s0 - s2
		print(result)

	elif s[1] == "/":
		result = s0 / s2
		print(result)

	elif s[1] == "%":
		result = s0 % s2
		print(result)

	elif s[1] == "^":
		result = s0 ** s2
		print(result)

print()
print()


#Solution 6.
rSq = float(input("Enter Radius of the Circle: ")) ** 2
print("The area of the Circle is: ", round((3.14159 * rSq), 3))

side = float(input("Enter Side of thr Square: ")) ** 2
print("The area of the Square is: ", round(side, 3))

l = float(input("Enter Length of thr Rectangle: "))
b = float(input("Enter Length of thr Rectangle: "))
print("The area of the Rectangle is: ", round(l * b, 3))

print()
print()


#Solution 7.
c = input("Enter a Character: ")
if c.isupper():
	print("The character is Uppercase")

else:
	print("The character is Lowercase")
print()
print()


#Solution 8.
marks = int(input("Enter Avg. Marks: "))
if marks >= 80 and marks <= 100:
	print("Grade: A")

elif marks >= 60 and marks < 80:
	print("Grade: B")

elif marks >= 40 and marks < 60:
	print("Grade: C")

elif marks >= 33 and marks < 40:
	print("Grade: D")

elif marks >= 0 and marks < 33:
	print("Grade: Fail!")

else:
	print("Invalid Marks!")
print()
