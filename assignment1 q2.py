attendance_data = [
    (101, ['P', 'A', 'P', 'P', 'P']),
    (102, ['A', 'A', 'P', 'P', 'A']),
    (103, ['P', 'P', 'P', 'A', 'P']),
    (104, ['P', 'A', 'A', 'P', 'P'])
]

def attendance_percentage(arr):
    percentages = {}
    for student_id, records in arr:
        total_days = len(records)
        present = records.count('P')
        percentage = (present / total_days) * 100
        percentages[student_id] = percentage
    return percentages

def low_attendance(arr, threshold):
    percent = attendance_percentage(arr)
    low_attendance = []
    for student_id, percentage in percent.items():
        if percentage < threshold:
            low_attendance.append(student_id)
    return low_attendance

def daily_absences(arr):
    days = len(arr[0][1])
    return [sum(1 for student_id, records in arr if records[day] == 'A') for day in range(days)]


print('attendance percentage:', attendance_percentage(attendance_data))
print('below threshold:', low_attendance(attendance_data, 75))
print('total absents (per day):', daily_absences(attendance_data))
