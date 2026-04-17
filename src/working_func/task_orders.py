from func_orders import calculate_order_total, check_stock_availability, format_order_info

stock = 10
required = 3
order_id = 1
price = 1000
quantity = 3
discount = 10

if check_stock_availability(stock, required):
    total = calculate_order_total(price, quantity, discount)
    print(
        f"Товар доступен: {check_stock_availability(stock, required)}",
        f"Инфомация о заказе: {format_order_info(order_id, total)}",
        sep='\n'
    )
else:
    print("Товара нет")
