from Function.validasiID import IDValid, IDditemukan

from CsvTools import parseCSV
gadgetData = parseCSV("data" + "/gadget.csv")
consumableData = parseCSV("data" + "/consumable.csv")

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
                        if data[i]["id"] == ID:
                            print("Apakah anda ingin menghapus " + data[i]["nama"] + "?(Yy/Nn)")
                            op = input()
                            if op == "Y" or op == "y":
                                del data[i]
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
                        if data[i]["id"] == ID:
                            print("Apakah anda ingin menghapus " + data[i]["nama"] + "?(Yy/Nn)")
                            op = input()
                            if op == "Y" or op == "y":
                                del data[i]
                                print("Item telah berhasil dihapus")
                            elif op == "n" or op == "N" :
                                print("Kembali ke Menu")
                else:
                    print("Tidak ada item dengan ID tersebut")
        else:
            print("Tidak ada item dengan ID tersebut")      