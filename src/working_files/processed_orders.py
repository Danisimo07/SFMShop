try:
    with open("orders.txt", 'r', encoding='utf-8') as infile:
        orders = infile.readlines()

    count = 0
    total = 0
    for line in orders:
        line = line.strip()
        parts = line.split(':')
        if len(parts) == 3 and parts[2] == 'новый':
            total += int(parts[1])
            count += 1

    with open("working_files/processed_orders.txt", 'w', encoding='utf-8') as outfile:
        outfile.write(f"Обработано заказов: {count}\n")
        outfile.write(f"Общая сумма: {total} руб.\n")

    print("✅ Готово!")

except FileNotFoundError:
    print("❌ working_files/orders.txt не найден")
except Exception:
    print("❌ Ошибка")