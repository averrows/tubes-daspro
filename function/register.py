def gantiKapital(nama):
    # untuk mengganti sebuah teks dengan kapitalisasi yang benar di awal kata
    nama_kapital = []
    for i in range ((len(nama))):
        if (nama[i] == " ") and (i < len(nama)):
            nama_kapital.append(nama[i])
            nama_kapital.append(nama[i+1].upper())
        elif (nama[i-1] == " "):
            pass
        elif (i == 0):
            nama_kapital.append(nama[i].upper())
        else:
            nama_kapital.append(nama[i].lower())
    return nama_kapital

def cekSama(nama, listKamus, data):
    # untuk memeriksa apakah suatu nama sama dengna sebuah value dari data pada array of dictionary
    count = 0
    for i in range (len(listKamus)):
        if (nama == listKamus[i][data]):
            count = 1
    if (count == 1):
        return True
    else:
        return False

def register():
    # input nama user & mengganti kapitalisasi secara otomatis
    raw_nama_user = input("Masukkan nama: ")
    nama_user = gantiKapital(raw_nama_user)

    # input username & mengecek ketersediaan
    username_user = input("Masukkan username: ")
    sama = cekSama(username_user, userData, 'username')
    while (sama == True):
        print(f"Username {username_user} sudah digunakan!")
        username_user = input("Masukkan username: ")
        sama = cekSama(username_user, userData, 'username')

    # input password -- hashing?
    password_user = input("Masukkan password: ")

    # input alamat
    alamat_user = input("Masukkan alamat: ")
    
    # penambahan data user baru
    new_user = {'nama': nama_user, 'username': username_user, 'password': password_user, 'alamat': alamat_user}
    userData.append(new_user)
    writeCSV("user.csv", userData)
    print(f"User {username_user} telah berhasil register ke dalam Kantong Ajaib.") 