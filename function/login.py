from CsvTools import parseCSV
userData = parseCSV("data" + "/user.csv")

def cekSama(nama, listKamus, data):
    # untuk memeriksa apakah suatu nama sama dengan sebuah value dari data pada array of dictionary
    count = 0
    for i in range (len(listKamus)):
        if (nama == listKamus[i][data]):
            count += 1
    if (count > 0):
        return True
    else:
        return False

def login(userData):
    # input username dan password
    username_login = input("Masukkan username: ")
    password_login = input("Masukkan password: ")
    
    # validasi akun
    sama_username = cekSama(username_login, userData, 'username')
    sama_password = cekSama(password_login, userData, 'password')
    while (sama_username == False) or (sama_password == False):
        print("Masukan username atau password salah!")
        username_login = input("Masukkan username: ")
        password_login = input("masukkan password: ")
        sama_username = cekSama(username_login, userData, 'username')
        sama_password = cekSama(password_login, userData, 'password')

    # login berhasil
    print(f"Halo {username_login}! Selamat datang di Kantong Ajaib.")
    status_login = {
        'username': username_login,
        'role': 'user'
        }
    return status_login