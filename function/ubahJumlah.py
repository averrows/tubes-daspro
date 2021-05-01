from function.validasiTahundanJumlah import jumlahbesarkecil # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error

def ubahjumlah(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
    # ALGORITMA
    status = False
    while not status:
        if IDValid(ID):
            status = True
            if ID[0] == "G":
                if len(gadgetData) == 1:
                # validasi data kosong    
                    print("Maaf data tidak tersedia")
                else:
                    ketemu = False
                    while not ketemu:
                        if IDditemukan(ID, gadgetData):
                            ketemu = True
                            for i in range(1, len(gadgetData)):
                                if ID == gadgetData[i]["id"]:
                                    kondisi = True
                                    kondisijumlah = False
                                    jumlah = int(input("Masukkan jumlah: "))
                                    while not kondisijumlah:                   
                                        if jumlahbesarkecil(jumlah):
                                            kondisijumlah = True
                                            jumlahgadget = int(gadgetData[i]["jumlah"])
                                            if jumlah >= 0:
                                                jumlahgadget += jumlah
                                                gadgetData[i]["jumlah"] = jumlahgadget
                                                print(str(jumlah) + " " + str(gadgetData[i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(gadgetData[i]["jumlah"]))
                                            else: #jumlah < 0:
                                                stringjumlah = str(jumlah)
                                                panjangjumlah = len(stringjumlah)
                                                jumlahasli = stringjumlah[1:panjangjumlah]
                                                if jumlahgadget >= int(jumlahasli):
                                                    jumlahgadget += jumlah
                                                    gadgetData[i]["jumlah"] = jumlahgadget
                                                    print(str(jumlahasli) + " " + str(gadgetData[i]["nama"]) + " berhasil diibuang. Stok sekarang: " + str(gadgetData[i]["jumlah"]))
                                                else:
                                                    print(str(jumlahasli) + " " + str(gadgetData[i]["nama"]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(gadgetData[i]["jumlah"]) + "(<" + str(jumlahasli) + ")")
                                        else:
                                            print("Masukkan jumlah tidak valid.")
                                            jumlah = int(input("Masukkan jumlah: "))
                                else:
                                    kondisi = False
                            if kondisi == True:
                                pass
                            else:
                                print("Tidak ada Item dengan ID Tersebut")
                                ID = input("Masukkan ID: ")
                        else:
                            print("Tidak ada Item dengan ID Tersebut")
                            ID = input("Masukkan ID: ")

            elif ID[0] == "C":
                if len(consumableData) == 1:
                # validasi data kosong
                    print("Maaf data tidak tersedia")
                else :
                    ketemu = False
                    while not ketemu:
                        if IDditemukan(ID, consumableData):
                            ketemu = True
                            for i in range(1, len(consumableData)):
                                if ID == consumableData[i]["id"]:
                                    kondisi = True
                                    kondisijumlah = False
                                    jumlah = int(input("Masukkan jumlah: "))
                                    while not kondisijumlah:
                                        if jumlahbesarkecil(jumlah):
                                            kondisijumlah = True
                                            jumlahconsumable = int(consumableData[i]["jumlah"])
                                            if jumlah >= 0:
                                                jumlahconsumable += jumlah
                                                consumableData[i]["jumlah"] = jumlahconsumable
                                                print(str(jumlah) + " " + str(consumableData[i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(consumableData[i]["jumlah"]))
                                            else: #jumlah < 0
                                                stringjumlah = str(jumlah)
                                                panjangjumlah = len(stringjumlah)
                                                jumlahasli = stringjumlah[1:panjangjumlah]
                                                if jumlahconsumable >= int(jumlahasli): 
                                                    jumlahconsumable += jumlah
                                                    consumableData[i]["jumlah"] = jumlahconsumable
                                                    print(str(jumlah) + " " + str(consumableData[i]["nama"]) + " berhasil dibuang. Stok sekarang: " + str(consumableData[i]["jumlah"]))
                                                else:
                                                    print(str(jumlah) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(consumableData[i]["jumlah"]) + "(<" + str(jumlah) + ")")
                                        else:
                                            print("Masukkan jumlah tidak valid")
                                            jumlah = int(input("Masukkan jumlah: "))
                                else:
                                    kondisi = False
                            if kondisi == True:
                                pass
                            else:
                                print("Tidak ada Item dengan ID Tersebut")
                                ID = input("Masukkan ID: ")
                        else:
                            print("Tidak ada Item dengan ID Tersebut")
                            ID = input("Masukkan ID: ")
        else:
            print("Input ID Tidak Valid!")
            ID = input("Masukkan ID: ")