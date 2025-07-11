#1.
for i in range(1, 11):
	print(i, end=" ")
print()
print()

#2.
for i in range(2, 21, 2):
	print(i, end=" ")
print()
print()

#3.
for i in range(20, 51, 2):
	print(i, end=" ")
print()
print()

#4.
for i in range(10, 0, -1):
	print(i, end=" ")
print()
print()

#5.
for i in range(40, 1, -2):
	print(i, end=" ")
print()
print()

#6.
n = int(input("Enter a Range of Factorials: "))
x = 1
f = 1
for i in range(1, n + 1):
	f = 1
	for o in range(1, x + 1):
		f = f * o
	x += 1
	print(f)
print()
print()

#7.
inp = int(input("Enter the Range of Fibonacci series > 2: ")) - 1
a = 0
b = 1
fib = 0

print(0, 1, end=" ")
for i in range(1, inp):
	fib = 0
	fib = a + b
	a = b
	b = fib
	print(fib, end=" ")
print()
print()

#8.
exp = 10
x = 4
for i in range(1, 6):
	exp = 10
	exp = exp ** x
	x -= 1
	print(exp, end=" ")
print()
print()

#9.
r = int(input("Enter the Range for Summation : "))
s = 0
for i in range(1, r + 1):
	s += i
print(s)
print()
print()

#10.
r = int(input("Enter the Range for Summation of Squares : "))
s = 0
for i in range(1, r + 1):
	s += (i ** 2)
print(s)
print()
print()

#11.
n = int(input("Enter the Range for Summation of Factorials: "))
x = 1
fac = 1
sf = 0
for i in range(1, n + 1):
	fac = 1
	for t in range(1, x + 1):
		fac = fac * t
	sf += fac
	x += 1
print(sf)
print()
print()

#12.
n = int(input("Enter the Range for Summation of Reciprocals of Factorials: "))
x = 1
fac = 1
sf = 0
for i in range(1, n + 1):
	fac = 1
	for t in range(1, x + 1):
		fac = fac * t
	sf += (1 / fac)
	x += 1
print(sf)
print()
print()

#13.
n = int(input("Enter the Range for Summation of Reciprocals of Factorials: "))
x = int(input("Enter the Numerator: "))
b = 1
fac = 1
sf = 0
for i in range(1, n + 1):
	fac = 1
	for t in range(1, b + 1):
		fac = fac * t
	sf += (x / fac)
	b += 1
print(sf)
print()
print()

#14.
u = int(input("Enter the Range for Summation: "))
x = 1
f = 0
sm = 0
for i in range(1, u + 1):
	f = 0
	for t in range(1, x + 1):
		f += t
	sm += f
	x += 1
print(sm)
print()
print()

#15.
num = int(input("Enter a Number to Reverse: "))
a = 0
rev = 0
while num != 0:
	a = num % 10
	rev += (a * (10 ** (len(str(num)) - 1)))
	num = num // 10
print(rev)
print()
print()

#16.
num2 = int(input("Enter a Number to Check if it is a Palindrome: "))
n = num2
b = 0
rev2 = 0
while num2 != 0:
	b = num2 % 10
	rev2 += (b * (10 ** (len(str(num2)) - 1)))
	num2 = num2 // 10
if rev2 == n:
	print("The Number is a Palindrome!")
else:
	print("The Number is not a Palindrome!")
print()
print()

#17.
num3 = int(input("Enter a Number to get the sum of its Digits: "))
c = 0
digSum = 0
while num3 != 0:
	c = num3 % 10
	digSum += c
	num3 = num3 // 10
print(digSum)
print()
print()

#18.
num4 = input("Enter a number to get its max Digit: ")
maxDig = 0
for char in num4:
	for dig in num4:
		if int(dig) >= int(char):
			maxDig = int(dig)
print(maxDig)
print()
print()

#19.
num5 = input("Enter a Number to check if it is an Armstrong Number: ")
sumCube = 0
for char in num5:
	sumCube += int(char) ** 3
print(sumCube)
if sumCube == int(num5):
	print("It is an Armstrong Number!")
else:
	print("It is not an Armstrong Number!")
print()
print()

#10.
num6 = int(input("Enter a Number to check if it is a Prime Number: "))
flag = 0
for i in range(2, (num6 // 2) + 1):
	if num6 % i == 0:
		flag = 1
		break
if flag == 1:
	print("It is not a Prime Number!")
else:
	print("It is a Prime Number!")
print()
print()

#21.
flag2 = 0
for j in range(10, 21):
	flag2 = 0
	for i in range(2, (j // 2) + 1):
		if j % i == 0:
			flag2 = 1
			break
	if flag2 == 0:
		print(j)

print()
