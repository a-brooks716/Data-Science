name = str(input("Enter your name: "))
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = (weight *730) / (height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name+", you are underweight.")
    
    elif (BMI<=24.9):
        print(name+ ", you are a normal weight.")
   
    elif (BMI<29.9):
        print(name + ", you are over weight.")
    
    elif (BMI<34.9):
        print(name+ ", you are obese.")

    elif (BMI>39.9):
        print(name+ ", you are severly obese.")
    
    else: 
        print("Enter valid input")
