#student grading and attendance system
#ask for abesents 
#if 5 or more absents = f
#1. ask user if what is his grade (0-100) 
#if below 60 = f
#if 60-69 = d
#if 70-79 = c
#if 80-89 = b
#if 90-100 = a

#if student gets a,b,c and abesents below 5 = pass
#if student gets 
#3 outputs
#fail for absents
#fail for grade
#remarks

#do it inside while 
#if stop print the grade and pass
#switch statement
#if a = excellent {remark}
#if b = good job
#if c = needs improvement
#if d = on probation
#if f = failed
#default = invalid grade


#remarks

# student grading and attendance system

import sys  # Import the sys module to use sys.exit()

def grading_system():
    while True:
        try:
            grade = int(input("what is the student grade? "))
            if grade > 100:
                print("invalid grade")
                continue
            elif grade < 0:
                print("invalid grade")
                continue
            absent = int(input("how many absents? "))
            remark = ""
            

            if absent >= 5:
                print("Fail for absents")
                remark = "f"
            else:
                if grade >= 90 and grade <= 100:
                    print("Grade: A")
                    print("remarks: Excellent")
                    remark = "a"
                    grade_equivalent = "Grade: A"
                    
                elif grade >= 80 and grade <= 89:
                    print("Grade: B")
                    print("remarks: Good Job")
                    remark = "b"
                    grade_equivalent = "Grade: B"
                    
                elif grade >= 70 and grade <= 79:
                    print("Grade: C")
                    print("remarks: Needs improvement")
                    remark = "c"
                    grade_equivalent = "Grade: C"
                    
                elif grade >= 60 and grade <= 69:
                    print("Grade: D")
                    print("remarks: On probation")
                    remark = "d"
                    grade_equivalent = "Grade: D"
                    
                elif grade < 60:
                    print("Grade: F")
                    print("remarks: failing grade")
                    remark = "f"
                    grade_equivalent = "Grade: F"
                    
                else:
                    print("Invalid grade")
                    continue
        except ValueError:
            print("no letters or character, number from 0-100 only")
            continue
       

        def remarks(rem):
            match rem:
                case "a":
                    print (f"remarks: Excellent")
                case "b":
                    print (f"remarks: Good Job")
                case "c":
                    print (f"remarks: needs improvement")
                case "d":
                    print (f"remarks: on probation")
                case "f":
                    print (f"remarks: failing grade")
        
        #print(f"You have a grade of {grade}\nremarks {remarks(remark)}")
        
        try:
            while True:
                choice = input("Do you still want to use the grading system? (yes or no only): ").lower()

                if choice == "yes":
                    break
                elif choice == "no":
                    remarks(remark)
                    print(grade_equivalent)
                    sys.exit()  # Exit the program
                else:
                    print("Yes or no only")
                    continue
        except ValueError:
            print("Yes or no only")
            
        
        
                
        
            
grading_system()
