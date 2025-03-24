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



def binary_substraction(num1, num2, already_bin):

    if not already_bin:
        num1_str = str(convert_to_binary(num1))
        num2_str = str(convert_to_binary(num2))
    else:
        num1_str = num1
        num2_str = num2

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

    summed_matrix = ['0']*(max_length+addition_rows)

    for num2_index in range(len(reversed_num2)):
        for num1_index in range(len(reversed_num1)): 
            total = int(reversed_num2[num2_index]) +  int(reversed_num1[num1_index])
            summed_matrix[num1_index + num2_index] = int(summed_matrix[num1_index + num2_index]) + total // 2

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

    return result[::-1]


def binary_division(num1, num2):
    num1_str = str(convert_to_binary(num1))
    num2_str = str(convert_to_binary(num2))

    if num2_str == '1':
        return num1_str
    elif num2_str == '0':
        return '0'

    comparator = ''

    result = ''

    for num1_index in range(len(num1_str)):
        comparator += num1_str[num1_index]
        comparator_not_smaller = True
        for index in range(len(num2_str)):
            if len(comparator) < len(num2_str   ):
                comparator_not_smaller = False
                break
            elif int(comparator[index]) > int(num2_str[index]):
                break
            elif int(num2_str[index]) > int(comparator[index]):
                comparator_not_smaller = False
                break
            elif index == len(num1_str) - 1:
                comparator_not_smaller = False
        if comparator_not_smaller:
            comparator = binary_substraction(comparator, num2_str, True)
            result += '1'
        else:
            result += '0'
        comparator = comparator.lstrip('0')

    return convert_to_int(result)
            


if __name__ == "__main__":
    print(binary_division(10, 2))   # Expected: 5
    print(binary_division(100, 2))  # Expected: 50
    print(binary_division(15, 3))   # Expected: 5
    print(binary_division(8, 4))    # Expected: 2
    print(binary_division(10, 1))   # Expected: 10
    print(binary_division(1, 1))    # Expected: 1
    print(binary_division(0, 1))    # Expected: 0
    print(binary_division(50, 5))   # Expected: 10
    print(binary_division(81, 9))   # Expected: 9
    print(binary_division(1000, 10))# Expected: 100
    print(binary_division(7, 2))    # Expected: 3
