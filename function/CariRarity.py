# Program CariRarity
# berisi prosedur untuk melakukan pencarian gadget sesuai rarity

def cariRarity(data):
# I.S. data sudah dalam bentuk list of dictionary;
# F.S. menampilkan seluruh gadget sesuai rarity yang dicari.
# KAMUS LOKAL
    # data : array of dictionary (data yang akan diproses)
    # rarity : char (S, A, B, C)

    def isFound(x):
    # fungsi IsFound menghasilkan True jika menemukan barang
    # sesuai rarity yang dicari dan False jika tidak ditemukan
    # KAMUS LOKAL
        # x : char (S, A, B, C)
        # found : bool
        # i : integer
    # ALGORITMA
        found = False
        i = 1
        while i < len(data) and not found:
            if data[i]["rarity"] == x:
                found = True
            else:
                i += 1
        if found:
            return True
        else:
            return False

# ALGORITMA    
    if len(data) == 1:  # data hanya berisi header
        print("Data gadget kosong!")
    else:
        rarity = input("Masukkan rarity: ")
        print("Hasil pencarian:\n")
        
        if isFound(rarity):
            for i in range(1, len(data)):
                if data[i]["rarity"] == rarity:
                    print("Nama            :", data[i]["nama"])
                    print("Deskripsi       :", data[i]["deskripsi"])
                    print("Jumlah          :", data[i]["jumlah"])
                    print("Rarity          :", data[i]["rarity"])
                    print("Tahun Ditemukan :", data[i]["tahun ditemukan"], "\n")
        else:
            print(f"Gadget dengan rarity {rarity} tidak ditemukan!")
