# 1. Write a program to enter names of employees and their salaries as input and store them in a dictionary
employees = dict()
n = int(input("Enter the number of Employees: "))
for e in range(n):
    name = input("Enter Name of Employee: ")
    salary = int(input("Enter Salry of the Employee: "))
    employees[name] = salary
print(employees)
print()

# 2. Write a program to count the number of times a character appears in a given string.
string = input("Enter a string: ")
counts = dict()
for char in string:    
    c = string.count(char)
    counts[char] = c
print(counts)
print()

# 3. Write a program to convert a number input into its corresponding number in words (876 = Eight Seven Six)
numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}
n = input("Enter a number: ")
for num in n:
    print(numbers[int(num)], end=" ")
print()

# 4. Repeatedly ask the user to enter a team name and how many games the team has won and how many they lost. Store this information in a dictionary where the keys are the team names and values are the lists of the form [wins, losses]
t = int(input("Enter number of teams: "))
team_dict = dict()
for i in range(t):
    team_name = input("Enter the name of the team: ")
    wins = input("Enter the number of wins: ")
    losses = input("Enter the number of losses: ")
    team_list = [wins, losses]
    team_dict[team_name] = team_list
print("The dictionary of the teams is: ", team_dict)
print()

# 5. Program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys are the product names and whose values are the prices.
no_of_products = int(input("Ente number of products: "))
products = dict()
for i in range(no_of_products):
    product = input("Enter product name: ")
    price = int(input("Enter price: "))
    products[product] = price
print("The dictionary of the products are: ", products)
print()

# 6. 
months = {"Jan": 31, "Feb": 28, "Mar": 31, "April": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
m = input("Enter month name: ")
print("The number of days in the month is: ", months[m])
a = list(months.keys())
b = sorted(a)
print("The keys in alphabetical order are: ", b)
months_with_31_days = list()
for month in a:
    if months[month] == 31:
        months_with_31_days.append(month)
    else:
        pass
print("The months having 31 days are: ", months_with_31_days)
sorted_months = dict()
v = list(months.values())
sv = sorted(v)
for num in sv:
    for month in a:
        if months[month] == num:
            sorted_months[month] = num
            a.remove(month)
            v.remove(num)
            break
print("The dictionary of the months sorted according to the number of days: ", sorted_months)
print()

# Write a program to add 2 dictionaries' values D1 = {"A": 10, "B": 20}, D2 = {"A": 5, "B": 15}
D1 = {"A": 10, "B": 20}
D2 = {"A": 5, "B": 15}
D3 = dict()
for i in D1.keys():
    if i in D2.keys():
        D3[i] = D1[i] + D2[i]
print("The sum of the two dictionaries: ", D3)

# Write a program to find the average of each student STU = {"NEHA": [87, 90, 78], "AMIT": [80, 95, 87]}
STU = {"NEHA": [87, 90, 78], "AMIT": [80, 95, 87]}
AVG = dict()
for student in STU.keys():
    average = round(sum(STU[student]) / len(STU[student]), 2)
    AVG[student] = average
print("The averages of the students are: ", AVG)

