try:
    marks1 = int(input("Enter marks for subject 1: "))
    marks2 = int(input("Enter marks for subject 2: "))
    marks3 = int(input("Enter marks for subject 3: "))
    marks4 = int(input("Enter marks for subject 4: "))

    average_marks = (marks1 + marks2 + marks3 + marks4) / 4
    if average_marks > 80:
        print("Student type: Outstanding student")
    elif average_marks > 70:
        print("Student type: Normal student")
    else:
        print("Student type: Lazy student")

except ValueError:
    print("Invalid input. Please enter integer marks.")
