student_name = input("Gloria Arinda")
student_number =input("SEP23/BCS/088U/F")
programming = float(90)
data_science = float(87)
computer_applications = float(77)
marks =[90,87,77]
total_marks = sum(marks)
count = len(marks)
average = total_marks/count
print(f"The average mark is :{average:.3f}")

# Display full details of the student
print(f"The name of the student is {student_name}, student no. is {student_number}, her marks in programming are {programming},in data science she has {data_science},and in computer applications she has {computer_applications}")