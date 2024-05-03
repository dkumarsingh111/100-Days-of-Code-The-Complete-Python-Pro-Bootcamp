student_heights = input().split()

noOfStudents = 0
total_height = 0
average_height = 0

for n in range(0, len(student_heights)):
    total_height += int(student_heights[n])
    noOfStudents += 1
    
average_height = round(total_height / noOfStudents)

print(f"Total Height = {total_height}")
print(f"No of Students = {noOfStudents}")
print(f"Average Height = {average_height}")