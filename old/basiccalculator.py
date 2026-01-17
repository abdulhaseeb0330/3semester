
# # #input in string
# # def inputdata():
# #   x=input("enter a number")
# #   return x
# # #convert string to int
# # def convert_to_int(s):
# #     for i in s:
# #         if i==int():
# #          print(i)

# # print(convert_to_int(inputdata()))



# # list=[1,2,3,4]
# # x=[lambda y:y*y for y in list]
# # print([y for y in x])
# list101=[10,-13,20,-30,-50]
# def trans(list101):
   
#     t=list(map(lambda x:x-1,list101))
#     print(t)

# print(tuple(list101))
# print(max(list101,key=abs))
# list1=["ali","haseeb","zain","ahmed"]
# print(max(list1,key=len))


# def rewpos(list1):
#     even=[]
#     odd=[]
#     for i in list1:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even,odd
# e,o=rewpos([1,2,3,4,5,6,7,8,9])
# print("even",e)
# print("odd",o)


list2=[[1,1],1,1,1,1,1,1,1,1,1,[1,[1,1,1],1]]
# sum=[sum for i in list2 if isinstance(i, list) for j in i if isinstance(j, list) for k in j if isinstance(k, list) sum=sum+k else sum=sum+j continue else sum=sum+i]
# print(sum)
# sum=0
# for i in list2:
#     if isinstance(i,list):
#         for j in i:
#             if isinstance(j,list):
#                 for k in j:
#                     sum=sum+k
#             else:
#                 sum=sum+j
#         continue
#     sum=sum+i
# print(sum)

# list1=[1,[2,[3,4],5],6]

# def sum(l):
#     total = 0
#     for i in l:
#         if isinstance(i,list):
#             total = total +sum(i)
#         else:
#             total = total +i
#     return total


# print(sum(list1))


# products = {
#     "Electronics": {"Laptop": 1200, "Phone": 800},
#     "Clothes": {"Shirt": 50, "Shoes": 100},
#     "Grocery": {"Rice": 20, "Milk": 10}
# }

# maxn = ""
# maxp= 0

# for category, items in products.items():
#     for name, price in items.items():
#         if price > maxp:
#             maxp = price
#             maxn = name

# print(maxn, maxp)



# def count(lst, freq=None):
#     if freq is None:
#         freq = {}
#     for i in lst:
#         if type(i) == list:
#             count(i, freq)
#         else:
#             freq[i] = freq.get(i, 0) + 1
#     return freq

# lst = [1, [2, [3, 2, 4], 5, 1], 6]
# result = count(lst)
# print(result)
 



