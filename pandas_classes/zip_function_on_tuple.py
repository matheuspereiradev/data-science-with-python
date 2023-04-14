cars = ("Jetta", "Pollo", "Onix")
prices = (75000, 25000, 35500)

# create an list by tuples
print(list(zip(cars, prices)))

for item in zip(cars, prices):
    print(f"CAR: {item[0]} PRICE: {item[1]}")

for car, price in zip(cars, prices):
    if price > 30000:
        print(f"{car} => {price}")
