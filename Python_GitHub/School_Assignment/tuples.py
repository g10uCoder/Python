"""
School Assignment
Tuples

"""
# 1.
T1 = (1, 2, 3, 4, 5, 6, 7)
s1 = sum(T1)
size = len(T1)
avg = s1 / size
print("Sum of the elements of the Tuple is: ", s1)
print("The Average is: ", avg)
print("The Highest element of the tuple is: ", max(T1))
print("The Lowest element of the tuple is: ", min(T1))
print("The size of the tuple is: ", size)
print()

# 2.
T1 = (10, 11, 21)
T2 = (20, 5, 7)
T3 = T1 + T2
print("T1 + T2 = T3 =", T3)

# 3.
tuple_square = ()
for n in range(1, 16):
	sq = (n ** 2, )
	tuple_square += sq
	
print("The tuple is: ", tuple_square)
print()

# 4.
F = [0, 1]
a = 0
b = 1
for i in range(1, 7):
	fib = a + b 
	a = b
	b = fib
	F.append(fib)
print("Tuple containing Fibonacci: ", tuple(F))
print()

# 5.
T5 = (1, 3, 5, 6, 7, 9, 0)
print("T5 =", T5)
even_T5 = ()
for i in range(0, len(T5), 2):
	even_T5 += (T5[i], )
print("The even elements of the tuple T5: ", even_T5)
print()

# 6.
T6 = ("Python", "is", "the", "best!")
print("T6 =", T6)
t6_str = " ".join(T6)
print(t6_str)
print()

# 7.
L7 = [4, 5, 6, 7, 8, 9]
print("L7 =", L7)
converted_tuple = ()
for i in L7:
	element = (i, )
	converted_tuple += element
print("L7 converted to tuple is: ", converted_tuple)

T7 = ("apple", "banana", "mango")
print("T7 =", T7)
converted_list = []
for i in L7:
	converted_list.append(i)
print("T7 converted to list is: ", converted_list)
print()

# 8.
T8 = (4, 45, 67, 123, 5, 6, 7, 3445)
print("T8 =", T8)
element_to_find = 45 # Example
if element_to_find in T8:
	print("FOUND")
else:
	print("NOT FOUND")
print()

# 9.
T9 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("T9 =", T9)
print("Fourth element from the beginning: ", T9[3])
print("Fourth element from the last: ", T9[-4])

# 10.
T = (1, 3, 4, 6, 1, 5, 2, 3, 4, 1, 3, 1, 2, 1)
print("T =", T)
e = 1
print("The Frequency of 1 in the tuple is: ", T.count(e))
print()

# 11.
T11 = (1, 3, 5, 7, 9, 11)
L11 = list(T11)
L11.remove(9)
print("The new tuple with 9 removed: ", tuple(L11))
print()

# 12.
v, w, x, y, z = (1, 2, 3, 4, 5)
print("Tuple to be unpacked: (1, 2, 3, 4, 5)")
str12 = str(v) + str(w) + str(x) + str(y) + str(z)
values = " ".join(str12)
print("The unpacked values are: ", values)
print()

# 13.
Tx = (15, 25, 23, 16, 125, 17, 35)
Tnew = ()
for n in Tx:
	if n % 5 == 0:
		Tnew += (n, )
	else:
		pass
print("The new tuple: ", Tnew)
print()

# 14.
Rx = ((2, 4), (13, 12), (14, 7), (24, 6))
c = 0
for t in Rx:
	if (t[0] + t[1]) % 2 == 0:
		c += 1
	else:
		pass
print("No. of fully even elements: ", c)
print()

# 15.
t1 = (11, 2, 4)
t2 = (2, 41, 44)
ts = t1 + t2
flag = 0
for n in ts:
	if ts.count(n) > t1.count(n):
		flag = 1
		break
	else:
		pass
if flag == 1:
	print("True")
else:
	print("False")
print()

# 16.
T16 = ("This", "is", "a", "Tuple")
print("T16 =", T16)
max_str = max(T16, key=len)
min_str = min(T16, key=len)
print("The largest string in the tuple: ", max_str)
print("The smallest string in the tuple: ", min_str)

