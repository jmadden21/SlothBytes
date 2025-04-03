def bridge_shuffle(list1, list2):
    shuffled = []
    for i in range(len(list1)):
        shuffled.append(list1[i])
        shuffled.append(list2[i])
    return shuffled


list1 = ['A', 'A', 'A']
list2 = ['B', 'B', 'B']
print(bridge_shuffle(list1, list2))