# # list=[1,27,33,12,20,15,2378]
# # for i in range(5):
# #     x=int(input("enter numbers"))
# #     list[i].append(x)
x=[int(input("entr number")) for i in range(2)]
y=[input("entr name for length") for j in range(2)]

def returnbool(list,list1):
    
    for i in list:
        if i%2==0:
            list[list.index(i)]=True
        else:
            list[list.index(i)]=False
    print(list)
    for j in list1:
        list1[list1.index(j)]=len(j)
    print(list1)
    return list,list1

l=[]
l,m=returnbool(x,y)
print(l,m)


# def returnlength(list1):
#     for i in list1:
#         list1[list1.index(i)]=len(i)
#     return list1

# print(returnlength(y))

