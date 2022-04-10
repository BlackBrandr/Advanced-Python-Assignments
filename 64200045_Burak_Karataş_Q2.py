import pandas as pd
from scipy.stats.stats import pearsonr

df = pd.read_excel('COE-101-Grades.xlsx')

# Replacing the N/A values with 0.
df = df.fillna(0)

# All Users Scores
students = {}

# Iterating through the users' data.

# Midterm 1 - 25%
# Midterm 2 - 25%
# Final - 50%

for index, row in df.iterrows():
    students[row["STUDENTNO"]] = (float(row["MIDI"]) * 0.25) + (float(row["MIDII"]) * 0.25) + (float(row["FIN"]) * 0.5)

print("All Students' Number Gradings: \n")
print(students, "\n\n")

# Letter Grading
print("Students' Letter Grading: \n")

students_letter_grading = {}

for key, value in students.items():
    if value >= 94:
        students_letter_grading[key] = "A+"
    elif value >= 87:
        students_letter_grading[key] = "A"
    elif value >= 79:
        students_letter_grading[key] = "B+"
    elif value >= 70:
        students_letter_grading[key] = "B"
    elif value >= 60:
        students_letter_grading[key] = "C+"
    elif value >= 50:
        students_letter_grading[key] = "C"
    elif value >= 45:
        students_letter_grading[key] = "D+"
    elif value >= 40:
        students_letter_grading[key] = "D"
    elif value < 40:
        students_letter_grading[key] = "F"

print(students_letter_grading, "\n\n")

# Students who fail/did not pass the course (grading scores under or equal to 50)
print("Students' Passing / Not Passing: \n")

failed_students = []

# Adding Letter Grades to the main Data Frame
for key, value in students.items():
    if value <= 50:
        failed_students.append(key)

print(failed_students)

# Assigning to the dataframe
l_grades = []

for key, value in students_letter_grading.items():
    l_grades.append(value)

df = df.assign(LGRADE=l_grades)
print(df, "\n\n")

# Pivot Table
print("Pivot Table: \n")
print(pd.pivot_table(df, index=["NAME", "LGRADE"], values="STUDENTNO"), "\n\n")

# Histogram Table
# df.hist(column='FIN')

# Pie Graph
custom_df = pd.DataFrame({
    'SUM': [2, 3, 3, 6, 4, 4, 0, 2, 4]
}, index=['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F'])

# plot = custom_df.plot.pie(y='SUM', figsize=(5, 5))

# MIDI & MIDII Average
midi = []
midii = []
final_scores = []
student_no_list = []


def Average(lst):
    return sum(lst) / len(lst)


for index, row in df.iterrows():
    midi.append(row["MIDI"])
    midii.append(row["MIDII"])
    final_scores.append(row["FIN"])
    student_no_list.append(row["STUDENTNO"])

print(f"Midterm 1 Grades: {midi}")
print(f"Midterm 2 Grades: {midii}")

print(f"Midterm 1 Average: {Average(midi)}")
print(f"Midterm 2 Average: {Average(midii)}")

# Final 10% Check
mid_avg = []

increased_10_list = []

for i in range(len(midi)):
    if (midi[i] * 1.1 >= final_scores[i]) and (midii[i] * 1.1 >= final_scores[i]):
        increased_10_list.append(student_no_list[i])

print("\n\nStudents who increased their score by at least 10% in the Final Exam: \n")
print(increased_10_list)

# Midterm 1 & Midterm 2 Average
for i in range(len(midi)):
    mid_avg.append((midi[i] + midii[i]) / 2)

# Midterm 1 & Final Correlation
print("\n\n Midterm 1 / Midterm 2 & Final Grades Correlation: \n")

print(f"Midterm 1 & Final Correlation Value: {pearsonr(midi, final_scores)}")

# Midterm 2 & Final Correlation
print(f"Midterm 2 & Final Correlation Value: {pearsonr(midii, final_scores)} \n")
