n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks of student "+i+1+": "))
    marks.append(m)


def average_marks(marks_list):
    total = 0
    for m in marks_list:
        total += m
    return total / len(marks_list)

def highest_marks(marks_list):
    highest = marks_list[0]
    for m in marks_list:
        if m > highest:
            highest = m
    return highest


def grades(marks_list):
    grade_list = [
        "A" if m >= 90 else
        "B" if m >= 75 else
        "C" if m >= 60 else
        "F"
        for m in marks_list
    ]
    return grade_list


print("\n--- Results ---")
print("Average Marks:", average_marks(marks))
print("Highest Marks:", highest_marks(marks))
print("Grades of all students:", grades(marks))
