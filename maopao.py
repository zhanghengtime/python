list1 = [12,5,99,43,69,78,41,35,9]
for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if (list1[j] > list1[j+1]):
            l = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = l
print(list1)




