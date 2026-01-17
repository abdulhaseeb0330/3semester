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