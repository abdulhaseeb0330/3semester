products = {
    "Electronics": {"Laptop": 120000, "Phone": 336155},
    "Clothes": {"pent": 800, "colar": 50},
    "Grocery": {"cherry": 2000, "grain": 1000}
}
max_price = 0
p_name = ""

for category_items in products.values():
    for name, price in category_items.items():
        if price > max_price:
            max_price = price
            p_name = name



print(p_name+" ", max_price)
