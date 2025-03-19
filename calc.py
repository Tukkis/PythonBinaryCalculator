import math

def convert_to_binary(num):
    return bin(num)[2:]


def convert_to_int(binary):
    return int(binary, 2)

def binary_addition(num1, num2):

    num1_str = str(convert_to_binary(num1))
    num2_str = str(convert_to_binary(num2))

    max_length = max(len(num1_str), len(num2_str))
    num1_str = num1_str.zfill(max_length)
    num2_str = num2_str.zfill(max_length)

    reversed_num1 = list(num1_str[::-1])
    reversed_num2 = list(num2_str[::-1])

    result = ''
    carry_over = 0

    for index in range(len(reversed_num1)):
        total = carry_over + int(reversed_num1[index]) + int(reversed_num2[index])
        result += str(total % 2)
        carry_over = total // 2  

    if carry_over:
        result += str(carry_over)
    
    return result[::-1]



def binary_substraction(num1, num2):

    num1_str = str(convert_to_binary(num1))
    num2_str = str(convert_to_binary(num2))

    max_length = max(len(num1_str), len(num2_str))
    num1_str = list(num1_str.zfill(max_length))
    num2_str = list(num2_str.zfill(max_length))

    num1_not_smaller = True
    for index in range(len(num1_str)):
        if int(num1_str[index]) > int(num2_str[index]):
            break
        elif int(num2_str[index]) > int(num1_str[index]):
            num1_not_smaller = False
            break

    if num1_not_smaller:
        reversed_num1 = num1_str[::-1]
        reversed_num2 = num2_str[::-1]
    else:
        reversed_num2 = num1_str[::-1]
        reversed_num1 = num2_str[::-1]

    result = ''
    carry_over = 0

    for index in range(len(reversed_num1)):
        total = int(reversed_num1[index]) - int(reversed_num2[index]) + carry_over
        carry_over = 0
        if total < 0:
            carry_over -= 1
            result += str(total % 2)
        else:
            result += str(total)
    
    if not num1_not_smaller:
        result += "-"

    return result[::-1]

def binary_multiplication(num1, num2):
    num1_str = str(convert_to_binary(num1))
    num2_str = str(convert_to_binary(num2))

    max_length = max(len(num1_str), len(num2_str))

    num1_comparator = list(num1_str.zfill(max_length))
    num2_comparator = list(num2_str.zfill(max_length))

    num1_not_smaller = True
    for index in range(len(num1_str)):
        if int(num1_comparator[index]) > int(num2_comparator[index]):
            break
        elif int(num2_comparator[index]) > int(num1_comparator[index]):
            num1_not_smaller = False
            break

    if num1_not_smaller:
        reversed_num1 = list(num1_str[::-1])
        reversed_num2 = list(num2_str[::-1])
    else:
        reversed_num2 = list(num1_str[::-1])
        reversed_num1 = list(num2_str[::-1])

    addition_rows = min(len(num1_str), len(num2_str)) - 1

    calculation_matrix = []

    calculation_matrix.append(reversed_num1+ ['0']*addition_rows)

    for index in range(1,addition_rows):
        row_digit = (int(reversed_num1[index]) + int(reversed_num2[index])) // 2
        digits_for_row = ''.ljust(max_length, str(row_digit))
        row_to_add = list(digits_for_row.zfill(max_length + index))
        calculation_matrix.append(row_to_add + ['0']*(addition_rows - index))
    
    calculation_matrix.append(['0']*addition_rows + reversed_num1)

    summed_matrix = ['0']*(max_length+addition_rows)

    carry_over = 0

    for  row in calculation_matrix:
        for column_index, column in enumerate(row):
            total = int(summed_matrix[column_index]) + int(column) + carry_over
            carry_over = total // 2 
            summed_matrix[column_index] = str(total % 2)

    result= ''.join(summed_matrix)
    if carry_over:
        result += str(carry_over)

    return convert_to_int(result[::-1])




if __name__ == "__main__":
    print(binary_multiplication(29,9))