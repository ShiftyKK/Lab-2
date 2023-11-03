def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print("Your BMI is " + str(bmi))

    if (bmi >25):
        print("You are Overweight")
        return 1
    elif (bmi < 18.5):
        print("You are Underweight")
        return -1
    else:
        print("You have a normal weight")
        return 0

calculate_bmi(weight=124, height=1.73)