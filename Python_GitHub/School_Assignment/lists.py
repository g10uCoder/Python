"""
Programs Regarding Lists

"""

# 1: Take a List accepting 5 numbers and print the sum and average of its elements.
# Solution:
l1 = [1, 2, 3, 4, 5] # Can be any List

lsum = sum(l1)
lavg = lsum / len(l1)

print("The sum is: ", lsum) # Sum = 15
print("The average is: ", lavg) # Average = 3

print()


# 2: Find Minimum and Maximum value of the same List.
# Solution:
lmax = max(l1)
lmin = min(l1)

print("The Maximum value is: ", lmax) # Max = 5
print("The Minimum value is: ", lmin) # Min = 1

print()


# 3: Create a copy of list [10, 5, 15, 12, 7]. The new list's name should be duplicate
# Solution:
l2 = [10, 5, 15, 12, 7]
duplicate = l2.copy()

print(duplicate)

print()


# 4: In a list X = [20, 15, 7, 25, 17, 30, 45, 11], search for an element a. If a is present then print "FOUND" and if a is absent print "NOT FOUND".
# Solution:
X = [20, 15, 7, 25, 17, 30, 45, 11]
a = 30

if a in X:
	print("FOUND")
else:
	print("NOT FOUND")

print()


# 5: Take a List and print only its odd numbers
# Solution:
L5 = [10, 21, 32, 43, 54, 65]
odd_elements = [num for num in L5 if num % 2 != 0]
print(L5)
print("Odd elements in L5:", odd_elements)
print()

# 6: To replace the last element in a list with another list.
L6 = [1, 2, 3, 4, 5]
print("L6 =", L6)
anotherlist = [7, 8, 9]
L6[-1:] = anotherlist
print("New list: ", L6)
print()

# 7: To replace the last element which are divisible by 5 to 1 in a list.
L7 = [30, 3, 5, 6, 8, 10, 35, 34, 255]
new_L7 = [1 if n % 5 == 0 else n for n in L7]
print("New List: ", new_L7)
print()

# 8: To display the sum of elements divisible by 2 form the givern list L = [45, 3, 67, 2, 19, 12]
L = [45, 3, 67, 2, 19, 12]
L_sum = sum(n for n in L if n % 2 == 0)
print("The sum of elements divisible by 2: ", L_sum)
print()

# 9: To append the sum of the elements of two lists L1 and L2 into L3.
L1 = [11, 22 , 33]
L2 = [10, 20, 30]
L3 = [L1[n] + L2[n] for n in range(len(L1))]
print("L1 =", L1)
print("L2 =", L2)
print("Sum of elements in L3 =", L3)
print()

# 10: To create a resultant list L3 from two given lists L1: [23, 14, 56] and L2: [10, 20, 30]
L1 = [23, 14, 56]
L2 = [10, 20, 30]
L3 = L1 + L2
print("The resultant list: ", L3)
print()

# 11: To generate and print a list of first and last 5 elements where the values are square of numbers between 1 to 30
L_SQ = [i ** 2 for i in range(1, 31)]
new_list = L_SQ[:5] + L_SQ[-5:]
print("The list with first 5 and last five squares is: ", new_list)
print()

# 12: To shift the elements of LIST_X form left to right. Ex- LIST_X = [10, 23, 13, 45, 15]
LIST_X = [10, 23, 13, 45, 15]
shifted_list = [LIST_X[i] for i in range(-1, len(LIST_X) - 1)]
print("Shifted list: ", shifted_list)

# 13: To create a list of strings and find the longest string
strings = ["apple", "banana", "mango", "pineapple", "strawberry"]
longest = max(strings, key=len)
print("List: ", strings)
print("Longest string: ", longest)
print()

# 14: To create a list and find the second largest string from LIST_X
LIST_X = ["apple", "banana", "mango", "pineapple", "strawberry"]
print("LIST_X =", LIST_X)
LIST_X.remove(max(LIST_X, key=len))
print("The second largest string: ", max(LIST_X, key=len))
print()

# 15: To convert given list L = ["happy", "go", "lucky"] to string
L = ["happy", "go", "lucky"]
string_L = " ".join(L)
print("Converted string: ", string_L)
print()

# 16: To convert string to list from the string given. Str = "get set go"
Str = "get set go"
L_Str = Str.split()
print("Converted list: ", L_Str)
print()

# 17: To count the number of Strings from the list L3 where the length of the string is more than equal to 4. L3 = ["happy", "more", "joy", "ants", "go", "find"]
L3 = ["happy", "more", "joy", "ants", "go", "find"]
no_of_strings = sum(1 for n in L3 if len(n) >= 4)
print("Number of strings whose length is >= 4: ", no_of_strings)
print()

# 18: From the given list Z of strings remove the first character of each string in the list and display. Z = ["happy", "apple", "high"]
Z = ["happy", "apple", "high"]
updated_string = " ".join(w[1:] for w in Z)
print("Updated string:", updated_string)

# 19: From the given list X display only the first character of each string in the list. X = ["happy", "apple", "smile"]
X = ["happy", "apple", "smile"]
updated_string = " ".join(w[0] for w in X)
print("Updated string: ", updated_string)
print()

# 20: To accept two list L2 and L1 and display True if it has at least one common element
L1 = [10, 20, 30, 40, 50]
L2 = [6, 12, 18, 24, 30]
flag = 0
for n in L1:
	if L2.count(n) > 0:
		flag = 1
		break
	else:
		pass
if flag == 0:
	print("False")
else:
	print("True")
print()

# 21: To display the LIST_R in reverse order. LIST_R = [10, 20, 30, 40, 50]
LIST_R = [10, 20, 30, 40, 50]
reverse_LIST_R = LIST_R[::-1]
print("Reversed List: ", reverse_LIST_R)
print()


# 22: To arrange the elements of the LIST_SORT in ascending order.
LIST_SORT = [3, 433, 54, 2, 554, 55, 535]
print("LIST_SORT =", LIST_SORT)
LIST_SORT.sort()
print("In ascending order: ", LIST_SORT)
print()

# 23: To find the frequency of each element form the list LIST_F.
LIST_F = [10, 20, 10, 30, 30, 40, 20, 50, 20, 10]
one_occurance = {}
one_occurance = sorted(list(set(num for num in LIST_F if num not in one_occurance)))
for i in one_occurance:
	print("Frequency of", i, ":", LIST_F.count(i))
print()

# 24: Find mean median and range from the given list LIST_Z
LIST_Z = [10, 20, 30, 40, 50]
print("LIST_Z =", LIST_Z)
mean = sum(LIST_Z) / len(LIST_Z)
median_index = ((len(LIST_Z) + 1) // 2) if len(LIST_Z) % 2 != 0 else (len(LIST_Z) // 2) - 1
median = LIST_Z[median_index - 1]
range_of_list = (LIST_Z[len(LIST_Z) - 1] - LIST_Z[0])
print("Mean =", mean)
print("Median = ", median)
print("Range =", range_of_list)
print()

# 25: To generate to lists simultaneously. L1 = [1, 2, 3], L2 = ["yellow", "blue", "red"]

# Normal form
L1 = [1, 2, 3]
L2 = ["yellow", "blue", "red"]
for i in range(3):
	print(L1[i], L2[i])
print()

# Tabular form
L1 = [1, 2, 3]
L2 = ["yellow", "blue", "red"]
L3 = [L1, L2]
for r in range(3):
	for c in range(2):
		d = L3[c]
		print(d[r], end=" ")
	print()
print()

