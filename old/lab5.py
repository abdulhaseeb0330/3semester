# def check(inputdata):
#     for i in range(len(inputdata)):
#         if inputdata[i] % 2 == 0:
#             inputdata[i] = True
#         else:
#             inputdata[i] = False
#     return inputdata

# inputdata =[1,2,3,9,10,15]
# a=check(inputdata)
# print(a)



# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def countprimes(numbers):
#     count = 0
#     for num in numbers:
#         if isprime(num):
#             count += 1
#     return count

# list1 = [1, 2, 3, 4, 5]
# print(countprimes(list1))


# def prime(a):
#     list1 =a
#     count=0
#     for i in range(len(list1)):
#         for j in range(2,list1[i]):
#             if list1[i] % j ==0:
#                 count=count+1
#                 break
#     return count

#     # for i in range(len(list)):
#     #     if list[i] %list[i]==0:
#     #         count=count+1
          
          


# list1=[1,2,3,4,5]
# prime(list1)

def strin(list,t):
    # count of vowel words atleast having 2 vowels
    count=0
    for i in range(t):
        if 'aeiouAEIOU' in list[i]:
            count=count+1
            if count>=2:
                break
    return count
lists=["ahmed","ali","umar","hassan"]
t=len(lists)
a=strin(list,t)
# print(a)