"""
School Assignment
Topic: String

"""

#Solution 1.
vowels = ["a", "e", "i", "o", "u"]
str1 = input("Enter a string to get Number of Vowels in the String: ")
nVow = 0
for char in str1:
	if char.lower() in vowels:
		nVow += 1
print(nVow)
print()
print()

#Solution 2.
str2 = input("Enter a String: ")
replacedStr2 = ""
for i in str2:
	if i.lower() in vowels:
		replacedStr2 += "*"
	else:
		replacedStr2 += i
print(replacedStr2)
print()
print()

#Solution 3.
str3 = input("Enter a String: ")
replacedStr3 = ""
for i in str3:
	if i.isupper():
		replacedStr3 += i.lower()
	elif i.islower():
		replacedStr3 += i.upper()
print(replacedStr3)
print()
print()

#Solution 4.
str4 = input("Enter a String: ")
replacedStr4 = ""
for i in range(len(str4)):
	if (i + 1) % 3 == 0:
		replacedStr4 += "_"
	else:
		replacedStr4 += str4[i]
print(replacedStr4)
print()
print()

#Solution 5.
str5 = input("Enter a String: ")
c = input("Enter the character whose Frequency is to be found: ")
print(str5.count(c))

#Solution 6.
str6 = input("Enter a Sentence: ")
sen6 = str6.split()
w = input("Enter the Word you want to Find: ")
if w in sen6:
	print("Found")
else:
	print("NOT FOUND")
print()
print()

#Solution 7.
str7 = input("Enter a Sentence: ")
lis7 = str7.split()
print(lis7)
word = input("Enter Word whose count you want to find: ")
print(lis7.count(word))
print()
print()

#Solution 8.
str8 = input("Enter a Sentence: ")
str8Split = str8.split()
processedStr8 = ["*".join(i) for i in str8Split]
print(" ".join(processedStr8))
print()
print()

#Solution 9.
str9 = input("Enter a Sentence: ")
symbols = [",", ".", "(", ")", "[", "]", "*", "{", "}", "_", "-", "+", "=", "?", "/", "!", "@", "#", "$", "%", "^", "&", ":", ";"] 
symNum = 0
alpha = 0
digits = 0
spaces = 0
for i in str9:
	if i.isalpha():
		alpha += 1
	if i.isdigit():
		digits += 1
	if i in symbols:
		symNum += 1
	if i == " ":
		spaces += 1
print("Number of Alphabets: ", alpha)
print("Number of Digits: ", digits)
print("Number of Spaces: ", spaces)
print("Number of Special Characters: ", symNum)
print()
print()

#Solution 10.
str101 = input("Enter First String: ")
str102 = input("Enter Second String: ")

if len(str101) > len(str102):
	print("First String is Larger!")
elif len(str101) < len(str102):
	print("Second String is Larger!")
else:
	print("Both Are Equally Large!")
print()
print()

#Solution 11.
#Program:

a = " Hello, World! "
print(len(a))
x = (a.strip())
print(x)
a = " Hello, World! "
print(a.rstrip())
a = " Hello, World! "
print(a.lstrip()) 
print()
print()

#Solution 12.
str1 = "i am very good student of class 11a"
x = str1. partition("good")
print(x)
y = str1.partition("a")
print(y)
z = str1.partition("we")
print(z)
p = str1.partition("we")
print(p)
print()
print()

#Solution 13.
str13 = input("Enter a String: ")
print(str13[::-1])

#Solution 14.
str14 = input("Enter a String: ")
if str14 == str14[::-1]:
	print("The String is a Palindrome!")
else:
	print("The String is NOT a Palindrome!")
print()
print()

#Solution 15.
str15 = input("Enter a String: ")
print(str15)
digits = [int(char) for char in str15 if char.isdigit()]
print("Number of Digits: ", digits)
print("Sum of the Digits: ", sum(digits))
print()
print()

#Solution 16.
str16 = input("Enter a Sentence: ")
longestString = max(str16.split(), key = len)
print("Longest String out of the Sentence is: ", longestString)
print()
print()

#Solution 17.
def swapString(str17):
	abc = "abc"
	xyz = "xyz"
	swappedString =""
	for char in str17:
		if char in abc:
			swappedString += xyz[abc.index(char)]
		elif char in xyz:
			swappedString += abc[xyz.index(char)]
	return swappedString
#Examples
print(swapString("abc"))
print(swapString("abz"))
print()
print()

#Solution 18:
str18 = input("Enter a String: ")
lower = 0
upper = 0
for char in str18:
	if char.islower():
		lower += 1
	elif char.isupper():
		upper += 1
print("Number of Small Letters: ", lower)
print("Number of Capital Letters: ", upper)
print()
print()

#Solution 19.
str19 = input("Enter a String: ")
replacedStr19 = ""
for i in range(len(str19)):
	if (i + 1) % 3 == 0:
		replacedStr19 += "_"
	else:
		replacedStr19 += str19[i]
print(replacedStr19)
print()
print()

#Solution 20.
thestr = "This is a test"
inputint = 3
teststr = thestr
while inputint >= 0:
	teststr = teststr[1:-1]
	inputint -= 1
testbool = "t" in teststr
print(thestr)
print(teststr)
print(inputint)
print(testbool)

#Solution 21.
Inputstr = input("enter a string")
bigint = 0
smallint = 0
otherint = 20
for x in Inputstr:
	if x >= "a" and x <= "m": #line1
		smallint += 1
	elif x > "m" and x <= "z":
		bigint += 1
	else:
		otherint += 1
print(bigint) #line2
print(smallint) #line3
print(otherint) #line4
print(Inputstr.isdigit())
