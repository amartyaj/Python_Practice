#!/usr/bin/env python3


def calc_output(my_list):
    result = []

    my_list = [str(x) for x in my_list]
    my_list_bkp = my_list.copy()

    for num in my_list:
        my_list_bkp.remove(num)
        result_element = "*".join(my_list_bkp)
        result.append(result_element)
        my_list_bkp = my_list.copy()

    final_result = ",".join(result)
    print(final_result)

    return


if __name__ == "__main__":
    print("Test")

    my_input = [2, 6, 3, 7]
    calc_output(my_input)
