# #CAPSTONE 1 - ARMAND

from tabulate import tabulate

list_karyawan = [
    {'ID Karyawan': 1001 ,
     'Nama'       : 'Mikael',
     'Departemen' : 'Marketing',
     'Umur'       : '26',
     'Domisili'   : 'Jakarta'},

    {'ID Karyawan': 1002 ,
     'Nama'       : 'Arnold', 
     'Departemen' : 'Procurement',
     'Umur'       : '29',
     'Domisili'   : 'Jakarta'},

    {'ID Karyawan': 1003 ,
     'Nama'       : 'Karen', 
     'Departemen' : 'Production',
     'Umur'       : '32',
     'Domisili'   : 'Jakarta'},

    {'ID Karyawan': 1004 ,
     'Nama'       : 'Brian', 
     'Departemen' : 'Finance',
     'Umur'       : '35',
     'Domisili'   : 'Jakarta'}
    
    ]

def isDigit(angka):
    return angka.isdigit()

def inputAngka(teks):
    userInput=input(teks)
    while not isDigit(userInput):
        print('Input harus Angka. Coba lagi!')
        userInput=input(teks)
    return userInput


## MENU UTAMA

def main_menu() :
    input_menu = input('''---------------------------------------------
SELAMAT DATANG DI PORTAL KARYAWAN PT.JCDS
          
Menu :
1. Menampilkan Data Karyawan
2. Menambah Data Karyawan
3. Merubah Data Karyawan
4. Menghapus Data Karyawan    
5. Keluar Aplikasi

Masukkan menu yang ingin dijalankan: ''')

    return input_menu

## READ
def readData() :
    while True :
        menu1 = input('''----------------------
Data Karyawan

Menu:
1. Tampilkan seluruh karyawan
2. Tampilkan karyawan berdasarkan ID
3. Kembali ke menu utama

Masukkan menu yang ingin dijalankan: ''')
            
        if menu1 == '1' :
            if list_karyawan == [] :
                print('\nTidak ada data')
            elif list_karyawan != []:
                headers = ['ID Karyawan', 'Nama', 'Departemen', 'Umur', 'Domisili']
                rows = [[karyawan[field] for field in headers] for karyawan in list_karyawan]
                print('\n')
                print('SELAMAT DATANG DI PORTAL KARYAWAN PT.JCDS'.center(63, '-'))
                print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))

        if menu1 == '2':
            if not list_karyawan:
                print('\nTidak ada data')
            else:
                while True:
                    ID_inp = inputAngka('Masukkan ID karyawan: ')
                    if ID_inp.isdigit():
                        ID_inp = int(ID_inp)
                        if ID_inp >= 1000:
                            break
                        else:
                            print('Mohon masukkan angka di atas 1000')
                    else:
                        print('Mohon masukkan angka yang valid')

                ID_list = [karyawan['ID Karyawan'] for karyawan in list_karyawan]

                if ID_inp in ID_list:
                    headers = ['ID Karyawan', 'Nama', 'Departemen', 'Umur', 'Domisili']
                    for karyawan in list_karyawan:
                        if karyawan['ID Karyawan'] == ID_inp:
                            rows = [[karyawan['ID Karyawan'], karyawan['Nama'], karyawan['Departemen'], karyawan['Umur'], karyawan['Domisili']]]
                            print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
                            break
                else:
                    print('\nTidak ada data')
        elif menu1 == '3' :
            break

## CREATE 
        
def createData() :
    while (True) :
        menu2 = input('''---------------------
Menambah Data Karyawan

Menu:
1. Menambah karyawan
2. Kembali ke menu utama

Masukkan menu yang ingin dijalankan: ''')

        if menu2 == '1':
            while True:
                add_ID = inputAngka('Masukkan ID karyawan : ')
                if add_ID.isdigit():
                    add_ID = int(add_ID)
                    if add_ID >= 1000:
                        if add_ID not in [karyawan['ID Karyawan'] for karyawan in list_karyawan]:
                            break
                        else:
                            print('ID karyawan sudah ada')
                    else:
                        print('Mohon masukkan angka di atas 1000')
                else:
                    print('Mohon masukkan angka yang valid')

            ID_list = []
            for i in list_karyawan:
                ID_list.append(i['ID Karyawan'])
                        
            if add_ID in ID_list:
                print('ID karyawan sudah ada')

            else :    
                add_Nama = input('Masukkan nama karyawan : ')
                add_Departemen = input(''' 
Departemen:
1. Marketing
2. Production
3. Finance
4. Procurement

Masukkan Nama Departemen : ''')
                while True:
                    add_Umur = inputAngka('Masukkan umur karyawan : ')
                    if 18 <= int(add_Umur) <= 60:
                        break
                    else:
                        print('Mohon masukkan umur antara 18 dan 60')

                add_Domisili = input('Masukkan domisili karyawan : ')
                while (True) :
                    save = input('Apakah anda yakin untuk menyimpan data? (ya/tidak) ')

                    if save.lower() == 'ya':
                        list_karyawan.append({'ID Karyawan': add_ID, 'Nama': add_Nama, 'Departemen': add_Departemen, 'Umur': add_Umur, 'Domisili': add_Domisili})
                        print('\nData berhasil disimpan\n')
                        print('\nList Karyawan setelah penambahan :\n')
                        headers = ['ID Karyawan', 'Nama', 'Departemen', 'Umur', 'Domisili']
                        rows = [[karyawan['ID Karyawan'], karyawan['Nama'], karyawan['Departemen'], karyawan['Umur'], karyawan['Domisili']] for karyawan in list_karyawan]
                        print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
                        break
                    elif save.lower() == 'tidak':
                        print('Batal menyimpan data')
                        break
                    else:
                        print('Input tidak valid, silahkan diulang.')  
        elif menu2 == '2' :
            break
        
## UPDATE
        
def updateData() :
    while (True):
        menu3 = input('''----------------------
Merubah Data Karyawan

Menu:
1. Ubah data karyawan
2. Kembali ke menu utama

Masukkan menu yang ingin dijalankan : ''')
        if menu3 == '1':
            while True:
                upd_ID = int(input('Masukkan ID karyawan : '))
                ID_list = [karyawan['ID Karyawan'] for karyawan in list_karyawan]

                if upd_ID not in ID_list:
                    print('ID karyawan tidak ditemukan')
                    break
                else:
                    for karyawan in list_karyawan:
                        if karyawan['ID Karyawan'] == upd_ID:
                            upd_idx = list_karyawan.index(karyawan)
                            headers = ['ID Karyawan', 'Nama', 'Departemen', 'Umur', 'Domisili']
                            data = [list(karyawan.values())]
                            print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
                            break

                    while (True) :    
                        update1 = input('Apakah anda yakin ingin melakukan perubahan? (ya/tidak) ')
                            
                        if update1.lower() == 'ya' :
                            while (True) :
                                inp_field = input('''Silahkan pilih menu untuk melanjutkan perubahan :
1. Name
2. Departemen
3. Umur
4. Domisili
''')
                                if inp_field == '1' :
                                    field = 'Nama'
                                    break
                                elif inp_field == '2':
                                    field = 'Departemen'
                                    break
                                elif inp_field == '3':
                                    field = 'Umur'
                                    break
                                elif inp_field == '4':
                                    field = 'Domisili'
                                    break
                                
                            inp_value = input('Silahkan masukkan perubahan : ')
                                    
                            update2 = input('Apakah anda yakin ingin menyimpan perubahan? (ya/tidak)')
                                
                            if update2.lower() == 'ya' :
                                list_karyawan[upd_idx][field] = inp_value
                                print('Data berhasil dirubah')
                                break
                                        
                            elif update2.lower() == 'tidak' :
                                break
                            else :
                                print('Input tidak valid, silahkan input ulang : ')
                            
                                    
                        elif update1.lower() == 'tidak' :
                            break           
                break
                            
        elif menu3 == '2' :
            break        

## DELETE
        
def deleteData() :
    while (True) :
        menu4 = input('''--------------------
Menghapus Data Karyawan

Menu:
1. Hapus karyawan
2. Kembali ke menu utama

Enter the Menu Number: ''')
        if menu4 == '1' :
            del_ID = int(input('Masukkan ID karyawan: '))
                
            ID_list = []
            for i in list_karyawan:
                ID_list.append(i['ID Karyawan'])
                
            if del_ID not in ID_list :
                print('ID karyawan tidak ditemukan')

            else :
                while (True) :
                    del_cek = input('Apakah anda yakin ingin menghapus? (ya/tidak) ')
                    if del_cek.lower() == 'ya' :
                        for i in range(len(list_karyawan)) :
                            if list_karyawan[i]['ID Karyawan'] == del_ID :
                                del_idx = i
                                list_karyawan.pop(del_idx)
                                print('Data karyawan berhasil dihapus')
                                break
                        break                         
                    elif del_cek.lower() == 'tidak' :
                        break 
                
        elif menu4 == '2' :
            break


while (True) :
    menu = main_menu()
    if menu == '1' :
        readData()
    elif menu == '2' :
        createData()
    elif menu == '3' :
        updateData()
    elif menu == '4' :
        deleteData()            
    elif menu == '5' :
        print('\nTerima kasih\nSampai jumpa kembali\n')
        break
    else:
        print('\nSilahkan masukkan kembali menu dengan benar!\n')

