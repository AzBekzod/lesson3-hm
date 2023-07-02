"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
Верните все возможные варианты комплектации рюкзака.
"""

MAX_LOAD = 10

ITEMS = {
    "палатка": {"weight": 8},
    "удочка": {"weight": 3},
    "фонарик": {"weight": 2},
    "карта": {"weight": 2},
    "продукты": {"weight": 3},
    "вода": {"weight": 4},
    "нож": {"weight": 3},
    "ружьё": {"weight": 7},
    "спички": {"weight": 1},
}


def find_backpack_combinations(items, max_weight):
    backpack_combinations = []
    current_combination = []

    def backtrack(weight, available_items):
        if weight == 0:
            backpack_combinations.append(list(current_combination))
        elif weight < 0:
            return
        else:
            for i in range(len(available_items)):
                item_name, item_props = available_items[i]
                item_weight = item_props["weight"]
                current_combination.append((item_name, item_weight))
                backtrack(weight - item_weight, available_items[i+1:])
                current_combination.pop()

    backtrack(max_weight, items)
    return backpack_combinations


combinations = find_backpack_combinations(list(ITEMS.items()), MAX_LOAD)


for combination in combinations:
    total_weight = sum(item[1] for item in combination)
    print("Комплектация:", combination, "Общий вес:", total_weight)
