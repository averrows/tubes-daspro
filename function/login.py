from function.hashing import hash # pylint: disable=import-error

def cekSama(nama, listKamus, data):
    # untuk memeriksa apakah suatu nama sama dengan sebuah value dari data pada array of dictionary
    count = 0
    for i in range (1,len(listKamus)):
        if (nama == listKamus[i][data]):
            count += 1
    if (count > 0):
        return True
    else:
        return False

def login(userData):
    # validasi data tidak kosong
    if (len(userData) == 1):
        print("Ups, maaf! Data tidak ditemukan (っ °Д °;)っ")
    else:
        # input username dan password
        username_login = input("Masukkan username: ")
        password = input("Masukkan password: ")
        password_login = hash(username_login, password)
        
        # validasi akun
        sama_username = cekSama(username_login, userData, 'username')
        sama_password = cekSama(password_login, userData, 'password')
        while (sama_username == False) or (sama_password == False):
            print("Masukan username atau password salah!\n")
            username_login = input("Masukkan username: ")
            password = input("masukkan password: ")
            password_login = hash(username_login, password)
            sama_username = cekSama(username_login, userData, 'username')
            sama_password = cekSama(password_login, userData, 'password')

        # cek role & id akun
        for i in range (1, len(userData)):
            if (username_login == userData[i]['username']):
                role_login = userData[i]['role']
                id_login = userData[i]['id']

        # login berhasil
        print("Login berhasil!")
        print("")
        print(f"Halo {username_login}! Selamat datang di Kantong Ajaib.")
        status_login = {
            'id': id_login,
            'username': username_login,
            'role': role_login
            }
        return status_login