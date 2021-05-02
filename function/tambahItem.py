from function.validasiTahundanJumlah import tahunvalid, jumlahvalid # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error

def tambahitem(gadgetData,consumableData):
    # main procedure
    # ALGORITMA
    validID = False
    while not validID:
        ID = input("Masukkan ID: ")
        if IDValid(ID):
            if ID[0] == "G":
                if len(gadgetData) == 1:    # jika data gadget hanya berisi header
                    tambahgadget(ID, gadgetData)
                    validID = True
                else:   # data ada isinya
                    # cek apakah ada ID yang sama
                    if IDditemukan(ID, gadgetData):
                        print("Gagal menambahkan item karena ID sudah ada.")
                    else:
                        tambahgadget(ID, gadgetData)
                        validID = True

            else:   # ID[0] == "C"
                if len(consumableData) == 1:    # jika data consumable hanya berisi header
                    tambahconsumable(ID, consumableData)
                    validID = True
                else:   # data ada isinya
                    # cek apakah ada ID yang sama
                    if IDditemukan(ID, consumableData):
                        print("Gagal menambahkan item karena ID sudah ada.")
                    else:
                        tambahconsumable(ID, consumableData)
                        validID = True
            
        else:
            print("Gagal menambahkan item karena ID tidak valid.")


def tambahgadget(ID, gadgetData):
    gadgettambahan = {"id": f"{ID}", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
    gadgettambahan["nama"] = input("Masukkan Nama: ")
    gadgettambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    
    # input + validasi jumlah
    isjumlahvalid = False
    while not isjumlahvalid:
        gadgettambahan["jumlah"] = input("Masukkan Jumlah: ")
        if jumlahvalid(gadgettambahan["jumlah"]):
            isjumlahvalid = True
        else:
            print("Input Jumlah Tidak Valid!")

    # input + validasi rarity
    israrityvalid = False
    while not israrityvalid:
        gadgettambahan["rarity"] = input("Masukkan Rarity: ")
        if gadgettambahan["rarity"] in "SABC":
            israrityvalid = True
        else :
            print("Input Rarity Tidak Valid!")
                    
    # input + validasi tahun
    istahunvalid = False
    while not istahunvalid:
        gadgettambahan["tahun"] = input("Masukkan tahun: ")
        if tahunvalid(gadgettambahan["tahun"]):
            gadgetData.append(gadgettambahan)
            print("Item berhasil ditambahkan ke database.")
            istahunvalid = True
        else:
            print("Input Tahun Tidak Valid!")


def tambahconsumable(ID, consumableData):
    consumabletambahan = {"id": f"{ID}", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
    consumabletambahan["nama"] = input("Masukkan nama: ")
    consumabletambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    
    isjumlahvalid = False
    while not isjumlahvalid:
        consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
        if jumlahvalid(consumabletambahan["jumlah"]):
            isjumlahvalid = True
        else:
            print("Input Jumlah Tidak Valid!")
                
    israrityvalid = False
    while not israrityvalid:
        consumabletambahan["rarity"] = input("Masukkan Rarity: ")
        if consumabletambahan["rarity"] in "SABC":
            israrityvalid = True
            consumableData.append(consumabletambahan)
            print("Item berhasil ditambahkan ke database.")
        else :
            print("Input Rarity Tidak Valid!")
                                    