def describe_product(name: str, **kwargs):
    result = name + ' ('
    first = True

    for key, value in kwargs.items():
        if not first:
            result += ', '
        result += str(key) + ': ' + str(value)
        first = False

    result += ')'
    return result

print(describe_product("Ноутбук", цена=50000, бренд="Lenovo", вес=2.1))
print(describe_product("Мышь", цвет="черный"))
print(describe_product("Клавиатура"))
