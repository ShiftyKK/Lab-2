def display_main_menu():
    print("Enter some numbers separated by commas e.g. 5, 67, 32")

def get_user_input():
    inp = input()
    x = inp.split(',')
    float_list = [float(y) for y in x]
    return float_list

def calc_average(float_list):
    total = sum(float_list)
    avg = total / len(float_list)
    print("Average is: " + str(avg))  # Convert avg to a string

def find_min_max(float_list):
    min_val = min(float_list)
    max_val = max(float_list)

    print("Minimum is: " + str(min_val))  # Convert min_val to a string
    print("Maximum is: " + str(max_val))  # Convert max_val to a string

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    user_input = get_user_input()
    calc_average(user_input)  # Pass the user_input list as an argument
    find_min_max(user_input)

if __name__ == "__main__":
    main()
