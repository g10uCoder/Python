#Solution 1.
for r in range(1, 4):
	for c in range(1, 5):
		print("*", end=" ")
	print()

print()

for r in range(1, 4):
	for c in range(1, 4):
		print("A", end=" ")
	print()

print()

for r in range(1, 5):
	for c in range(1, 4):
		print("1", end=" ")
	print()

print()


#Solution 2.
for r in range(1, 4):
	for c in range(1, 4):
		print(r, end=" ")
	print()

print()

for r in range(1, 4):
	for c in range(1, 4):
		print(c, end=" ")
	print()

print()

n = 1
for r in range(1, 4):
	for c in range(1, 4):
		print(n, end=" ")
		n += 1
	print()

print()


#Solution 3.
for r in range(1, 5):
	for c in range(1, r + 1):
		print("+", end=" ")
	print()

print()


#Solution 4.
for r in range(1, 5):
	for c in range(1, r + 1):
		print(r, end=" ")
	print()

print()

for r in range(1, 5):
	for c in range(1, r + 1):
		print(c, end=" ")
	print()

print()

j = 1
for r in range(1, 5):
	for c in range(1, r + 1):
		print(j, end=" ")
		j += 1
	print()

print()


#Solution 5.
for r in range(1, 5):
	for i in range(1, 5 - r):
		print(end=" ")

	for c in range(1, r + 1):
		print(r, end=" ")
	print()

print()

for r in range(1, 5):
	for i in range(1, 5 - r):
		print(end=" ")

	for c in range(1, r + 1):
		print(c, end=" ")
	print()

print()

x = 1
for r in range(1, 5):
	for i in range(1, 5 - r):
		print(end=" ")

	for c in range(1, r + 1):
		print(x, end=" ")
		x += 1
	print()

print()


#Solution 6.
for r in range(1, 6):
	for c in range(1, 6):
		if r == 1 or r == 5 or c == 1 or c == 5:
			print("*", end=" ")

		else:
			print(end="  ")
	print()

print()

for r in range(1, 6):
	for c in range(1, 6):
		if r == 1 or r == 5 or c == 1 or c == 5 or r == c or r + c == 6:
			print("*", end=" ")

		else:
			print(end="  ")
	print()

print()


#Solution 7.
for r in range(1, 6):
	for c in range(1, 6):
		if r == 1 or r == 5 or c == 3:
			print("*", end=" ")

		else:
			print(end="  ")
	print()

print()

for r in range(1, 6):
	for c in range(1, 6):
		if c == 1 or c == 5 or r == 3:
			print("*", end=" ")

		else:
			print(end="  ")
	print()

print()

for r in range(1, 6):
	for c in range(1, 6):
		if c == 1 or c == 5 or r == 1 or r == 3:
			print("*", end=" ")

		else:
			print(end="  ")
	print()

print()


#Solution 8.
for r in range(1, 5):
	for i in range(1, 5 - r):
		print(end=" ")

	for c in range(1, r + 1):
		print("*", end=" ")
	print()

print()

y = 2
for r in range(1, 8):
	if r <= 4:
		for i in range(1, 5 - r):
			print(end=" ")

		for c in range(1, r + 1):
			print("*", end=" ")
		print()

	if r > 4:
		for i2 in range(1, y):
			print(end=" ")

		for c2 in range(1, 6 - y):
			print("*", end=" ")

		y += 1
		print()

print()


#Solution 9.
A = 65
for r in range(1, 4):
	for c in range(1, 4):
		print(chr(A), end=" ")
	A += 1
	print()

print()

A = 65
for r in range(1, 4):
	for c in range(1, 4):
		print(chr(A), end=" ")
		A += 1
	A = 65
	print()

print()

A = 65
for r in range(1, 4):
	for c in range(1, 4):
		print(chr(A), end=" ")
		A += 1
	print()

print()


#Solution 10.
A = 65
for r in range(1, 5):
	for c in range(1, r + 1):
		print(chr(A), end=" ")
	A += 1
	print()

print()

A = 65
for r in range(1, 4):
	for c in range(1, r + 1):
		print(chr(A), end=" ")
		A += 1
	A = 65
	print()

print()

A = 65
for r in range(1, 5):
	for i in range(1, 5 - r):
		print(end=" ")

	for c in range(1, r + 1):
		print(chr(A), end=" ")
	A += 1
	print()

print()


#Solution 11.
z = 122
for r in range(1, 4):
	for c in range(1, 4):
		print(chr(z), end=" ")
	z -= 1
	print()

print()

n = 10
for r in range(1, 4):
	for c in range(1, 4):
		print(n, end=" ")
		n += 1
	print()

print()

n = 1
for r in range(1, 4):
	for c in range(1, 4):
		print((n * 10), end=" ")
		n += 1
	print()

print()

for r in range(1, 5):
	for c in range(1, r + 1):
		print((r ** 2), end=" ")
	print()

print()