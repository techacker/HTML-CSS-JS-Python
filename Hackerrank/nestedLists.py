# Nested Lists - Hackerank Practice Challenge
'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
'''

students = {}
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score

# The scores can be captured in a list using key, value properties of dictionary.
scores = students.values()

# Set removes duplicates from a list. Then sorting the set puts the second lowest as list[1]
second_score = sorted(set(scores))[1]

# Empty list to capture names of second lowest grades
secondLowestStudents = []

for name, score in students.items():
    if score == second_score:
        secondLowestStudents.append(name)

# Create a list of second lowest score names and sort it.
secondLowestStudents.sort()

for name in secondLowestStudents:
    print(name)


    

