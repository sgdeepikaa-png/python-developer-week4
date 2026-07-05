from collections import namedtuple

# Create Student namedtuple
Student = namedtuple("Student", ["name", "year", "gpa", "major"])

# Student data
students = [
    Student("Priya Sharma", 2, 3.8, "Computer Science"),
    Student("Liam O'Brien", 3, 3.2, "Electrical Eng"),
    Student("Anika Patel", 1, 3.9, "Data Science"),
    Student("Carlos Ruiz", 4, 3.5, "Software Eng"),
    Student("Fatima Al-Amin", 2, 3.7, "Computer Science"),
    Student("James Kim", 3, 2.9, "Mechanical Eng"),
    Student("Mei Zhang", 1, 3.6, "Data Science"),
    Student("Omar Hassan", 4, 3.1, "Software Eng")
]

# Display function
def print_roster(students, title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    print(f"{'Name':<20}{'Year':<8}{'GPA':<8}Major")
    print("-" * 60)

    for s in students:
        print(f"{s.name:<20}{s.year:<8}{s.gpa:<8}{s.major}")

# Sort by Name
print_roster(sorted(students, key=lambda s: s.name), "Sorted by Name")

# Sort by GPA
print_roster(sorted(students, key=lambda s: s.gpa, reverse=True), "Sorted by GPA")

# Sort by Year then Name
print_roster(sorted(students, key=lambda s: (s.year, s.name)), "Sorted by Year then Name")