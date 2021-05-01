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
                    jumlah = False
                    while not jumlah:
                        if jumlahvalid(gadgettambahan["jumlah"]):
                            jumlah = True
                            statusrarity = False
                            gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                            while not statusrarity:
                                if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                                    statusrarity = True
                                    statustahun = False
                                    gadgettambahan["tahun"] = input("Masukkan tahun: ")
                                    while not statustahun:
                                        if tahunvalid(gadgettambahan["tahun"]):
                                            statustahun = True
                                            gadgetData.append(gadgettambahan)
                                            print("Item berhasil ditambahkan ke database.")
                                        else:
                                            print("Input Tahun Tidak Valid!")
                                            gadgettambahan["tahun"] = input("Masukkan tahun: ")
                                else :
                                    print("Input Rarity Tidak Valid!")
                                    gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                        else:
                            print("Input Jumlah Tidak Valid!")
                            gadgettambahan["jumlah"] = input("Masukkan Jumlah: ")
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
                            jumlah = False
                            while not jumlah:
                                if jumlahvalid(gadgettambahan["jumlah"]):
                                    jumlah = True
                                    statusrarity = False
                                    gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                                    while not statusrarity:
                                        if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                                            statusrarity = True
                                            statustahun = False
                                            gadgettambahan["tahun"] = input("Masukkan tahun: ")
                                            while not statustahun:
                                                if tahunvalid(gadgettambahan["tahun"]):
                                                    statustahun = True
                                                    gadgetData.append(gadgettambahan)
                                                    print("Item berhasil ditambahkan ke database.")
                                                else:
                                                    print("Input Tahun Tidak Valid!")
                                                    gadgettambahan["tahun"] = input("Masukkan tahun: ")
                                        else :
                                            print("Input Rarity Tidak Valid!")
                                            gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                                else:
                                    print("Input Jumlah Tidak Valid!")
                                    gadgettambahan["jumlah"] = input("Masukkan Jumlah: ")
                    break

            else:
                if len(consumableData) == 1:
                    consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    consumabletambahan["id"] = ID
                    consumabletambahan["nama"] = input("Masukkan nama: ")
                    consumabletambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                    jumlah = False
                    while not jumlah:
                        if jumlahvalid(consumabletambahan["jumlah"]):
                            jumlah = True
                            statusrarity = False
                            consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                            while not statusrarity:
                                if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                                    statusrarity = True
                                    consumableData.append(consumabletambahan)
                                    print("Item berhasil ditambahkan ke database.")
                                else :
                                    print("Input Rarity Tidak Valid!")
                                    consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                        else:
                            print("Input Jumlah Tidak Valid!")
                            consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                else:
                    ketemu = False
                    while not ketemu:
                        if IDditemukan(ID, consumableData):
                            print("Gagal menambahkan item karena ID sudah ada.")
                            ID = input("Masukkan ID: ")
                        else:
                            consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                            consumabletambahan["id"] = ID
                            consumabletambahan["nama"] = input("Masukkan nama: ")
                            consumabletambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                            consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                            jumlah = False
                            while not jumlah:
                                if jumlahvalid(consumabletambahan["jumlah"]):
                                    jumlah = True
                                    statusrarity = False
                                    consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                                    while not statusrarity:
                                        if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                                            statusrarity = True
                                            consumableData.append(consumabletambahan)
                                            print("Item berhasil ditambahkan ke database.")
                                        else :
                                            print("Input Rarity Tidak Valid!")
                                            consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                                else:
                                    print("Input Jumlah Tidak Valid!")
                                    consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                    break

        else:
            print("Gagal menambahkan item karena ID tidak valid.")
            ID = input("Masukkan ID: ")