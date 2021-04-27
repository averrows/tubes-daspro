from function.hashing import hash # pylint: disable=import-error

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
    nama_kapital = "".join(nama_kapital)
    return nama_kapital

def cekSama(nama, listKamus, data):
    # untuk memeriksa apakah suatu nama sama dengan sebuah value dari data pada array of dictionary
    count = 0
    for i in range (1, len(listKamus)):
        if (nama == listKamus[i][data]):
            count += 1
    if (count > 0):
        return True
    else:
        return False

def register(userData):
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

    # input password beserta hashing
    password = input("Masukkan password: ")
    password_user = hash(username_user, password)

    # input alamat
    alamat_user = input("Masukkan alamat: ")
    
    # penggabungan data baru dan lama
    new_user = {'nama': nama_user, 'username': username_user, 'password': password_user, 'alamat': alamat_user, 'role': 'user'}
    userData.append(new_user)

    print(f"User {username_user} telah berhasil register ke dalam Kantong Ajaib.")