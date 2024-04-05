list1 = [[1, 2, 3, 4], [6, 7, 8]]
'''
print(list1[1][2])

print("____________________")

for List in list1:
    for tak in List:
        print(tak)

print("____________________")

copy = [[print(f) for f in s] for s in list1]
# print(copy)
'''

#copy = [[print(v) for v in c] for c in list1]

#print(copy)

new = [[v for v in range(1, 3)] for c in range(1, 4)]

print(new)