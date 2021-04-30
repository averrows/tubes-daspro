from Function.validasiID import IDValid, IDditemukan

# from CsvTools import parseCSV
# gadgetData = parseCSV("data" + "/gadget.csv")
# consumableData = parseCSV("data" + "/consumable.csv")

def tambahitem(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
# ALGORITMA
    if IDValid(ID):
        if ID[0] == "G":
            if len(gadgetData) == 1:
            # validasi data kosong    
                print("maaf data tidak tersedia")
            else:
                if IDditemukan(ID, gadgetData):
                    print("Gagal menambahkan item karena ID sudah ada.")
                else:
                    gadgettambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    gadgettambahan["id"] = ID
                    gadgettambahan["nama"] = input("Masukkan nama: ")
                    gadgettambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    gadgettambahan["jumlah"] = input("Masukkan Jumlah: ")
                    gadgettambahan["rarity"] = input("Masukkan Rarity: ")
                    if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S" or gadgettambahan["rarity"] == "c" or gadgettambahan["rarity"] == "b" or gadgettambahan["rarity"] == "a" or gadgettambahan["rarity"] == "s":
                        gadgettambahan["tahun"] = int(input("Masukkan tahun: "))
                        gadgetData.append(gadgettambahan)
                        print("Item berhasil ditambahkan ke database.")
                    else :
                        print("Input Rarity Tidak Valid!")
                    print("Gagal menambahkan item karena ID sudah ada.")

        elif ID[0] == "C":
            if len(consumableData) == 1:
            # validasi data kosong
                print("maaf data tidak tersedia")
            else:
                if IDditemukan(ID, consumableData):
                    print("Gagal menambahkan item karena ID sudah ada.")
                else:
                    consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    consumabletambahan["id"] = ID
                    consumabletambahan["nama"] = input("Masukkan nama: ")
                    consumabletambahan["deskripsi"] = input("Masukkan Deskripsi: ")
                    consumabletambahan["jumlah"] = input("Masukkan Jumlah: ")
                    consumabletambahan["rarity"] = input("Masukkan Rarity: ")
                    if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S" or consumabletambahan["rarity"] == "c" or consumabletambahan["rarity"] == "b" or consumabletambahan["rarity"] == "a" or consumabletambahan["rarity"] == "s":
                        consumableData.append(consumabletambahan)
                        print("Item berhasil ditambahkan ke database.")
                    else :
                        print("Input Rarity Tidak Valid!")

        else: #ID[0] != "C" and ID[0] != "G"
            print("Gagal menambahkan item karena ID tidak valid.")
    else:
        print("Gagal menambahkan item karena ID tidak valid.")