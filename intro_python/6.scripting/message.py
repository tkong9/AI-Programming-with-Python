names = list(input("Enter names seperated by commas: ").split(",")) # get and process input for a list of names
assignments = list(input("Enter assignment counts seperated by commas: ").split(",")) # get and process input for a list of the number of assignments
grades = list(input("Enter grades seperated by comma: ").split(",")) # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


# names = ['a', 'b', 'c', 'd']
# assignments = [3, 6, 0, 2]
# grades = [81, 77, 92, 88]
# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(names)):
    print(message.format(names[i], assignments[i], grades[i], int(assignments[i]) * 2 + int(grades[i])))

