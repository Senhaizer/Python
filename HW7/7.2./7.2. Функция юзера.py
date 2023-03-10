from User_interface_module import get_user_data

def index_maker(parameters: tuple) -> tuple[tuple]:
    (strings_number, columns_number) = parameters
    indexes_list = []
    for i in range(1, strings_number + 1):
        for j in range(1, columns_number + 1):
            index = (i, j)
            indexes_list.append(index)

    result = indexes_list
    return result

def print_operation_table(indexes: list, parameters: tuple, f) -> tuple[int]:
    elements_list = []
    (strings_number, columns_number) = parameters
    for element in indexes:
        element = f(element[0], element[1])
        elements_list.append(element)

    result = elements_list
    for i in range(strings_number):
        lower_border = columns_number * i
        upper_border = columns_number * i + columns_number
        i += 1
        print()
        for j in range(lower_border, upper_border):
            print(f"{elements_list[j]:^4}", end="")

    return result

message_for_user_1 = 'Укажите количество строк матрицы: '
message_for_user_2 = 'Укажите количество столбцов матрицы: '
list_of_messages = message_for_user_1, message_for_user_2
user_parameters = get_user_data(messages=list_of_messages)
indexes_list = index_maker(parameters=user_parameters)
element_calculate = lambda x, y: x * y
array2d_elements = print_operation_table(indexes=indexes_list, parameters=user_parameters, f=element_calculate)
