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
                    for i in range(len(gadgetData)):
                        if gadgetData[i]["id"] == ID:
                            print("Apakah anda ingin menghapus " + gadgetData[i]["nama"] + "?(Yy/Nn)")
                            op = input()
                            if op == "Y" or op == "y":
                                del gadgetData[i]
                                print("Item telah berhasil dihapus")
                            elif op == "n" or op == "N" :
                                print("Kembali ke Menu")
                else:
                    print("Tidak ada item dengan ID tersebut")
        elif ID[0] == "C":
            if len(consumableData) == 1:
                print("maaf data tidak tersedia")
            else:
                if IDditemukan(ID, consumableData):
                    for i in range(len(consumableData)):
                        if consumableData[i]["id"] == ID:
                            print("Apakah anda ingin menghapus " + consumableData[i]["nama"] + "?(Yy/Nn)")
                            op = input()
                            if op == "Y" or op == "y":
                                del consumableData[i]
                                print("Item telah berhasil dihapus")
                            elif op == "n" or op == "N" :
                                print("Kembali ke Menu")
                else:
                    print("Tidak ada item dengan ID tersebut")
        else:
            print("Tidak ada item dengan ID tersebut")      