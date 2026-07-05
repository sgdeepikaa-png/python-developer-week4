course_a = {"Priya", "Liam", "Anika", "Carlos", "Fatima", "James"}

course_b = {"Anika", "Carlos", "Omar", "Mei", "James", "Sara"}

print("Course A")
print(course_a)

print("\nCourse B")
print(course_b)

print("\nUnion")
print(course_a | course_b)

print("\nIntersection")
print(course_a & course_b)

print("\nOnly in Course A")
print(course_a - course_b)

print("\nOnly in Course B")
print(course_b - course_a)

print("\nSymmetric Difference")
print(course_a ^ course_b)

print("\nMembership Test")

print("Is Anika in both courses?",
      "Anika" in course_a and "Anika" in course_b)

print("Is Omar in Course A?",
      "Omar" in course_a)