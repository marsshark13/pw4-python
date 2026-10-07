import numpy as np
import matplotlib.pyplot as plt

# a. NumPy Array
marks = np.array([
    [78, 65, 80],
    [85, 90, 88],
    [60, 55, 65],
    [92, 88, 95],
    [70, 75, 72]
])

print("=== NUMPY ARRAY ===")
print(marks)

print("\nShape:", marks.shape)
print("Dimensions:", marks.ndim)
print("Data Type:", marks.dtype)


# b. Indexing and Slicing
print("\n=== FIRST THREE STUDENTS ===")
print(marks[:3])

print("\n=== TEST MARKS FOR ALL STUDENTS ===")
print(marks[:, 2])


# c. Mathematical Operations

# Average mark for each student
student_average = np.mean(marks, axis=1)

print("\n=== AVERAGE MARK FOR EACH STUDENT ===")

for i in range(len(student_average)):
    print(f"Student {i + 1}: {student_average[i]:.2f}")


# Average mark for each assessment
assessment_average = np.mean(marks, axis=0)

print("\n=== AVERAGE MARK FOR EACH ASSESSMENT ===")

print(f"Assessment 1: {assessment_average[0]:.2f}")
print(f"Assessment 2: {assessment_average[1]:.2f}")
print(f"Assessment 3: {assessment_average[2]:.2f}")


# Highest mark in entire array
highest_mark = np.max(marks)

print("\nHighest Mark:", highest_mark)


# d. Data Visualisation

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]

plt.bar(students, student_average)

plt.title("Average Mark for Each Student")
plt.xlabel("Students")
plt.ylabel("Average Mark")

plt.show()