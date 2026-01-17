# list=["apple","banana","cherry"]
# a=None
# # list automatically unpacked with variables using loop
# for x in list:
#     a=x
#     print(a)




def con(str,vowels):
    lis=[]
    for x in str:
        if(x in vowels):
            lis.append(x)
    return lis

list1=['l','pyhton','ali']
print(con(list1,"aeiouAEIOU"))