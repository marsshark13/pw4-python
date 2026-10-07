import pandas as pd

# a. DataFrame

data = {
    "Student_ID": [
        "F1001",
        "F1002",
        "F1003",
        "F1004",
        "F1005",
        "F1005",
        "F1006",
        "F1007"
    ],

    "Name": [
        "Ali",
        "Siti",
        "Kumar",
        "Aina",
        "Daniel",
        "Daniel",
        "Mei Ling",
        "Amir"
    ],

    "Department": [
        "JTMK",
        "JTMK",
        "JKE",
        "JTMK",
        "JKE",
        "JKE",
        "JTMK",
        "JKE"
    ],

    "Mark": [
        78,
        85,
        None,
        92,
        70,
        70,
        88,
        None
    ]
}

df = pd.DataFrame(data)

print("=== ORIGINAL DATAFRAME ===")
print(df)


# b. Data Cleaning

# Remove duplicate records
df = df.drop_duplicates()

# Calculate mean of available marks
mean_mark = df["Mark"].mean()

# Replace missing marks with mean
df["Mark"] = df["Mark"].fillna(mean_mark)

print("\n=== CLEANED DATAFRAME ===")
print(df)


# c. Data Processing

# Students with marks 75 and above
high_marks = df[df["Mark"] >= 75]

print("\n=== STUDENTS WITH MARKS 75 AND ABOVE ===")
print(high_marks)


# Sort highest to lowest
sorted_df = df.sort_values(by="Mark", ascending=False)

print("\n=== STUDENTS SORTED FROM HIGHEST TO LOWEST ===")
print(sorted_df)


# Average mark for each department
department_average = df.groupby("Department")["Mark"].mean()

print("\n=== AVERAGE MARK FOR EACH DEPARTMENT ===")
print(department_average)


# d. Data Export
df.to_csv("student_analysis.csv", index=False)

print("\nstudent_analysis.csv successfully created.")
