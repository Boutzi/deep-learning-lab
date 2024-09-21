def load_data_1():
    training_name = "x_by_2"
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
    output_data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 200]
    return training_name, input_data, output_data

def load_data_2():
    training_name = "x_by_3"
    input_data = [1, 2, 3, 4, 5]
    output_data = [3, 6, 9, 12, 15]
    return training_name, input_data, output_data

def load_data_3():
    training_name = "celcius_to_fahrenheit" # °F = °C × (9/5) + 32
    input_data = [0, 1, 2, 3, 5, 10, 100]
    output_data = [32, 33.8, 35.6, 37.4, 41, 50, 212]
    return training_name, input_data, output_data

