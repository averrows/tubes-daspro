# Program Hashing
# Berisi fungsi untuk hashing password

def hash_ala2(uname, pswd):
    def unique_val(string):
        # untuk mencari nilai ordinal dari kalimat
        string_val = 0
        for i in range(len(string)):
            string_val += ord(string[i])
        return string_val

    def randomize(uname, pswd):
        # untuk mencari angka unik dari kombinasi username dan password
        # random number digunakan untuk randomize jumlah langkah pada caesar
        uname_val = unique_val(uname)
        pswd_val = unique_val(pswd)
        random_num = ((((pswd_val + uname_val) * pswd_val) ** 101) - uname_val) // (len(uname) + len(pswd))
        return random_num

    def salt(uname, pswd):
        # untuk menambahkan "garam" pada password aslinya
        salt_val = str(unique_val(uname)) + str(unique_val(pswd))
        pswd += salt_val
        return pswd

    def key(pswd):
        # untuk mencari angka unik dari password
        # digunakan untuk indexing pada random number
        pswd_val = unique_val(pswd)
        key = 0
        while pswd_val != 0:
            key += pswd_val % 10
            pswd_val //= 10
        return key

    def caesar(char_dec, langkah):
        # untuk menggeser huruf (dalam decimal)
        return (char_dec + langkah) % 128

    def hashing(pswd_char_val, key, random_num):
        # untuk mengubah karakter pada password
        batas_atas = 2*key
        batas_bawah = key
        char_hashed = caesar(caesar(pswd_char_val, int(str(random_num)[batas_bawah:batas_atas])), -key)
        return char_hashed

    # mendapatkan password yang sudah di-hash
    pswd_salted = salt(uname, pswd)
    print(pswd_salted)
    pswd_hashed = ""
    angka_random = randomize(uname, pswd)
    kunci = key(pswd)
    while((len(pswd_hashed))<32):
        for char in pswd_salted:
            char_new = hashing(ord(char), kunci, angka_random)
            pswd_hashed = pswd_hashed + str(char_new)
            kunci += 3
    return pswd_hashed[:32]


# variabel untuk test
u = "a"
p = "a"

print(hash_ala2(u, p))