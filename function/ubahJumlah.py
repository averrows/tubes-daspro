from function.validasiTahundanJumlah import jumlahbesarkecil # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error

def ubahjumlah(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
    # ALGORITMA
    if IDValid(ID):
        if ID[0] == "G":
            if len(gadgetData) == 1:
            # validasi data kosong    
                print("maaf data tidak tersedia")
            else:
                if IDditemukan(ID, gadgetData):
                    for i in range(1, len(gadgetData)):
                        jumlah = int(input("Masukkan jumlah: "))
                        if jumlahbesarkecil(jumlah):
                            if int(gadgetData[i]["jumlah"]) < jumlah and jumlah > 0:
                                gadgetData[i]["jumlah"] += int(jumlah)
                                print(jumlah + " " + gadgetData[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + gadgetData[i]["jumlah"])
                            elif int(gadgetData[i]["jumlah"]) > jumlah and jumlah > 0:
                                gadgetData[i]["jumlah"] += jumlah
                                print(jumlah + " " + gadgetData[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + gadgetData[i]["jumlah"])
                            elif int(gadgetData[i]["jumlah"]) > jumlah and jumlah < 0:
                                gadgetData[i]["jumlah"] -= jumlah
                                print(jumlah + " " + gadgetData[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + gadgetData[i]["jumlah"])
                            else:
                                print(jumlah + " gagal dibuang karena stok kurang. Stok sekarang: " + gadgetData[i]["jumlah"] + "(<" + jumlah + ")")
                        else:
                            print("Masukkan jumlah tidak valid.")
                else:
                    print("Tidak ada item dengan ID tersebut.")
        elif ID[0] == "C":
            if len(consumableData) == 1:
            # validasi data kosong
                print("maaf data tidak tersedia")
            else:
                if IDditemukan(ID, consumableData):
                    for i in range(1, len(consumableData)):
                        jumlah = input("Masukkan jumlah: ")
                        if jumlahbesarkecil(jumlah):
                            if consumableData[i]["jumlah"] < jumlah and jumlah > 0:
                                consumableData[i]["jumlah"] += jumlah
                                print(jumlah + " " + consumableData[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + consumableData[i]["jumlah"])
                            elif consumableData[i]["jumlah"] > jumlah and jumlah > 0:
                                consumableData[i]["jumlah"] += jumlah
                                print(jumlah + " " + consumableData[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + consumableData[i]["jumlah"])
                            elif consumableData[i]["jumlah"] > jumlah and jumlah < 0:
                                consumableData[i]["jumlah"] -= jumlah
                                print(jumlah + " " + consumableData[i]["nama"] + " berhasil ditambahkan. Stok sekarang: " + consumableData[i]["jumlah"])
                            else:
                                print(jumlah + " gagal dibuang karena stok kurang. Stok sekarang: " + consumableData[i]["jumlah"] + "(<" + jumlah + ")")
                        else:
                            print("Masukkan jumlah tidak valid")
                else:
                    print("Tidak ada item dengan ID tersebut.")
        else:
            print("Input ID Tidak Valid!")
    else:
        print("Input ID Tidak Valid!")