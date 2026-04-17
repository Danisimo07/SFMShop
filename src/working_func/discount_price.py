def discount_price(price: int, dicsount: int) -> float:
    dsc = 1 - dicsount / 100
    result = price * round(dsc, 2)
    return result


print(
    f"Цена на товар 1 со скидкой: {discount_price(1000, 10)}",
    f"Цена на товар 2 со скидкой: {discount_price(5000, 15)}",
    sep='\n'
)
