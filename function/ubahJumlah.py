from Function.validasiID import IDValid, IDditemukan

from CsvTools import parseCSV
gadgetData = parseCSV("data" + "/gadget.csv")
consumableData = parseCSV("data" + "/consumable.csv")

def ubahjumlah(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    jumlah = input("Masukkan jumlah: ")
    
    # ALGORITMA
    if IDValid(ID):
        if ID[0] == "G":
            if len(gadgetData) == 1:
            # validasi data kosong    
                print("maaf data tidak tersedia")
                if IDditemukan(ID, gadgetData):
                    for i in range(len(gadgetData)):
                        if data[i]["jumlah"] < jumlah and jumlah > 0:
                            data[i]["jumlah"] += jumlah
                            print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                        elif data[i]["jumlah"] > jumlah and jumlah > 0:
                            data[i]["jumlah"] += jumlah
                            print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                        elif data[i]["jumlah"] > jumlah and jumlah < 0:
                            data[i]["jumlah"] -= jumlah
                            print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                        else:
                                print(jumlah + " gagal dibuang karena stok kurang. Stok sekarang: " + data[i]["jumlah"] + "(<" + jumlah + ")")
                else:
                    print("Tidak ada item dengan ID tersebut.")
        elif ID[0] == "C":
            if len(consumableData) == 1:
            # validasi data kosong
                print("maaf data tidak tersedia")
                if IDditemukan(ID, consumableData):
                    for i in range(len(consumableData)):
                        if data[i]["jumlah"] < jumlah and jumlah > 0:
                            data[i]["jumlah"] += jumlah
                            print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                        elif data[i]["jumlah"] > jumlah and jumlah > 0:
                            data[i]["jumlah"] += jumlah
                            print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                        elif data[i]["jumlah"] > jumlah and jumlah < 0:
                            data[i]["jumlah"] -= jumlah
                            print(jumlah + " " + data[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + data[i]["jumlah"])
                        else:
                            print(jumlah + " gagal dibuang karena stok kurang. Stok sekarang: " + data[i]["jumlah"] + "(<" + jumlah + ")")
                else:
                    print("Tidak ada item dengan ID tersebut.")
        else:
            print("Tidak ada item dengan ID tersebut.")
    else:
        print("Tidak ada item dengan ID tersebut.")