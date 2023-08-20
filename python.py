list_1 = [1,10,7,6]
list_2 = [4,7,2]
list_1.extend(list_2)
list_1.sort()
length = len(list_1)
if (length%2 == 0):
    median = (list_1[length//2]+list_1[(length//2)-1])/2
else:
    median = list_1[length//2]
print(median)