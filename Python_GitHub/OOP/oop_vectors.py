"""
Creating a Module for Vectors
Contains Basic Functions like add, sub, dot, cross, mag, etc.

"""

import math

g = 9.8

# Class For 2D Vectors
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

	def getAngle(self):
		t = round(math.degrees(math.atan(self.y / self.x)))

		return t

	def projectile(self):
		magnitude = round(((self.x ** 2) + (self.y ** 2)) ** 0.5, 2)
		angle = round(math.degrees(math.atan(self.y / self.x)))

		p = Projectile(magnitude, angle)

		return p


# Class for 3D Vectors
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
		magnitude = round(((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5, 2)
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
		x = (self.y * vec2.z) - (self.z * vec2.y)
		y = (self.z * vec2.x) - (self.x * vec2.z)
		z = (self.x * vec2.y) - (self.y * vec2.x)
		res = Vector3(x, y, z)

		return res



class Projectile:
	def __init__(self, mag: float, angle: int):
		self.mag = mag
		self.angle = angle

	def findMaxHeight(self):
		h = round(((self.mag * math.sin(math.radians(self.angle))) ** 2) / (2 * g), 2)

		return h

	def findPeakTime(self):
		t = round(((self.mag * math.sin(math.radians(self.angle))) / (g)), 2)

		return t

	def findRange(self):
		r = round((((self.mag ** 2) * math.sin(math.radians(2 * self.angle))) / (g)), 2)

		return r

	def findTotalTime(self):
		T = round(2 * ((self.mag * math.sin(math.radians(self.angle))) / (g)), 2)

		return T

	def vector(self):
		x = round(self.mag * (math.cos(math.radians(self.angle))), 2)
		y = round(self.mag * (math.sin(math.radians(self.angle))), 2)

		res = Vector2(x, y)

		return res

	def show(self):
		return (self.mag, self.angle)



# Some Vectors
vec1 = Vector2(4.0, 3.0)
vec2 = Vector2(4.0, 3.0)

vec3 = Vector3(4.0, 5.0, 7.0)
vec4 = Vector3(5.0, 2.0, -3.0)
vec5 = Vector2(3.0, 3.0)

# Test Usages
print(vec1.mag()) # Show Magnitude of a Vector
print(vec1.add(vec2).show())
print(vec3.dot(vec4))
crossVec = vec3.cross(vec4).show() # Show Resultant Vector's Components in Tuple Format
print(vec5.getAngle()) # Show the Angle(in degrees) of the Vector w.r.t X-axis

print(vec5.projectile().show())


