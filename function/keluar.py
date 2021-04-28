from function.simpan import simpan # pylint: disable=import-error

# Program Keluar
# Berisi fungsi untuk mengakhiri program main

def keluar(kondisi, newData, folderData):
# Fungsi mengembalikan nilai False 
# KAMUS LOKAL
    # kondisi : bool
# ALGORITMA
    prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    while prompt not in "YyNn":  # validasi input
        prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    if prompt in "Yy":
        # jalankan prosedur save data
        simpan(newData,folderData)
    else:
        pass
    return False