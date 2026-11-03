# Sum of all numbers in a list

list = [23,46,89,13,490,76]
total = 0
for num in list:
    total += num
    print(total)
    
 # --------- OR ----------
 
total = 0
for i in range(34,67):
    total += i
print("Total : ",total)
    
# Doubling each number in a list

list = ["r","u","i",8,5]
double = []

for letter in list:
    double.append(letter*2)
    
    print(double)
    

list = ["r","u","i",8,5]
double = []

for letter in list:
    double.append(letter*2)

print("doubled :",double)
  
# printing food

food = ["roti","rice","samber","chapati","baji"]

for food in food:
    print("I eat ",food,"food")
    

# iterating over dictionary keys

student_marks = {"Basu" : 89,"Laxmi":78}

for student in student_marks.keys() :
    
    print(student)
    
# iterating over dictionary values

student_marks = {"Basu" : 89,"Laxmi":78}

for marks in student_marks.values() :
    
    print(student)
    
# iterating over both keys and values

student_marks = {"Basu" : 89,"Laxmi":78}

for student,marks in student_marks.items() :
    
    print(student,"scored",marks,"marks")
    
    
student = ["chandan","Basuraj","kavita","Laxmi"]
marks = [89,67,90,79]

student_marks = {}

for index,student in enumerate(student):
    student_marks[student] = marks[index]
    
print(student_marks)
    