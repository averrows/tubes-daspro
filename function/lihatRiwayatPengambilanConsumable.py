from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal #pylint: disable=import-error

def printDataDariAkhir(consumableHistoryData, n, userData, consumableData):
    jumlahData = len(consumableHistoryData)
    for i in range((jumlahData - 1), (jumlahData - n - 1), -1):
        susunanPrint(i, consumableHistoryData, userData, consumableData)
        print("")

def cariNamaPengambil(userData, id_pengambil):
    for i in range (1, len(userData)):
        if id_pengambil == userData[i]["id"]:
            nama_pengambil = userData[i]["nama"]
    return nama_pengambil

def cariNamaConsumable(consumableData, id_consumable):
    for i in range(1, len(consumableData)):
        if id_consumable == consumableData[i]["id"]:
            nama_consumable = consumableData[i]["nama"]
    return nama_consumable

def susunanPrint(i, consumableHistoryData, userData, consumableData):
    id_pengambil = consumableHistoryData[i]['id_pengambil']
    id_consumable = consumableHistoryData[i]['id_consumable']
    print("ID Pengambilan        : " + consumableHistoryData[i]["id"])
    print("Nama Pengambil        : " + cariNamaPengambil(userData, id_pengambil))
    print("Nama Consumable       : " + cariNamaConsumable(consumableData, id_consumable))
    print("Tanggal Pengambilan   : " + consumableHistoryData[i]["tanggal_pengambilan"])
    print("Jumlah                : " + consumableHistoryData[i]["jumlah"])

def lihatRiwayatPengambilanConsumable(consumableHistoryData, userData, consumableData):
    # validasi data tidak kosong
    if ((len(consumableHistoryData) == 1)):
        print("Ups, maaf! Data tidak ditemukan (っ °Д °;)っ")
    else:
        # duplikasi data original dan diurutkan berdasarkan tanggal
        data = consumableHistoryData[:]
        urutDataBerdasarTanggal(data)
        if (len(data) <= 5):
            printDataDariAkhir(data, len(data), userData, consumableData)
            print("Kamu di halaman terakhir! (o゜▽゜)o☆ \nKembali ke menu utama....")
        else:
            halaman = 1
            print("-"*25 + f" HALAMAN {halaman} " + "-"*25)
            printDataDariAkhir(data, 5, userData, consumableData)
            kondisi = True
            while (kondisi == True):
                printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
                print("")
                while not((printSisa == 'Y') or (printSisa == 'y') or (printSisa == 'N') or (printSisa == 'n')):
                    print("Masukan invalid!")
                    printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
                if (printSisa == 'Y') or (printSisa == 'y'):
                    del data[(len(data) - 5):(len(data) + 1)]
                    halaman += 1
                    print("-"*25 + f" HALAMAN {halaman} " + "-"*25)
                    if (len(data) > 5):
                        printDataDariAkhir(data, 5, userData, consumableData)
                    else:
                        printDataDariAkhir(data, (len(data) - 1), userData, consumableData)
                        kondisi = False
                        print("Kamu di halaman terakhir! (o゜▽゜)o☆ \nKembali ke menu utama....")
                else:
                    kondisi = False
                    print("Kembali ke menu utama....")