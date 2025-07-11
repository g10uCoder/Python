class MyMath:
	def __init__(self):
		pass


	def summation(self, a, b):
		result = 0

		for i in range(a, b + 1):
			result += i

		return result

	def sumList(self, a):
		result = 0

		for i in a:
			if str(i).isdigit():
				result += int(i)

		return result