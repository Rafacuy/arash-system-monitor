# Utils/misc.py

def update_data_array(data_array, new_value, max_length):
    data_array.append(new_value)
    if len(data_array) > max_length:
        data_array.pop(0)
