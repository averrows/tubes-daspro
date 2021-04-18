from register import cekSama

def validasiAkun(username, password, userData):
    sama_username = cekSama(username, userData, 'username')
    sama_password = cekSama(password, userData, 'password')
    if (sama_username == True):
        if (sama_password == True):
            return True
        else:
            return False
    else:
        return False       

def login(userData):
    # input username dan password
    username_login = input("Masukkan username: ")
    password_login = input("Masukkan password: ")
    
    # validasi akun
    validasiAkun(username_login, password_login, userData)
    while (validasiAkun == False):
        print("Masukan username atau password salah!")
        username_login = input("Masukkan username: ")
        password_login = input("masukkan password: ")
        validasiAkun(username_login, password_login, userData)

    # login berhasil
    print(f"Halo {username_login}! Selamat datang di Kantong Ajaib.")