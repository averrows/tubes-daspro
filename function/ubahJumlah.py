from function.validasiTahundanJumlah import jumlahbesarkecil # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error

def ubahjumlah(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
    # ALGORITMA
    if IDValid(ID):
        if ID[0] == "G":
            if len(gadgetData) == 1:
            # validasi data kosong    
                print("Maaf data tidak tersedia")
            else:
                for i in range(1, len(gadgetData)):
                    if IDditemukan(ID, gadgetData):
                        if ID == gadgetData[i]["id"]:
                            kondisi = True
                            jumlah = int(input("Masukkan jumlah: "))                   
                            if jumlahbesarkecil(jumlah):
                                jumlahgadget = int(gadgetData[i]["jumlah"])
                                if (jumlahgadget < jumlah or jumlahgadget >= jumlah) and jumlah > 0:
                                    jumlahgadget += jumlah
                                    gadgetData[i]["jumlah"] = jumlahgadget
                                    print(str(jumlah) + " " + str(gadgetData[i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(gadgetData[i]["jumlah"]))
                                elif (jumlahgadget > jumlah or jumlahgadget == jumlah) and jumlah < 0:
                                    jumlahgadget += jumlah
                                    gadgetData[i]["jumlah"] = jumlahgadget
                                    print(str(jumlah) + " " + str(gadgetData[i]["nama"]) + " berhasil diibuang. Stok sekarang: " + str(gadgetData[i]["jumlah"]))
                                else:
                                    print(str(jumlah) + " " + str(gadgetData[i]["nama"]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(gadgetData[i]["jumlah"]) + "(<" + str(jumlah) + ")")
                            else:
                                print("Masukkan jumlah tidak valid.")
                        else:
                            kondisi = False
                if kondisi == True:
                    pass
                else:
                    print("Tidak ada Item dengan ID Tersebut")
                    
        elif ID[0] == "C":
            if len(consumableData) == 1:
            # validasi data kosong
                print("Maaf data tidak tersedia")
            else:
                for i in range(1, len(consumableData)):
                    if IDditemukan(ID, consumableData):
                        if ID == consumableData[i]["id"]:
                            kondisi = True
                            jumlah = int(input("Masukkan jumlah: "))
                            if jumlahbesarkecil(jumlah):
                                jumlahconsumable = int(consumableData[i]["jumlah"])
                                if (jumlahconsumable < jumlah or jumlahconsumable >= jumlah) and jumlah > 0:
                                    jumlahconsumable += jumlah
                                    consumableData[i]["jumlah"] = jumlahconsumable
                                    print(str(jumlah) + " " + str(consumableData[i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(consumableData[i]["jumlah"]))
                                elif jumlahconsumable >= jumlah and jumlah < 0:
                                    jumlahconsumable += jumlah
                                    consumableData[i]["jumlah"] = jumlahconsumable
                                    print(str(jumlah) + " " + str(consumableData[i]["nama"]) + " berhasil dibuang. Stok sekarang: " + str(consumableData[i]["jumlah"]))
                                else:
                                    print(str(jumlah) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(consumableData[i]["jumlah"]) + "(<" + str(jumlah) + ")")
                            else:
                                print("Masukkan jumlah tidak valid")
                        else:
                            kondisi = False
                if kondisi == True:
                    pass
                else:
                    print("Tidak ada Item dengan ID Tersebut")
        else:
            print("Input ID Tidak Valid!")
    else:
        print("Input ID Tidak Valid!")