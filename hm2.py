"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

import string


def count_most_frequent_words(text, n=10):
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()

    words = text.split()

    word_counts = {}

    for WORD in words:
        if WORD in word_counts:
            word_counts[WORD] += 1
        else:
            word_counts[WORD] = 1

    most_common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]

    return most_common_words


article = """A car or an automobile is a motor vehicle with wheels.
Most definitions of cars say that they run primarily on roads, seat one to eight people,
have four wheels, and mainly transport people, not cargo.
French inventor Nicolas-Joseph Cugnot built the first steam-powered road vehicle in 1769,
while French-born-Swiss inventor François Isaac de Rivaz designed and
constructed the first internal combustion powered automobile in 1808.
The modern car—a practical, marketable automobile for everyday use—was invented in 1886,
when German inventor Carl Benz patented his Benz Patent-Motorwagen.
Commercial cars became widely available during the 20th century.
One of the first cars affordable by the masses was the 1908 Model T, 
an American car manufactured by the Ford Motor Company. Cars were rapidly adopted in the US,
where they replaced horse-drawn carriages. In Europe and other parts of the world,
demand for automobiles did not increase until after World War II.
The car is considered an essential part of the developed economy."""

result = count_most_frequent_words(article)
for word, count in result:
    print(word, count)
