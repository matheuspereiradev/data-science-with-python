import numpy as np

data_for_dimensional = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado',
     'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático',
     'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático',
     'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

array_2_dimensional = np.array(data_for_dimensional)
# print(type(array_2_dimensional))
# print(array_2_dimensional.shape)
# print(array_2_dimensional)

year = [2022, 2021, 2020, 2019, 2018]
value = [150, 30, 55, 77, 99]

test = np.array([year, value])
print(test)
print("===")
print(test[:, 1:5])
