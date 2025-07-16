grade = int(input("Enter your grade: "))



if grade >= 90 and grade <= 100:
    print("You got an A")
elif grade >= 80 and grade < 90:
    print("You got a B")
elif grade >= 70 and grade < 80:
    print("You got a C")
elif grade >= 60 and grade < 70:
    print("You got a D")
elif grade >= 0 and grade < 60:
    print("You got an F")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")
