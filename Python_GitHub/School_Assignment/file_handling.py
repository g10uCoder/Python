'''
Q-1 Create a file Data.txt using function CreateData() with following data:
    "Python provides an inbuilt function for creating, writing and reading files."
    Write a program to:
    a. Read and view the file using mode 'w' and 'a'.
    b. Read and view only "Python Provides".
    c. Count the number of characters/size in the file.
    d. To count numbers of spaces in a file.
    e. To count the number of spaces in a file.
'''

def createFile():
    with open("Data.txt", "w") as file:
        file.write("Python provides an inbuilt function for creating, writing and reading files.")

def read_and_view_file():
    with open("Data.txt", "r") as file:
        content = file.read()
        print(content)
        print(content[:15])
        print(f"Number of characters in the file: {len(content)}")
        space_count = content.count(' ')
        print(f"Number of spaces in the file: {space_count}")

createFile()
read_and_view_file()


'''
Q-2 Create a file File1.txt using function CreateFile() with following instructions:
    'we are learning file handlingn'
    'we are understanding how it works'
    'We are storing data in notepad'
    'file handling stores data'
Write the programs with following functions to :
a. Countlines() -Count the no of lines using readlines, readline and read().Using function CountLine(..
a. Wordlen3()- Count the number of words with length 4 and return it.
b. TotalWord() - Count the total number of words.
c. LineData() - Display the lines containing the word 'data' from the text file.
'''

def CreateFile():
    with open("File1.txt", "w") as file:
        file.write("we are learning file handling\n")
        file.write("we are understanding how it works\n")
        file.write("we are storing data in notepad\n")
        file.write("file handling stores data\n")

def CountLine():
    with open("File1.txt", "r") as file:
        lines = file.readlines()
        print(f"Number of lines using readlines: {len(lines)}")
        
        file.seek(0)
        line_count = 0
        while file.readline():
            line_count += 1
        print(f"Number of lines using readline: {line_count}")
        
        file.seek(0)
        content = file.read()
        print(f"Number of lines using read(): {content.count('\\n') + 1}")

def Wordlen3():
    with open("File1.txt", "r") as file:
        content = file.read()
        words = content.split()
        count = sum(1 for word in words if len(word) == 4)
        print(f"Number of words with length 4: {count}")

def TotalWord():
    with open("File1.txt", "r") as file:
        content = file.read()
        words = content.split()
        print(f"Total number of words: {len(words)}")

def LineData():
    with open("File1.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if 'data' in line:
                print(line.strip())

CreateFile()
CountLine()
Wordlen3()
TotalWord()
LineData()


'''
Q-3 Using the above file create the function
a. FirstChar() to count and display the number of lines beginning from 'W'or 'w'.
b. Vowel() to count the number of words which begin with vowel and end with vowel.
c. CountWord() to count the words which ends with 'g'.
'''

def FirstChar():
    with open("File1.txt", "r") as file:
        lines = file.readlines()
        count = sum(1 for line in lines if line.startswith(('W', 'w')))
        print(f"Number of lines beginning with 'W' or 'w': {count}")

def Vowel():
    with open("File1.txt", "r") as file:
        content = file.read()
        words = content.split()
        count = sum(1 for word in words if word[0].lower() in 'aeiou' and word[-1].lower() in 'aeiou')
        print(f"Number of words that begin and end with a vowel: {count}")

def CountWord():
    with open("File1.txt", "r") as file:
        content = file.read()
        words = content.split()
        count = sum(1 for word in words if word.endswith('g'))
        print(f"Number of words that end with 'g': {count}")

FirstChar()
Vowel()
CountWord()

'''
Q-4 Create a copy of Filel txt to another file. The user should be allowed to given the file name.
    Function CopyFile().
'''

def CopyFile():
    source_file = "File1.txt"
    destination_file = input("Enter the name of the destination file: ")
    
    with open(source_file, "r") as src:
        content = src.read()
        
    with open(destination_file, "w") as dest:
        dest.write(content)
        
    print(f"File '{source_file}' has been copied to '{destination_file}'.")

CopyFile()


'''
Q-5 Create a file File2.txt using function CreateNew() with following information: 
'we have 200 apples in basket.'
'41 apples are given to class 12c'
'52 apples were sold off'
'we will now distribute them in class.'
Write the functions for the following:
a. Count the number of digits in the file and return it using function CountDigit().
b. Count the number of times words 'apples' and 'we' appear and display as follows using CountTwoWords().
apples count is: 3
we count is: 2
'''

def CreateNew():
    with open("File2.txt", "w") as file:
        file.write("we have 200 apples in basket.\n")
        file.write("41 apples are given to class 12c\n")
        file.write("52 apples were sold off\n")
        file.write("we will now distribute them in class.\n")

def CountDigit():
    with open("File2.txt", "r") as file:
        content = file.read()
        digit_count = sum(1 for char in content if char.isdigit())
        print(f"Number of digits in the file: {digit_count}")

def CountTwoWords():
    with open("File2.txt", "r") as file:
        content = file.read()
        apples_count = content.count('apples')
        we_count = content.count('we')
        print(f"apples count is: {apples_count}")
        print(f"we count is: {we_count}")

CreateNew()
CountDigit()
CountTwoWords()


'''
Q-6 Using file File1.txt create a function SEARCH(file, word) to search for a word and return 'found ' if word exist else "not found".
'''

def SEARCH(file, word):
    with open(file, "r") as f:
        content = f.read()
        if word in content:
            return "found"
        else:
            return "not found"

file_name = "File1.txt"
search_word = input("Enter the word to search: ")
result = SEARCH(file_name, search_word)
print(result)


'''
Q-7 Open file File1 txt and count the occurrence of the character 'a' and 'w' in the file. Display as following:
a count ....
w count ....
'''

def CountCharacters():
    with open("File1.txt", "r") as file:
        content = file.read()
        a_count = content.count('a')
        w_count = content.count('w')
        print(f"a count: {a_count}")
        print(f"w count: {w_count}")

CountCharacters()


'''
Q-8 A text file "employee.txt" has structure [empno, name,salary, dept).
a. Write a user define function CreateFile() to input data for a record and add it to employee.txt.
b. Write a function Countdata(dept) which accepts the department name as parameter and count and return number of employees in the department accepted.
c. Define a function Display to view all the records in the file.
'''

def CreateFile():
    empno = input("Enter employee number: ")
    name = input("Enter employee name: ")
    salary = input("Enter employee salary: ")
    dept = input("Enter employee department: ")
    
    with open("employee.txt", "a") as file:
        file.write(f"{empno}, {name}, {salary}, {dept}\n")

def Countdata(dept):
    with open("employee.txt", "r") as file:
        lines = file.readlines()
        count = sum(1 for line in lines if line.strip().split(', ')[3] == dept)
        return count
    
def Display():
    with open("employee.txt", "r") as file:
        content = file.read()
        print(content)

CreateFile()
department_name = input("Enter the department name: ")
employee_count = Countdata(department_name)
print(f"No. of employees in {department_name} department: {employee_count}")
Display()


