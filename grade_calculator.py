name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)
