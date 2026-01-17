attendance_data = [
    (101, ['P', 'A', 'P', 'P', 'P']),
    (102, ['A', 'P', 'A', 'P', 'P']),
    (103, ['P', 'P', 'P', 'p', 'p']),
    (104, ['P', 'P', 'P', 'P', 'P']),
    (105, ['A', 'A', 'A', 'A', 'A'])
]

def attendancepercentage(attendance_data):
    percentages = {}
    for student in attendance_data:
        sid = student[0]
        record = student[1]
        presentdays = record.count('P')
        percentage = (presentdays / len(record)) * 100
        percentages[sid] = percentage
    return percentages

def lowattendancestudents(attendance_data, threshold):
    percentages = attendancepercentage(attendance_data)
    low = []
    for sid, perc in percentages.items():
        if perc < threshold:
            low.append(sid)
    return low

def dailyabsences(data):
    days = len(data[0][1])
    absences = []
    for day in range(days):
        count = 0
        for sid, record in data:
            if record[day] == 'A':
                count += 1
        absences.append(count)

    return absences


percentages = attendancepercentage(attendance_data)
print("Attendance Percentages")
for sid, perc in percentages.items():
    print(f"Student {sid}: {perc}%")

threshold = 75
print("\nStudents below threshold ", lowattendancestudents(attendance_data, threshold))
print("\nTotal absences per day", dailyabsences(attendance_data))