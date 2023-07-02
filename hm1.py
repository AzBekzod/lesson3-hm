"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
Пример:
[1, 2, 3, 1, 2, 4, 5] -> [1, 2]
"""


def find_duplicates(num_all):
    unique_nums = set()
    duplicates = set()

    for num in num_all:
        if num in unique_nums:
            duplicates.add(num)
        else:
            unique_nums.add(num)

    return list(duplicates)


nums = [1, 2, 3, 1, 2, 4, 5, 5, 5, 4, 4, 7, 8, 9]
result = find_duplicates(nums)
print(result)
