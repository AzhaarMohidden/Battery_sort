# a = [(25 , 2), (45 , 1), (78 , 4), (56 , 7), (78 , 4)]
a = [[25 , 2], [45 , 1], [78 , 4], [56 , 7], [78 , 4]]
def takeSecond(elem):
    return elem[1]

print('Unsorted', a)
# a.sort(key=takeSecond)
a.sort(key=takeSecond)
print("Sorted" , a)
