import numpy as np

marks = np.array([88, 99, 67, 87, 65, 85, 75, 23, 33, 43])

print("Marks of all students:", marks)

avg = np.mean(marks)
print("Average marks:", avg)

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))

print("\nStudent Results:")
for mark in marks:
    if mark >= 40:
        print(f"{mark} -> Pass")
    else:
        print(f"{mark} -> Fail")

pass_students = np.sum(marks >= 40)
fail_students = np.sum(marks < 40)

print("\nSummary:")
print("Pass students:", pass_students)
print("Fail students:", fail_students)