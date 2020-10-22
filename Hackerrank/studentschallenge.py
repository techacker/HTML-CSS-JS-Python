#if __name__ == '__main__':
#    N = int(input())

#records = [['chi',20.0],['beta',50.0],['alpha',50.0]]

#print(len(records))
#print(records[1][0])

#for inner in records:
#    for value in inner:
#        print(value)

N = int(input())
students = []
final = []

for _ in range(N):
    name = input()
    grade = float(input())
    students.append([name,grade])

students.sort()
print(students)



#for i in range(len(students)):
#    if students[i][1] < students[-1][1]:
#        sortedlist = sortedlist + students[i]
#        print(sortedlist)
#        if sortedlist[0][1] 
        

#sortedlist.sort()

#print(sortedlist)

#for items in sortedlist:
#    for values in items:
#        print(values)


#print(students)
#print(sortedlist)

