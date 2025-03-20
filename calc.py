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

    for num2_index in range(len(reversed_num2)):
        row_to_add = []
        for num1_index in range(len(reversed_num1)): 
            total = int(reversed_num2[num2_index]) +  int(reversed_num1[num1_index])
            row_to_add.append(total // 2)
        filler = [0] * num2_index 
        filler.extend(row_to_add)
        calculation_matrix.append(filler)

    summed_matrix = ['0']*(max_length+addition_rows)

    for row_index, row in enumerate(calculation_matrix):
        padding = (addition_rows - row_index)*[0]
        row.extend(padding)
        for column_index, column in enumerate(row):
            summed_matrix[column_index] = str(int(summed_matrix[column_index]) + int(column))

    carry_over = 0

    result = ''

    for col in summed_matrix:
        value = int(col) + carry_over
        carry_over = value // 2 
        result += str(value % 2)

    while carry_over > 1:
        carry_over = carry_over // 2
        result += str(carry_over % 2)

    if carry_over:
        result += str(carry_over)

    return convert_to_int(result[::-1])




if __name__ == "__main__":
    print(binary_multiplication(5, 3))    # Expected output: 15
    print(binary_multiplication(12, 4))   # Expected output: 48
    print(binary_multiplication(7, 7))    # Expected output: 49
    print(binary_multiplication(19, 6))   # Expected output: 114
    print(binary_multiplication(25, 25))  # Expected output: 625
    print(binary_multiplication(50, 10))  # Expected output: 500
    print(binary_multiplication(100, 100))# Expected output: 10000
    print(binary_multiplication(255, 2))  # Expected output: 510
    print(binary_multiplication(128, 8))  # Expected output: 1024
    print(binary_multiplication(17, 13))  # Expected output: 221