def fizzbuzz():
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def arr_sort():
    list1 = [1,4,6]
    list2 = [11, 33, 22]
    result = sorted(list1, key=lambda x: list2[list1.index(x)])
    print(result)


def check_similar(str_list):
    char_names = [set(word) for word in str_list]
    common_chars = set.intersection(*char_names)
    result = []
    for char in common_chars:
        min_count = min([word.count(char) for word in str_list ])
        result.extend([char] * min_count)
    print(result)


def roman_nums(num):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    previous_num = 0
    for i in num[::-1]:
        current_num = roman_dict[i]
        if current_num < previous_num:
            result -= current_num
        else:
            result += current_num
        previous_num = current_num

    print(f"Результат равен: {result}")


if __name__ == "__main__":
    print("Первое задание:")
    fizzbuzz()
    print("Второе задание:")
    arr_sort()
    print("Третье задание:")
    list_1 = ["bella", "label", "roller"]
    list_2 = ["cool", "lock", "cook"]
    check_similar(list_1)
    check_similar(list_2)
    print("Четвёртое задание:")
    roman_nums(input("Введите римское число: "))


