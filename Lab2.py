def display_main_menu():
    print("Enter some temperatures separated by commas e.g. 5.6, 3.2, 7.8")

def get_user_input():
    inp = input()
    x = inp.split(',')
    float_list = [float(y) for y in x]
    return float_list

def calc_average(float_list):
    total = sum(float_list)
    avg = total / len(float_list)
    print("Average is: " + str(avg))

def find_min_max(float_list):
    min_val = min(float_list)
    max_val = max(float_list)

    print("Minimum is: " + str(min_val))
    print("Maximum is: " + str(max_val))

def sort_temperature(float_list):
    sorted_temperatures = sorted(float_list)
    print("Temperatures sorted in ascending order:", sorted_temperatures)
    return sorted_temperatures

def calc_median_temperature(sorted_temperatures):
    n = len(sorted_temperatures)
    if n % 2 == 0:
        # If the number of temperatures is even, calculate the median as the average of the middle two temperatures
        middle1 = sorted_temperatures[n // 2 - 1]
        middle2 = sorted_temperatures[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the number of temperatures is odd, the median is the middle temperature
        median = sorted_temperatures[n // 2]

    print("Median temperature is:", median)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    user_input = get_user_input()
    calc_average(user_input)
    find_min_max(user_input)
    sorted_temperatures = sort_temperature(user_input)
    calc_median_temperature(sorted_temperatures)

if __name__ == "__main__":
    main()
