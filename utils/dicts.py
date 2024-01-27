collection = {1: "Меркурий",
              2: "Венера",
              3: "Земля",
              4: "Марс",
              5: "Юпитер",
              6: "Сатурн",
              7: "Уран",
              8: "Нептун"}


def get_val(collection, key, val='noname'):
    try:
        key = int(key)
    except ValueError:
        return ("uncorrect key")
    if key < 0:
        return ("a negative number")
    if 0 < key < 9:
        return collection[key]
    return val


print(get_val(collection, -4))
