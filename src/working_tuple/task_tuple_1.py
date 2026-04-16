x = round(float(input("Введите координаты X: ")), 4)
y = round(float(input("Введите координаты Y: ")), 4)

maps = {}

# Распоковка координат
coordinates = (x, y)

cor_x, cor_y = coordinates

# Добавление координат в словарь
maps["coordinates"] = {
    'Координата X': cor_x,
    'Координата Y': cor_y,
    'Название места': 'Офис'
}

for key, place_info in maps.items():
    print(
        f"Ключ: {key}",
        f"Координата X: {place_info['Координата X']}",
        f"Координата Y: {place_info['Координата Y']}",
        f"Название места: {place_info['Название места']}",
        sep='\n'
    )

def find_place_by_coordinates(x_cor, y_cor):
    for place_key, place_info in maps.items():
        if (round(place_info['Координата X'], 4) == round(x_cor, 4) and
            round(place_info['Координата Y'], 4) == round(y_cor, 4)):
            return place_info['Название места']
        return "Не найдено"

print(f"\n🔍 Поиск по координатам ({x}, {y}):")
result = find_place_by_coordinates(x, y)
print(f"Найдено: {result}")
