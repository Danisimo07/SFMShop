def check_stock_availability(stock_quantity: int, required_quantity: int) -> True | False:
    return True if stock_quantity >= required_quantity else False

# stock_quantity = int(input("Введите запасное кол-во: "))
# required_quantity = int(input("Введите необходимое кол-во: "))

# final = check_stock_availability(stock_quantity, required_quantity)

# print(f"Результат: {final}")