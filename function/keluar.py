from function.save import save # pylint: disable=import-error

# Program Keluar
# Berisi fungsi untuk mengakhiri program main

def keluar(kondisi, newData, folderData):
# Fungsi mengembalikan nilai False 
    prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    while prompt not in "YyNn":  # validasi input
        prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    if prompt in "Yy":
        # jalankan prosedur save data
        save(newData,folderData)
    else:
        pass
    return False