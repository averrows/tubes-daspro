def gantiKapital(nama):
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

def register():
    nama_user = input("Masukkan nama: ")
    username_user = input("Masukkan username: ")
    password_user = input("Masukkan password: ")
    alamat_user = input("Masukkan alamat: ")
    
    print(f"User {username_user} telah berhasil register ke dalam Kantong Ajaib.") 