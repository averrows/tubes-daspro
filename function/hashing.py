# Program Hashing
# Berisi fungsi untuk hashing password

def hash(uname, pswd):
# Fungsi hash mengembalikan password yang sudah di-hash dalam 
# bentuk 32 karakter angka walaupun password yang di-hash hanya 1 karakter

    def unique_val(string):
    # Fungsi mengembalikan nilai ordinal dari suatu string
        string_val = 0
        for i in range(len(string)):
            string_val += ord(string[i])
        return string_val

    def randomize(uname, pswd):
    # Fungsi mengembalikan angka acak dari kombinasi username dan password
    # angka acak ini digunakan untuk randomize jumlah langkah pada caesar
        uname_val = unique_val(uname)
        pswd_val = unique_val(pswd)
        random_num = ((((pswd_val + uname_val) * pswd_val) ** 1001) - uname_val) // (len(uname) + len(pswd))
        return random_num

    def salt(uname, pswd):
    # Fungsi mengembalikan password yang sudah diberi "garam"
        salt_val = str(unique_val(uname)) + str(unique_val(pswd))
        pswd += salt_val
        return pswd

    def key(pswd):
    # Fungsi mengembalikan angka unik/key dari password
    # key digunakan untuk indexing pada random number
        pswd_val = unique_val(pswd)
        key = 0
        while pswd_val != 0:
            key += pswd_val % 10
            pswd_val //= 10
        return key

    def caesar(char_dec, langkah):
    # Fungsi mengembalikan karakter yang sudah digeser (dalam decimal)
        return (char_dec + langkah) % 128

    def hashing(pswd_char_val, key, random_num):
    # Fungsi mengembalikan karakter yang sudah diacak (dalam decimal)
        batas_atas = 2*key
        batas_bawah = key
        char_hashed = caesar(caesar(pswd_char_val, int(str(random_num)[batas_bawah:batas_atas])), -key)
        return char_hashed

# ALGORITMA
    # memberi "garam" pada password asli sebelum di hash
    pswd_salted = salt(uname, pswd)
    
    # generate angka random dan kunci
    angka_random = randomize(uname, pswd)
    kunci = key(pswd)

    # memulai hashing sampai tercapai 32 karakter angka
    pswd_hashed = ""
    while((len(pswd_hashed))<32):
        for char in pswd_salted:
            char_new = hashing(ord(char), kunci, angka_random)
            pswd_hashed = pswd_hashed + str(char_new)
            kunci += 3
    return pswd_hashed[:32]
