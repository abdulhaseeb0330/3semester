# # # print("hello world")
# # # # import csv as cv

# # # f=open("demo.txt","r")
# # # data=f.read()

# # # print(data)

# # # print(type(data))
# # # f.close()

# # # # f=open()
# # import os
# # t=True
# # while(t):   
# # # file making
# #     print("-------------------------------")
# #     print("welcome to Moon File Makig App")
# #     print("-------------------------------")
# #     print("press 1 empty file")
# #     print("press 2  copy data from another file")
# #     print("press 3 data write in file")
# #     print("press 4 data to file")
# #     print("press 5 delete file")
# #     print("press 6 close application")
# #     a=int(input("Enter choice"))
# #     press=0

# #     match a:
# #         case 1:
# #             press=1
# #         case 2:
# #             press=2
# #         case 3:
# #             press=3
# #         case 4:
# #             press=4
# #         case 5:
# #             press=5
# #         case 6:
# #             press=6
# #             print("Application closed successfully")
# #             exit(0)
# #         case _:
# #             print("plz! select correct option")
# #             print("press 0 to exit")
# #             print("press any key to continue....")
# #             f=input()
# #             if f==0:
# #                 t=False
# #             else:
# #                 t=True

# #     if press==1:
# #         filename=input("enter file name want to")
# #         f=open(filename,"x")
# #         f.close()
# #     elif press==2:
# #         filename_from=input("enter file name/path form")
# #         filename_to=input("enter file name/path to")
# #         f=open(filename_from,"r")
# #         data=f.read()
# #         f.close()
# #         newfile=open(filename_to,"w") 
# #         newfile.write(data)
# #         newfile.close()
# #     elif press==3:
# #         filename=input("enter file name/path ")
# #         user_data=input("enter text plz ")
# #         f=open(filename,"w")
# #         f.write(user_data)
# #         f.close()
# #     elif press==4:
# #         filename=input("enter file name want to ")
# #         user_data=input("enter text plz ")
# #         f=open(filename,"x")
# #         f.write(user_data)
# #         f.close()
# #         print("your file name is="+filename)
# #     elif press==5:
# #         filename=input("enter file name/path to delete ")
# #         if os.path.exists(filename):
# #             os.remove(filename)
# #         else:
# #             print("file not found")















# import os

# t = True
# while t:   
#     # Menu
#     print("-------------------------------")
#     print("Welcome to Moon File Making App")
#     print("-------------------------------")
#     print("Press 1: Create empty file")
#     print("Press 2: Copy data from another file")
#     print("Press 3: Write data in file")
#     print("Press 4: Create new file with data")
#     print("Press 5: Delete file")
#     print("Press 6: Close application")
    
#     try:
#         a = int(input("Enter choice: "))
#     except ValueError:
#         print("Please enter number only!")
#         continue
    
#     if a == 1:
#         filename = input("Enter file name: ")
#         try:
#             f = open(filename, "x")
#             f.close()
#             print("Empty file created:", filename)
#         except FileExistsError:
#             print("File already exists!")
            
#     elif a == 2:
#         filename_from = input("Enter source file: ")
#         filename_to = input("Enter destination file: ")
#         try:
#             with open(filename_from, "r") as f:
#                 data = f.read()
#             with open(filename_to, "w") as newfile:
#                 newfile.write(data)
#             print("Data copied successfully")
#         except FileNotFoundError:
#             print("Source file not found")
            
#     elif a == 3:
#         filename = input("Enter file name/path: ")
#         user_data = input("Enter text: ")
#         with open(filename, "w") as f:
#             f.write(user_data)
#         print("Data written to file:", filename)
        
#     elif a == 4:
#         filename = input("Enter file name: ")
#         user_data = input("Enter text: ")
#         try:
#             with open(filename, "x") as f:  
#                 f.write(user_data)
#             print("File created with data:", filename)
#         except FileExistsError:
#             print("File already exists!")
        
#     elif a == 5:
#         filename = input("Enter file name/path to delete: ")
#         if os.path.exists(filename):
#             os.remove(filename)
#             print("File deleted")
#         else:
#             print("File not found")
            
#     elif a == 6:
#         print("Application closed successfully")
#         break
#     else:
#         print("Invalid choice! Press 0 to exit or any key to continue...")
#         f = input()
#         if f == "0":
#             t = False







# students=["ali","aslam","haseeb","farooq","Fown","ubaid"]

# for word in students:
#     for a in word:
#         if(a=="f" or a=="F"):
#             print(word) 
# print("======")       
# students=["ali","aslam","haseeb","farooq","Fown","ubaid"]
# for word in students:
#     if(word[0]=="F" or word[0]=="f"):
#         print(word)


# students=["ali","aslam","haseeb","farooq","Fown","ubaid"]
# for word in students:
#     if(word.startswith("f") or word.startswith("F") ):
#         print(word)


# students=["ali","aslam","haseeb","farooq","Fown","ubaid"]
# for word in students:
#     if(word.endswith("f") or word.endswith("F") ):
#         print(word)

# students=["ali","aslam","haseeb","farooq","Fowfn","ubaid"]
# for word in students:
#     if(word.__init__("f") or word.__init__("F") ):
#         print(word)


# tup=(1,2,3,5,4,9,6,7,8,3)
# print(tup)


# def calc(tup):
#     lis=[]
    
#     for val in tup:#breakpoint ha
#         lis.append(tup[val]+1)
#         return tup
# print(calc(tup))


# x={"1":1,"city":"ibd"}
# print()


dict={"student":["ali","aslam","haseeb","farooq","Fown","ubaid"],
      "age":[10,15,18,10,20,15],
      "city":["lahore","multan","ibd","karachi","faisalabad","sialkot"],
      "class":[1,2,12,5,7,8],
      "math":[1,2,12,5,7,8],
      "phy":[1,2,12,5,7,8],
      "urdu":[1,2,12,5,7,8],
      "english":[1,2,12,5,7,8],
      }
print(dict["student"],"\n",dict["age"],"\n",dict["city"],"\n",dict["class"])
# avg marks of each student
for i in range(len(dict["student"])):
    print()

for i in range(len(dict["student"])):
    print(f" {dict['student'][i]}, Age: {dict['age'][i]}, City: {dict['city'][i]}, Class: {dict['class'][i]}")
sum=0
count=0

for i in range(len(dict["student"])):
    sum=sum+dict["age"][i]
    count=count+1
   
print(sum/count)

