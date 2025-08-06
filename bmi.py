#bmi
def calculate_bmi():
    while True:
        
        name = input("what is your name: ")
        weight = float(input("input weight"))
        height = float(input("input height"))
        height = height / 100
        bmi = weight / (height**2)

        UNDER_WEIGHT = bmi < 18.5
        HEALTHY_WEIGHT = bmi >= 18.5 and bmi <= 24.9
        OVER_WEIGHT = bmi >= 25 and bmi < 29.9
        OBESITY= bmi >= 30

        try:
            if UNDER_WEIGHT:
                print(f"hi {name}, you are Under weight")
          
            elif HEALTHY_WEIGHT:
                print(f"hi {name}, you are Healty weight")
          
            elif OVER_WEIGHT:
                print(f"hi {name}, you are Over weight")
           
            elif OBESITY:
                print(f"hi {name}, you are Obese")
              
            break
    
        except ValueError:
            print("Invalid input")

calculate_bmi()