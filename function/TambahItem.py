# from CsvTools import parseCSV
# gadgetData = parseCSV("data" + "/gadget.csv")
# consumableData = parseCSV("data" + "/consumable.csv")

def tambahitem(datas):
    ID = input("Masukkan ID: ")
    IDSama = len(ID)
    if ID[0] == "G":
        gadgetData = datas["gadgetData"]
        for tiapgadget in gadgetData:
            ID1 = ID[1:]
            ID2 = tiapgadget["id"][1:]
            for i in range (IDSama, 0, -1):
                if ID1[i] == ID2[i]:
                    IDSama += 1                
                else :
                    gadgettambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    gadgettambahan["id"] = ID1
                    gadgettambahan["nama"] = input()
                    gadgettambahan["deskripsi"] = input()
                    gadgettambahan["jumlah"] = input()
                    gadgettambahan["rarity"] = input()
                if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                    gadgettambahan["tahun"] = int(input())
                    gadgetData.append(gadgettambahan)
                else :
                    print("Input Rarity Tidak Valid!")
            if IDSama == len(ID):
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                gadgettambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                gadgettambahan["id"] = ID1
                gadgettambahan["nama"] = input()
                gadgettambahan["deskripsi"] = input()
                gadgettambahan["jumlah"] = input()
                gadgettambahan["rarity"] = input()
                if gadgettambahan["rarity"] == "C" or gadgettambahan["rarity"] == "B" or gadgettambahan["rarity"] == "A" or gadgettambahan["rarity"] == "S":
                    gadgettambahan["tahun"] = int(input())
                    gadgetData.append(gadgettambahan)
    elif ID[0] == "C":
        consumableData = datas["consumableData"]
        for tiapconsumable in consumableData:
            ID1 = ID[1:]
            ID2 = tiapconsumable["id"][1:]
            for i in range (IDSama, 0, -1):
                if ID1[i] == ID2[i]:
                    IDSama += 1                
                else :
                    consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                    consumabletambahan["id"] = ID1
                    consumabletambahan["nama"] = input()
                    consumabletambahan["deskripsi"] = input()
                    consumabletambahan["jumlah"] = input()
                    consumabletambahan["rarity"] = input()
                    if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                        consumableData.append(consumabletambahan)
                    else :
                        print("Input Rarity Tidak Valid!")
            if IDSama == len(ID):
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                consumabletambahan = {"id":"", "nama":"", "deskripsi":"", "jumlah":"", "rarity":"", "tahun ditemukan":""}
                consumabletambahan["id"] = ID1
                consumabletambahan["nama"] = input()
                consumabletambahan["deskripsi"] = input()
                consumabletambahan["jumlah"] = input()
                consumabletambahan["rarity"] = input()
                if consumabletambahan["rarity"] == "C" or consumabletambahan["rarity"] == "B" or consumabletambahan["rarity"] == "A" or consumabletambahan["rarity"] == "S":
                    consumableData.append(consumabletambahan)
                else :
                    print("Input Rarity Tidak Valid!")
    else: #ID[0] != "C" and ID[0] != "G"
        print("Gagal menambahkan item karena ID tidak valid.")