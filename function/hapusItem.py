from function.validasiID import IDValid, IDditemukan #pylint: disable=import-error

def hapusitem(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    tidakada = False
    # ALGORITMA
    while not tidakada:
        if IDValid(ID):
            tidakada = True
            if ID[0] == "G":
                if len(gadgetData) == 1:
                    print("Maaf data tidak tersedia")
                else:
                    ketemu = False
                    while not ketemu:
                        if IDditemukan(ID, gadgetData):
                            ketemu = True
                            for i in range(1, len(gadgetData)):
                                if gadgetData[i]["id"] == ID:
                                    print("Apakah anda ingin menghapus " + gadgetData[i]["nama"] + "?(Yy/Nn)")
                                    op = input(">>> ")
                                    yakin = False
                                    while not yakin:
                                        if op == "Y" or op == "y":
                                            del gadgetData[i]
                                            yakin = True
                                            print("Item telah berhasil dihapus")
                                        elif op == "n" or op == "N" :
                                            yakin = True
                                            print("Penghapusan tidak jadi dilakukan, kamu akan kembali ke menu")
                                        else:
                                            op = input(">>> ")
                        else:
                            print("Tidak ada item dengan ID tersebut")
                            ID = input("Masukkan ID: ")
            else: #ID[0] == "C":
                if len(consumableData) == 1:
                    print("maaf data tidak tersedia")
                else:
                    ketemu = False
                    while not ketemu:
                        if IDditemukan(ID, consumableData):
                            ketemu = True
                            for i in range(1, len(consumableData)):
                                if consumableData[i]["id"] == ID:
                                    print("Apakah anda ingin menghapus " + consumableData[i]["nama"] + "?(Yy/Nn)")
                                    op = input(">>> ")
                                    yakin = False
                                    while not yakin:
                                        if op == "Y" or op == "y":
                                            del consumableData[i]
                                            yakin = True
                                            print("Item telah berhasil dihapus")
                                        elif op == "n" or op == "N" :
                                            yakin = True
                                            print("Penghapusan tidak jadi dilakukan, kamu akan kembali ke menu")
                                        else:
                                            op = input(">>> ")
                        else:
                            print("Tidak ada item dengan ID tersebut")
                            ID = input("Masukkan ID: ")
        else:
            print("Input ID tidak valid!")
            ID = input("Masukkan ID: ")