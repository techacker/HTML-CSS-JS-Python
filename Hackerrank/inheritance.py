# Day 12: Inheritance
# Task
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
# Observe that Student inherits all the properties of Person.
# Complete the Student class by writing the following:
#
# A Student class constructor, which has 4 parameters:
# A string, firstName .
# A string, lastName.
# An integer, id.
# An integer array (or vector) of test scores, scores .
# A char calculate() method that calculates a Student object's average and returns 
# the grade character representative of their calculated average:

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, fName, lName, idNumber, score):
        Person.__init__(self, firstName, lastName, idNumber)
        # We can also use super():
        # super().__init__(self, firstName, lastName, idNumber)
        self.score = score
    
    def calculate(self):
        total = 0
        for i in range(len(self.score)):
            total += self.score[i]
        average = total / (len(self.score))
        if average < 40:
            return 'T'
        elif average >= 40 and average < 55:
            return 'D'
        elif average >= 55 and average < 70:
            return 'P'
        elif  average >= 70 and average < 80:
            return 'A'
        elif average >=80 and average < 90:
            return 'E'
        elif average >= 90 and average <= 100:
            return 'O'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

