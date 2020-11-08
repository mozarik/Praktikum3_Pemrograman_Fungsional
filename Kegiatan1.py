from copy import deepcopy


def concat_list(list_a, list_b):
    new_list = []
    for x in range(0, len(list_a)):
        string_gabung = list_a[x] + list_b[x]
        new_list.append(string_gabung)
    return new_list


def ekstrak_value(dict, *args):
    filter_keys = []
    end_list = []
    for arg in args:
        filter_keys.append(arg)
    for x in dict:
        value = list(map(x.get, filter_keys))
        end_list.append(value)
    return sum(end_list, [])


def pertama_z(dict):
    new_dict = deepcopy(dict)
    for x in new_dict:
        x.pop('umur')
        x.pop('pekerjaan')
    return new_dict


def kedua_e(dict):
    dict.pop(1)
    return dict


def ketiga_i(dict):
    new_dict = deepcopy(dict)
    for x in new_dict:
        nama = x.get('nama')
        umur = x.get('umur')
        pekerjaan = x.get('pekerjaan')
        gaji = x.get('gaji')
        print(f'Nama : {nama} \n'
              f'Umur: {umur} \n'
              f'Pekerjaan: {pekerjaan} \n'
              f'Gaji : {gaji}'
              )
        print("---------------------------")


def keempat_n(dict):
    new_value = {'universitas': 'Universitas Muhammadiyah Malang'}
    for x in dict:
        x.update(new_value)
    return dict


def kelima_f(dict):
    for d in dict:
        value = input("Masukan Nama Universitas : ")
        d.update(("universitas", value)
                 for k, v in d.items() if v == "Universitas Muhammadiyah Malang")
    print("input selesai")


def keenam_a(dict):
    new_dict = deepcopy(dict)
    for x in new_dict:
        nama = x.get('nama')
        umur = x.get('umur')
        pekerjaan = x.get('pekerjaan')
        gaji = x.get('gaji')
        universitas = x.get('universitas')
        print(f'Nama : {nama} \n'
              f'Umur: {umur} \n'
              f'Pekerjaan: {pekerjaan} \n'
              f'Gaji : {gaji} \n'
              f'Universitas: {universitas}'
              )
        print("---------------------------")


def ketujuh_h(dict):
    dict[2]["pekerjaan"] = "pengangguran"  # Key 3 Value 4
    dict[0]["umur"] = 69  # Key 2 Value 1
    dict[1]["gaji"] = 100


def kedelapan_r(dict):
    new_dict = deepcopy(dict)
    for x in new_dict:
        nama = x.get('nama')
        umur = x.get('umur')
        pekerjaan = x.get('pekerjaan')
        gaji = x.get('gaji')
        universitas = x.get('universitas')
        print(f'Nama : {nama} \n'
              f'Umur: {umur} \n'
              f'Pekerjaan: {pekerjaan} \n'
              f'Gaji : {gaji} \n'
              f'Universitas: {universitas}'
              )
        print("---------------------------")


def kesembilan_o(dict):
    value = ekstrak_value(dict, 'umur', 'gaji')
    return sum(value)


def kesepuluh_z(dict, *args):
    filter_keys = []
    list_tergabung = []
    for arg in args:
        filter_keys.append(arg)
    for x in dict:
        value = list(map(x.get, filter_keys))
        add_string = value[0] + value[1]
        list_tergabung.append(add_string)
    return list_tergabung
