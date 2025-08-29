#Q1:To create a list L1 and find the sum and average of all elements.

L1 = [10, 20, 30, 40, 50]
sum_L1 = sum(L1)
average_L1 = sum_L1 / len(L1)
print("List L1:", L1)
print("Sum of all elements in L1:", sum_L1)
print("Average of all elements in L1:", average_L1)
print()


#Q2:To create a list L3 and find the minimum element from the list.

L3 = [23, 1, 76, 30]
min_L3 = min(L3)
print("List L3:", L3)
print("Minimum element in L3:", min_L3)
print()


#Q3:To create a copy/clone of a existing list L3. Eg: L3 = [23, 1, 76, 30] Duplicate= [23, 1, 76, 30]

L3 = [23, 1, 76, 30]
duplicate_L3 = L3.copy()
print("Original List L3:", L3)
print("Duplicate of List L3:", duplicate_L3)
print()


#Q4:To find if the element exists in the list. If found print 'Found' else print 'Not Found'

L4 = [10, 20, 30, 40, 50]
element_to_find = 30
if element_to_find in L4:
    print("Found")
else:
    print("Not Found")
    print()


#Q5:From the given list print only the odd elements.

L5 = [10, 21, 32, 43, 54, 65]
odd_elements = [num for num in L5 if num % 2 != 0]
print(L5)
print("Odd elements in L5:", odd_elements)
print()


#Q6:To replace the last element in a list with another list.

L6 = [10, 20, 30, 40, 50]
new_list = [60, 70, 80]
L6[-1:] = new_list
print("Updated List L6:", L6)
print()


#Q7:To replace the last element which are divisible by 5 to 1 in a list.

L7 = [10, 21, 30, 43, 50]
L7 = [1 if num % 5 == 0 else num for num in L7]
print("Updated List L7:", L7)
print()


#Q8:To display the sum of elements divisible by 2 from the given list LIST_SUM = [45, 3, 67, 2, 19, 12]

LIST_SUM = [45, 3, 67, 2, 19, 12]
sum_divisible_by_2 = sum(num for num in LIST_SUM if num % 2 == 0)
print("Given List LIST_SUM:", LIST_SUM)
print("Sum of elements divisible by 2 in LIST_SUM:", sum_divisible_by_2)
print()


#Q9:To append the sum the elements of two list L1 and L2 into L3. L1 and L2 are of same size.

L1 = [11, 22, 33]
L2 = [10, 20, 30]
L3 = []
for a, b in zip(L1, L2):
    L3.append(a + b)
print("L1:", L1)
print("L2:", L2)
print("Sum of elements (L3):", L3) 
print()


#Q10:To create a resultant list L3 from two given list L1:[23, 14, 56] and L2:[10, 20, 30].

L1 = [23, 14, 56]
L2 = [10, 20, 30]
L3 = L1 + L2
print("List L1:", L1)
print("List L2:", L2)
print("Resultant List L3:", L3)
print()


#Q11:To generate and print a list of frist and last 5 elements where the values are square of numbers between 1 to 30(both included).

squares = [i**2 for i in range(1, 31)]
first_five = squares[:5]
last_five = squares[-5:]
result = first_five + last_five
print("List of squares from 1 to 30:", squares)
print("First 5 elements:", first_five)
print("Last 5 elements:", last_five)
print("Resultant List (first and last 5 elements):", result)  
print() 


#Q12:To shift the elements of the List_X from left to right. Eg: List_X = [10,23,13,45,15]

List_X = [10, 23, 13, 45, 15]
shifted_List_X = [List_X[-1]] + List_X[:-1]
print("Original List_X:", List_X)
print("List_X after shifting elements from left to right:", shifted_List_X)
print()


#Q13:To create a list of strings and find the longest string.

strings_list = ["apple", "banana", "cherry", "watermelon", "kiwi"]
longest_string = max(strings_list, key=len)
print("List of strings:", strings_list)
print("Longest string in the list:", longest_string)
print()


#Q14:To create a list of strings and find the second largest string from the list LIST_X.

LIST_X = ["apple", "banana", "cherry", "watermelon", "kiwi"]
unique_strings = list(set(LIST_X))
unique_strings.sort(key=len, reverse=True)
if len(unique_strings) >= 2:
    second_largest_string = unique_strings[1]
    print("List of strings:", LIST_X)
    print("Second largest string in the list:", second_largest_string)
else:
    print("Not enough unique strings to determine the second largest.")
    print()


#Q15:To convert List to striing from the given list L. Eg: L = ['happy', 'go', 'Lucky']

L = ['happy', 'go', 'Lucky']
result_string = ' '.join(L)
print("List L:", L)
print("Converted String:", result_string)
print()