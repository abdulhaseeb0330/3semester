products = {
    "Electronics": {"Laptop": 1200, "Phone": 800},
    "Clothes": {"Shirt": 50, "Shoes": 100},
    "Grocery": {"Rice": 20, "Milk": 10}
}
max_price = 0
p_name = ""

for category_items in products.values():
    for name, price in category_items.items():
        if price > max_price:
            max_price = price
            p_name = name


print(p_name+" ", max_price)