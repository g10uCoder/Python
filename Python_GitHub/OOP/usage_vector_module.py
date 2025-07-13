from oop_vectors import Vector2, Vector3, Projectile

# Some Vectors
vec1 = Vector2(4.0, 3.0)
vec2 = Vector2(4.0, 3.0)

vec3 = Vector3(4.0, 5.0, 7.0)
vec4 = Vector3(5.0, 2.0, -3.0)
vec5 = Vector2(3.0, 3.0)

pro1 = Projectile(20.0, 30)

# Test Usages
print(vec1.mag()) # Show Magnitude of a Vector

print(vec1.add(vec2).show()) # Show the Resultant 2D vector after adding vec1 and vec2
print(vec3.dot(vec4)) # Show Resultant 2D Vector's Components in Tuple Format

crossVec = vec3.cross(vec4).show() # Show Resultant 3D Vector's Components in Tuple Format

print(vec5.getAngle()) # Show the Angle(in degrees) of the Vector w.r.t X-axis
print(vec5.projectile().show()) # Show the Projectile form of vec5

print(pro1.findMaxHeight()) # Find the Maximum height reached by the Projectile
print(pro1.findPeakTime()) # Find the Time to reach Maximum height reached by the Projectile
print(pro1.findRange()) # Find the total Horizontal distance covered by the Projectile
print(pro1.findTotalTime()) # Find the Total Time the Projectile was in Flight