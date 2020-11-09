from pprint import pprint
from collections import OrderedDict

isi = [{'nama': 'Zein', 'jurusan': 'Informatika', 'semester': '2', 'angkatan': ''},
       {'nama': '', 'jurusan': 'Pertanian', 'semester': '', 'angkatan': '2017'},
       {'nama': 'Insan', 'jurusan': '', 'semester': '3', 'angkatan': ''},
       {'nama': 'Malik', 'jurusan': '', 'semester': '', 'angkatan': '2018'},
       {'nama': '', 'jurusan': 'Kehutanan', 'semester': '', 'angkatan': '2015'}]

# OrderedDict(data)

# for dictionary in data:
#     index = 1
#     for d in dictionary:
#         value = input(f"Masukan data pada baris dictionary {d}: ")
#         d.update((k, value) for k, v in d.items() if v == '')
#     index += 1


# for x in data:
#     for k, v in x.items():
#         if v == '':
#             inputan = input(f"Masukan data pada baris dictionary {k}: ")
#             x.update((k, inputan) for k, v in x.items() if v == '')

for i in range(len(isi)):
    if isi[i]['angkatan'] == '':
        k1 = input(isi[i]['nama'] + ' Angkatan Tahun Berapa :')
        isi[i]['angkatan'] = k1

for i in range(len(isi)):
    if isi[i]['nama'] == '':
        k1 = input('Jurusan ' + isi[i]['jurusan'] + ' Siapa :')
        isi[i]['nama'] = k1

for i in range(len(isi)):
    if isi[i]['jurusan'] == '':
        k1 = input(isi[i]['nama'] + ' Jurusan apa :')
        isi[i]['jurusan'] = k1

for i in range(len(isi)):
    if isi[i]['semester'] == '':
        k1 = input(isi[i]['nama'] + ' Semester Berapa :')
        isi[i]['semester'] = k1

for j in range(len(isi)):
    print(isi[j])

# for i in range(len(data)):
#     if data[i]['angkatan'] == '':
#         k1 = input(data[i]['nama'] + ' Angkatan Tahun Berapa :')
#         data[i]['angkatan'] = k1

# pprint(isi)
