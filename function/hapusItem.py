from CsvTools import parseCSV
gadgetData = parseCSV("data" + "/gadget.csv")
consumableData = parseCSV("data" + "/consumable.csv")

def hapusitem(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    op = input()
    
    def IsFound(ID, data):
        found = False
        i = 1
        while i < len(data) and not found:
            if data[i]["id"] == ID:
                found = True
            else:
                i += 1
        if found:
            return True
        else:
            return False
    
    # ALGORITMA
    if ID[0] == "G":
        if IsFound(ID, gadgetData):
            for i in range(len(gadgetData)):
                if data[i]["id"] == ID:
                    print("Apakah anda ingin menghapus " + data[i]["nama"] + "? (yYnN)")
                    if op == "Y" or op == "y":
                        del data[i]
                        print("Item telah berhasil dihapus")
                    elif op == "n" or op == "N" :
                        print("Kembali ke Menu")
        else:
            print("Tidak ada item dengan ID tersebut")
    elif ID[0] == "C":
        if IsFound(ID, consumableData):
            for i in range(len(consumableData)):
                if data[i]["id"] == ID:
                    print("Apakah anda ingin menghapus " + data[i]["nama"] + "? (yYnN)")
                    if op == "Y" or op == "y":
                        del data[i]
                        print("Item telah berhasil dihapus")
                    elif op == "n" or op == "N" :
                        print("Kembali ke Menu")
        else:
            print("Tidak ada item dengan ID tersebut")
    else:
        print("Tidak ada item dengan ID tersebut")      