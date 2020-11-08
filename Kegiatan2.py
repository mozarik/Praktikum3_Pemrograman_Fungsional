from pprint import pprint
from collections import OrderedDict

data = [{'nama': 'Zein', 'jurusan': 'Informatika', 'semester': '2', 'angkatan': ''},
        {'nama': '', 'jurusan': 'Pertanian', 'semester': '', 'angkatan': '2017'},
        {'nama': 'Insan', 'jurusan': '', 'semester': '3', 'angkatan': ''},
        {'nama': 'Malik', 'jurusan': '', 'semester': '', 'angkatan': '2018'},
        {'nama': '', 'jurusan': 'Kehutanan', 'semester': '', 'angkatan': '2015'}]
data2 = {'nama': 'Zein', 'jurusan': 'Informatika',
         'semester': '2', 'angkatan': ''}

# OrderedDict(data)

# for dictionary in data:
#     index = 1
#     for d in dictionary:
#         value = input(f"Masukan data pada baris dictionary {d}: ")
#         d.update((k, value) for k, v in d.items() if v == '')
#     index += 1


for x in data:
    for k, v in x.items():
        if v == '':
            inputan = input(f"Masukan data pada baris dictionary {k}: ")
            x.update((k, inputan) for k, v in x.items() if v == '')

pprint(data)
