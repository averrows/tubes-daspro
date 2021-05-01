from function.validasiTahundanJumlah import tahunvalid, jumlahvalid # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error

def tambahitem(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
# ALGORITMA
    tidakada = False
    while not tidakada:
        if IDValid(ID):
            tidakada = True
            if ID[0] == "G":
                if len(gadgetData) == 1:
                    gadgettambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    gadgettambahan["id"] = ID
                    gadgettambahan["nama"] = input("Masukkan nama: ")
                    gadgettambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    gadgettambahan["jumlah"] = input("Masukkan Jumlah: ")
                    if jumlahvalid(gadgettambahan["jumlah"]):
                        gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                        if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                            gadgettambahan["tahun"] = input("Masukkan tahun: ")
                            if tahunvalid(gadgettambahan["tahun"]):
                                gadgetData.append(gadgettambahan)
                                print("Item berhasil ditambahkan ke database.")
                            else:
                                print("Input Tahun Tidak Valid!")
                        else :
                            print("Input Rarity Tidak Valid!")
                    else:
                        print("Input Jumlah Tidak Valid!")
                else:
                    ketemu = False
                    while not ketemu:
                        if IDditemukan(ID, gadgetData):
                            print("Gagal menambahkan item karena ID sudah ada.")
                            ID = ("Masukkan ID: ")
                        else:
                            ketemu = True
                            gadgettambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                            gadgettambahan["id"] = ID
                            gadgettambahan["nama"] = input("Masukkan nama: ")
                            gadgettambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                            gadgettambahan["jumlah"] = input("Masukkan Jumlah: ")
                            if jumlahvalid(gadgettambahan["jumlah"]):
                                gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                                if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                                    gadgettambahan["tahun"] = input("Masukkan tahun: ")
                                    if tahunvalid(gadgettambahan["tahun"]):
                                        gadgetData.append(gadgettambahan)
                                        print("Item berhasil ditambahkan ke database.")
                                    else:
                                        print("Input Tahun Tidak Valid!")
                                else :
                                    print("Input Rarity Tidak Valid!")
                            else:
                                print("Input Jumlah Tidak Valid!")

            else:
                if len(consumableData) == 1:
                    consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    consumabletambahan["id"] = ID
                    consumabletambahan["nama"] = input("Masukkan nama: ")
                    consumabletambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                    if jumlahvalid(consumabletambahan["jumlah"]):
                        consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                        if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                            consumableData.append(consumabletambahan)
                            print("Item berhasil ditambahkan ke database.")
                        else :
                            print("Input Rarity Tidak Valid!")
                    else:
                        print("Input Jumlah Tidak Valid!")
                else:
                    if IDditemukan(ID, consumableData):
                        print("Gagal menambahkan item karena ID sudah ada.")
                    else:
                        consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                        consumabletambahan["id"] = ID
                        consumabletambahan["nama"] = input("Masukkan nama: ")
                        consumabletambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                        consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                        if jumlahvalid(consumabletambahan["jumlah"]):
                            consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                            if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                                consumableData.append(consumabletambahan)
                                print("Item berhasil ditambahkan ke database.")
                            else :
                                print("Input Rarity Tidak Valid!")
                        else:
                            print("Input Jumlah Tidak Valid!")

        else:
            print("Gagal menambahkan item karena ID tidak valid.")
            ID = ("Masukkan ID: ")