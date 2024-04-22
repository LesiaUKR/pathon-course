def wrong_function(numbers_list):
    numbers_sum = 0
    for number in numbers_list:
        numbers_sum += number
    return numbers_sum


print(wrong_function([1, 2, 3, 4, 5]))
