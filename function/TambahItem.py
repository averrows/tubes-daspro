# from CsvTools import parseCSV
# gadgetData = parseCSV("data" + "/gadget.csv")
# consumableData = parseCSV("data" + "/consumable.csv")

def tambahitem(gadgetData,consumableData):
    ID = input("Masukkan ID: ")
    
    def IsNotFound(ID, data):
        found = False
        i = 1
        while i < len(data) and not found:
            if data[i]["id"] == ID:
                found = True
            else:
                i += 1
        if found:
            return False
        else:
            return True
    
    # ALGORITMA
    if ID == "G":
        if IsNotFound(ID, gadgetData):
            gadgettambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
            gadgettambahan["id"] = ID
            gadgettambahan["nama"] = input()
            gadgettambahan["deskripsi"] = input()
            gadgettambahan["jumlah"] = input()
            gadgettambahan["rarity"] = input()
            if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                gadgettambahan["tahun"] = int(input())
                gadgetData.append(gadgettambahan)
            else :
                print("Input Rarity Tidak Valid!")
        else:
            print("Gagal menambahkan item karena ID sudah ada.")
            
    elif ID[0] == "C":
        if IsNotFound(ID, consumableData):
            consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
            consumabletambahan["id"] = ID
            consumabletambahan["nama"] = input()
            consumabletambahan["deskripsi"] = input()
            consumabletambahan["jumlah"] = input()
            consumabletambahan["rarity"] = input()
            if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                consumableData.append(consumabletambahan)
            else :
                print("Input Rarity Tidak Valid!")
        else:
            print("Gagal menambahkan item karena ID sudah ada.")

    else: #ID[0] != "C" and ID[0] != "G"
        print("Gagal menambahkan item karena ID tidak valid.")