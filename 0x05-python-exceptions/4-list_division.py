#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    answr = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            answr.append(result)
        except ZeroDivisionError:
            print("division by 0")
            answr.append(0)
        except TypeError:
            print("wrong type")
            answr.append(0)
        except IndexError:
            print("out of range")
            answr.append(0)
    return answr
