

# marks=int(input("enter marks"))
# ch=int(input("enter CH"))



# def checkdata(marks,ch):
#     if marks<=80 and marks>=0:
#         if ch==4:
#              if marks>=60 :
#                 print("Grade A")
#              elif marks>=50:
#                         print("Grade B")
#              elif marks>=30:
#                         print("Grade C")
#              elif marks<30:
#                   print("Grade f")
#              else:
#                 print("invalid ch")
#         else:
#             print("invalid marks")
#          #function of 4 ch
#     elif marks<=55 and marks>=0:
#         if ch==3:
#               if marks>=45 :
#                 print("Grade A")
#               elif marks>=35:
#                             print("Grade B")
#               elif marks>=25:
#                             print("Grade C")
#               elif marks<25:
#                     print("Grade f")
#               else:
#                     print("invalid ch")
   
#     elif marks<=40 and marks>=0:
#         if ch==2:
#             if marks>=30 :
#                     print("Grade A")
#             elif marks>=20:
#                             print("Grade B")
#             elif marks>=12:
#                             print("Grade C")
#             elif marks<12:
#                     print("Grade f")
#             else:
#                     print("invalid ch")
#     else:
#                 print("invalid marks")
#          #function of 2 ch
    

# checkdata(marks,ch)

# # if marks>40  and marks<0:
# #     if CH<2 and CH>2:
# #         if marks>40 and CH==2:
# #             print("Grade A")
# #         elif marks>30 and CH==2:
# #             print("Grade B")
# #         elif marks>20 and CH==2:
# #             print("Grade C")
# #         else:
# #             print("F")
# #     else:
# #         print("invalid CH")
# # elif CH<2 or CH>2:
# #     print("invalid marks and ch")
# # else:
# #     print("invalid Marks ")




marks=int(input("enter marks"))
ch=int(input("enter CH"))

if ch==4:
    if marks<=80 and marks>=0:
         if marks>=60 :
            print("Grade A")
         elif marks>=50:
                    print("Grade B")
         elif marks>=30:
                    print("Grade C")
         elif marks<30:
              print("Grade f")
         else:
            print("invalid ch")
    else:
        print("invalid marks")
     #function of 4 ch
elif ch==3:
    if marks<=55 and marks>=0:
          if marks>=45 :
            print("Grade A")
          elif marks>=35:
                        print("Grade B")
          elif marks>=25:
                        print("Grade C")
          elif marks<25:
                print("Grade f")
          else:
                print("invalid ch")
    else:
        print("invalid marks")
     #function of 3 ch
elif ch==2:
    if marks<=40 and marks>=0:
        if marks>=30 :
                print("Grade A")
        elif marks>=20:
                        print("Grade B")
        elif marks>=12:
                        print("Grade C")
        elif marks<12:
                print("Grade f")
        else:
                print("invalid ch")
    else:
                print("invalid marks")
     #function of 2 ch
else:
            print("invalid ch")