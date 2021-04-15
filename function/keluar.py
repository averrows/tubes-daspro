from save import save

# Program Keluar
# Berisi prosedur untuk mengakhiri program main

def Keluar(kondisi, folderData):
    # parameter kondisi diisi dengan variabel kondisi mengulang pada while loop di program main,
    # parameter folderData diisi dengan file yang akan disave
    prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    while prompt not in "YyNn":  # validasi input
        prompt = input("Apakah Anda mau menyimpan file yang sudah diubah?(y/n) ")
    if prompt in "Yy":
        # jalankan prosedur save data
        save(folderData)
    else:
        pass
    return False