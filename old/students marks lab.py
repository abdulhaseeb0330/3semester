#input of students in list in dictionary form
#max function object
#min function object
#return having grade A and F
# course wise
list=[
    {id:101,"name":"ali","marks":85,"grade":"A","course":"java"},
    {id:102,"name":"ahmed","marks":56,"grade":"C","course":"python"},
    {id:103,"name":"haseeb","marks":94,"grade":"A","course":"mlt"},
    {id:104,"name":"sara","marks":9,"grade":"F","course":"PSY"},
    {id:105,"name":"rabia","marks":100,"grade":"A","course":"Medicine"}
    ]
# id=None
# name=None
# marks=None
# grade=None
# course=None
# def input(list):
#     id=int(input("enter id"))
#     name=input("enter name")
#     marks=int(input("enter marks"))
#     grade=input("enter grade")
#     course=input("enter course")
# list.append({
#     "id":id,f"name":{name},"marks":{marks},"grade":{grade},"course":{course}
#     })

def studentprocess(list):
    maxmarks = max(student["marks"] for student in list)
    minmarks = min(student["marks"] for student in list)
    gradesA = [student for student in list if student["grade"] =="A"]
    gradesF = [student for student in list if student["grade"] =="F"]
    # courselist = []
    # for student in list:
    #     course = student["course"]
    #     if course not in courselist:
    #         courselist[course]=[]
    #         courselist[course].append(student)
    
    # cs={}
    # cs=[cs[x.cs].append(x) for x in list]

    # print(cs)
    return {"max":maxmarks,"min":minmarks,"grade student":gradesA}
    
print(studentprocess(list))