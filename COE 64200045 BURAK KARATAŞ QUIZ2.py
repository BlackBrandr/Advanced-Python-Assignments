def maximumElement(L):
    length=len(L)
    if length == 1:
        return L
    elif L[length-1]>=L[length-2]:
        del L[length-2]
    elif L[length-1]<=L[length-2]:
        del L[length-1]
    return maximumElement(L)

list1 = input("Enter the List 1: ").split()
for i in range(len(list1)):
    list1[i] = eval(list1[i])

print (maximumElement(list1))