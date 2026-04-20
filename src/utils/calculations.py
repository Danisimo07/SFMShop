def calculate_discount(price: int, discount_rate: int) -> float:
    discount = discount_rate / 100
    discount_product = round(price * discount, 2)
    return discount_product

def calculate_delivery(weight, base_cost: int = 100) -> None:
    return base_cost + (weight * 10)

def calculate_final_price(price: int, discount: int, weight: int) -> float:
    discount = round(discount / 100, 2)
    final_cost = price - discount + weight
    return final_cost