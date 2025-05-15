#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Divides two lists element by element
    new_list = []
    # Loop through the range of the list length
    for i in range(list_length):
        # Try to divide the elements at index i of both lists
        try:
            # Check if the index is within the range of the lists
            result = my_list_1[i] / my_list_2[i]
            # If the index is valid, append the result to the new list
            new_list.append(result)
        # If the index is out of range, catch the IndexError
        except TypeError:
            # Append 0 to the new list and print an error message
            new_list.append(0)
            # Print an error message for wrong type
            print("wrong type")
        except ZeroDivisionError:
            # Append 0 to the new list and print an error message
            new_list.append(0)
            # Print an error message for division by zero
            print("division by 0")
        # If the index is out of range, catch the IndexError
        except IndexError:
            # Append 0 to the new list and print an error message
            new_list.append(0)
            # Print an error message for out of range
            print("out of range")
        finally:
            print("processing done for index {}".format(i))
    # Return the new list containing the results of the division
    return new_list
