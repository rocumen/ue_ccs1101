


def age():
    
    while True:

        try:

            choice = int(input("Enter your age: "))\
            
            if choice < 0:
                print("Age must be more than 0")
                continue
            
            print(f"Your age is {choice}")
            break
    
        except ValueError:
            print("Invalid input, must number")
            continue
