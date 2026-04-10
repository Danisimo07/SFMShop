"""
    Расширение обработки имён
"""

name_1 = "  Иван    "
name_2 = "мария"
name_3 = " пЕТР  "
name_4 = "АННА"
name_5 = " олег "

print(
    name_1.strip().capitalize(),
    name_2.strip().capitalize(),
    name_3.strip().capitalize(),
    name_4.strip().capitalize(),
    name_5.strip().capitalize(),
    sep='\n'
    )