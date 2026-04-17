def sum_all(*args: int) -> int:
    total = 0
    for elem in args:
        total += elem
    return total

sum_two_numbers = sum_all(1000, 2000)
sum_five_numbers = sum_all(1000, 2000, 800, 900, 200)
sum_not_arguments = sum_all()

print(
    f"Сумма двух чисел: {sum_two_numbers}",
    f"Сумма пяти чисел: {sum_five_numbers}",
    f"Сумма без аргументов: {sum_not_arguments}",
    sep='\n'
)
