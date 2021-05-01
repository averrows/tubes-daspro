from function.validasiID import IDValid, IDditemukan #pylint: disable=import-error

def hapusitem(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
    # ALGORITMA
    if IDValid(ID):
        if ID[0] == "G":
            if len(gadgetData) == 1:
                print("maaf data tidak tersedia")
            else:
                if IDditemukan(ID, gadgetData):
                    for i in range(1, len(gadgetData)):
                        if gadgetData[i]["id"] == ID:
                            print("Apakah anda ingin menghapus " + gadgetData[i]["nama"] + "?(Yy/Nn)")
                            op = input(">>> ")
                            if op == "Y" or op == "y":
                                del gadgetData[i]
                                print("Item telah berhasil dihapus")
                            elif op == "n" or op == "N" :
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
                if IDditemukan(ID, consumableData):
                    for i in range(1, len(consumableData)):
                        if consumableData[i]["id"] == ID:
                            print("Apakah anda ingin menghapus " + consumableData[i]["nama"] + "?(Yy/Nn)")
                            op = input(">>> ")
                            if op == "Y" or op == "y":
                                del consumableData[i]
                                print("Item telah berhasil dihapus")
                            elif op == "n" or op == "N" :
                                print("Penghapusan tidak jadi dilakukan, kamu akan kembali ke menu")
                            else:
                                op = input(">>> ")
                else:
                    print("Tidak ada item dengan ID tersebut")
                    ID = input("Masukkan ID: ")
    else:
        print("Input ID tidak valid!")
        ID = input("Masukkan ID: ")