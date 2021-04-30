from function.urutDataBerdasarkanTanggal import urutDataBerdasarTanggal #pylint: disable=import-error

def printDataDariAkhir(consumableHistoryData, n, userData, consumableData):
    jumlahData = len(1, consumableHistoryData)
    for i in range((jumlahData - 1), (jumlahData - n - 1), -1):
        printRiwayat(i, consumableHistoryData, userData, consumableData)
        print("")

def cariNamaPengambil(userData, consumableHistoryData, id_pengambilan):
    for i in range (1, len(consumableHistoryData)):
        if id_pengambilan == consumableHistoryData[i]["id"]:
            id_pengambil = consumableHistoryData[i]["id_pengambil"]
    for i in range (1, len(userData)):
        if id_pengambil == userData[i]["id"]:
            nama_pengambil = userData[i]["nama"]
    return nama_pengambil

def cariNamaConsumable(consumableData, consumableHistoryData, id_peminjam):
    for i in range(1, len(consumableHistoryData)):
        if id_pengambilan == consumableHistoryData[i]["id"]:
            id_consumable = consumableHistoryData[i]["id_consumable"]
    for i in range(1, len(userData)):
        if id_consumable == consumableHistoryData[i]["id"]:
            nama_consumable = consumableData[i]["nama"]
    return nama_consumable

def printRiwayat(i, consumableHistoryData, userData, consumableData):
    id_pengambilan = consumableHistoryData
    print("ID Pengambilan        : " + consumableHistoryData[i]["id"])
    print("Nama pengambil        : " + cariNamaPengambil(userData, consumableHistoryData, id_pengambilan))
    print("Nama Consumable       : " + cariNamaConsumable(consumableData, consumableHistoryData, id_peminjam))
    print("Tanggal Pengambilan   : " + consumableHistoryData[i][""])
    print("Jumlah                : " + consumableHistoryData[i][""])

def riwayatambil(consumableHistoryData, userData, consumableData):
    # validasi data tidak kosong
    if ((len(consumableHistoryData) == 1) or (len(consumableData) == 1) or (len(userData) == 1)):
        print("Maaf, data tidak tersedia!")
    else:
        # duplikasi data original dan menghapus element header pada array
        data = consumableHistoryData[:]
        data.pop(0)
        urutDataBerdasarTanggal(data)
        jumlahData = len(data)
        if (jumlahData <= 5):
            printDataDariAkhir(data, jumlahData, userData, consumableData)
        else:
            printDataDariAkhir(data, 5, userData, consumableData)
            printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
            while not((printSisa == 'Y') or (printSisa == 'y') or (printSisa == 'N') or (printSisa == 'n')):
                print("Masukan invalid!")
                printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
            if (printSisa == 'Y') or (printSisa == 'y'):
                data_copy = data[:]
                del data_copy[(jumlahData - 5):(jumlahData + 1)]
                print("")
                if ((len(data_copy)) > 5):
                    printDataDariAkhir(data_copy, 5, userData, consumableData)
                else:
                    printDataDariAkhir(data_copy, len(data_copy), userData, consumableData)
            else:
                pass