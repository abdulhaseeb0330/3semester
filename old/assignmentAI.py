# # Print average, highest, and all student grades

list=[1,10,50,99,100,70,80,70,34,23,33,33,65,76,98,24,12,34]

def fmax(list):
    max=int(list[0])
    i=1
    for i in list:
        if type(i)==int:
            if max<i:
             max=i
    return max

def favg(list):
    sum=0
    for i in list:
        sum=sum+i
    avg=sum/len(list)
    return avg

def fmin(list):
    min=int(list[0])
    for i in list:
        if type(i)==int:
            if min>i:
             min=i
    return min


def assigngrades(list):
    grades = ["A" if i >= 90 else"B" if i >= 75 else"C" if i >= 60 else"F"for i in list]
    return grades


print("high",fmax(list))
print("average",favg(list))
print("low",fmin(list))
print("grades",assigngrades(list))



# list=[{"id":101,"price":50000,"isSold":True,"cat":"Mobile"},{"id":102,"price":103,"isSold":False,"cat":"Mobile"},{"id":103,"price":50000,"isSold":True,"cat":"Furniture"}]
# max=0
# for i in list:
#     for i in i.values():
#         if type(i)==int:
#             if i>max:
#                 max=i
# print(max)

#########################
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

#
print(f"Attendance Percentages: {percentages}")
