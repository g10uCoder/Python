"""
Programs Regarding Lists

"""

# Question 1: Take a List accepting 5 numbers and print the sum and average of its elements.
# Solution:
l1 = [1, 2, 3, 4, 5] # Can be any List

lsum = sum(l1)
lavg = lsum / len(l1)

print("The sum is: ", lsum) # Sum = 15
print("The average is: ", lavg) # Average = 3

print()


# Question 2: Find Minimum and Maximum value of the same List.
# Solution:
lmax = max(l1)
lmin = min(l1)

print("The Maximum value is: ", lmax) # Max = 5
print("The Minimum value is: ", lmin) # Min = 1

print()


# Question 3: Create a copy of list [10, 5, 15, 12, 7]. The new list's name should be duplicate
# Solution:
l2 = [10, 5, 15, 12, 7]
duplicate = l2.copy()

print(duplicate)

print()


# Question 4: In a list X = [20, 15, 7, 25, 17, 30, 45, 11], search for an element a. If a is present then print "FOUND" and if a is absent print "NOT FOUND".
# Solution:
X = [20, 15, 7, 25, 17, 30, 45, 11]
a = 30

if a in X:
	print("FOUND")
else:
	print("NOT FOUND")

print()


# Question 5: Take a List and print only its odd numbers
# Solution:
L5 = [10, 21, 32, 43, 54, 65]
odd_elements = [num for num in L5 if num % 2 != 0]
print(L5)
print("Odd elements in L5:", odd_elements)
print()

# Question 6: To replace the last element in a list with another list.
L6 = [1, 2, 3, 4, 5]
print("L6 =", L6)
anotherlist = [7, 8, 9]
L6[-1:] = anotherlist
print("New list: ", L6)
print()

# Question7: To replace the last element which are divisible by 5 to 1 in a list.
L7 = [30, 3, 5, 6, 8, 10, 35, 34, 255]
new_L7 = [1 if n % 5 == 0 else n for n in L7]
print("New List: ", new_L7)
