from save import save

# Program Keluar
# Berisi prosedur untuk mengakhiri program main

def Keluar(kondisi, folderData):
    # I.S. kondisi looping terdefinisi, folderData terdefinisi;
    # F.S. mengubah kondisi looping.
    # KAMUS LOKAL
        # kondisi : bool
    # ALGORITMA
    prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    while prompt not in "YyNn":  # validasi input
        prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    if prompt in "Yy":
        # jalankan prosedur save data
        save(folderData)
    else:
        pass
    return False