class Vector2:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def add(self, vec2):
		x = self.x + vec2.x
		y = self.y + vec2.y
		res = Vector2(x, y)

		return res

	def mag(self):
		magnitude = round(((self.x ** 2) + (self.y ** 2)) ** 0.5, 3)
		return magnitude

	def show(self):
		return (self.x, self.y)

	def change(self, x, y):
		self.x = x
		self.y = y

		return self

	def dot(self, vec2):
		x = self.x * vec2.x
		y = self.y * vec2.y
		res = x + y
		return res

class Vector3:
	def __init__(self, x: float, y: float, z: float):
		self.x = x
		self.y = y
		self.z = z

	def add(self, vec2):
		x = self.x + vec2.x
		y = self.y + vec2.y
		z = self.z + vec2.z
		res = Vector3(x, y, z)

		return res

	def mag(self):
		magnitude = round(((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5, 3)
		return magnitude

	def show(self):
		return (self.x, self.y, self.z)

	def change(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z


	def dot(self, vec2):
		x = self.x * vec2.x
		y = self.y * vec2.y
		z = self.z * vec2.z
		res = x + y + z

		return res

	def cross(self, vec2):
		x = (self.y * vec2.z) - (self.z - vec2.y)
		y = (self.z * vec2.x) - (self.x - vec2.z)
		z = (self.x * vec2.y) - (self.y * vec2.x)
		res = Vector3(x, y, z)

		return res


num = MyMath()
vec1 = Vector2(4.0, 3.0)
vec2 = Vector2(4.0, 3.0)

myList = ["List", 1, 2, 2, 5, 7]

print(num.summation(5, 7))
print(num.sumList(myList))

print(vec1.mag())
print(vec1.add(vec2).show())

