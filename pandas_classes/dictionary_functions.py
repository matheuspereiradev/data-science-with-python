cars = ("Jetta", "Pollo", "Onix")
prices = (75000, 25000, 35500)

# create an dictionary by tuples
dic = dict(zip(cars, prices))
print(dic)

print(dic["Pollo"])

print("Pollo" in dic)

# add new data to dicionary
dic["Fusca"] = 15420
print(dic)

# remove an data to dicionary
del dic["Onix"]
print(dic)

dic["Pollo"] = 50003
print(dic)

# two ways to use update
dic.update({"Prisma": 1500, "Palio": 3541, "Jetta": 60000})
dic.update(Pollo=1500, Passat=80000)
print(dic)

# remove
dic.pop("Cobalt", "NOT FOUND")

for key in dic.keys():
    print(f"CARRO: {key} => {dic[key]} R$")

# show the values
print(dic.values())

for item in dic.items():
    print(item)

print(sum(list(dic.values())))
