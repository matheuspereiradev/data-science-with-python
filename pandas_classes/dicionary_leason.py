dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    },
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

print("acessorios" in dados["Crossfox"])
print(dados["Passat"]["valor"])
print(dados["Passat"]["acessorios"][-1])

dataset = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

for key in dataset.keys():
    avg = dataset[key]["km"] / (2023 - dataset[key]["ano"])
    dataset[key]["media"] = avg
    print(f"{key} = {avg}")

# alternative way to calculate the average KM
for item in dataset.items():
    result = item[1]['km'] / (2023 - item[1]['ano'])
    print(result)
