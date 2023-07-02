baggage = {
    'Denis': ('fishing rod', 'lighter', 'tent'),
    'Alex': ('tent', 'brazier', 'gun'),
    'Vlad': ('tent', 'gun', 'sun cream')
}
all_items = list(baggage.values())
must_have_item = set(all_items[0])
for items in all_items:
    must_have_item = must_have_item.intersection(set(items))
print("Вещи, которые взяли все три друга:", must_have_item)

uniq_items = {}
for name, items in baggage.items():
    uniq_items[name] = set(items).difference(must_have_item)
print("Уникальные вещи каждого друга:", uniq_items)

missing_items = {}
for name, items in baggage.items():
    missing_items[name] = set.intersection(*[uniq_items[friend] for friend in baggage if friend != name])
for name, items in missing_items.items():
    if items:
        print("Вещи, которые есть у всех друзей кроме одного:", name, items)
