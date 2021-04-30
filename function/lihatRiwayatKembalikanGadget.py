from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal #pylint: disable=import-error

def printDataDariAkhir(gadgetReturnHistoryData, n, userData, gadgetData, gadgetBorrowHistoryData):
    jumlahData = len(gadgetReturnHistoryData)
    for i in range((jumlahData - 1), (jumlahData - n - 1), -1):
        susunanPrint(i, gadgetReturnHistoryData, userData, gadgetData, gadgetBorrowHistoryData)
        print("")

def cariNamaPengambil(userData, gadgetBorrowHistoryData, id_peminjaman):
    for i in range(1, len(gadgetBorrowHistoryData)):
        if (id_peminjaman == gadgetBorrowHistoryData[i]['id']):
            id_peminjam = gadgetBorrowHistoryData[i]['id_peminjam']
    for i in range(1, len(userData)):
        if (id_peminjam == userData[i]['id']):
            nama_pengambil = userData[i]['nama']
    return nama_pengambil

def cariNamaGadget(gadgetData, gadgetBorrowHistoryData, id_peminjaman):
    for i in range(1, len(gadgetBorrowHistoryData)):
        if (id_peminjaman == gadgetBorrowHistoryData[i]['id']):
            id_gadget = gadgetBorrowHistoryData[i]['id_gadget']
    for i in range(1, len(gadgetData)):
        if (id_gadget == gadgetData[i]['id']):
            nama_gadget = gadgetData[i]['nama']
    return nama_gadget

def susunanPrint(i, gadgetReturnHistoryData, userData, gadgetData,gadgetBorrowHistoryData):
    id_peminjaman = gadgetReturnHistoryData[i]['id_peminjaman']
    print("ID Pengembalian      : " + gadgetReturnHistoryData[i]['id'])
    print("Nama Pengambil       : " + cariNamaPengambil(userData, gadgetBorrowHistoryData, id_peminjaman))
    print("Nama Gadget          : " + cariNamaGadget(gadgetData, gadgetBorrowHistoryData, id_peminjaman))
    print("Jumlah Pengembalian  : " + gadgetReturnHistoryData[i]['jumlah_pengembalian'])
    print("Tanggal Pengembalian : " + gadgetReturnHistoryData[i]['tanggal_pengembalian'])

def lihatRiwayatKembalikanGadget(gadgetReturnHistoryData, userData, gadgetData, gadgetBorrowHistoryData):
    # validasi data tidak kosong
    if (len(gadgetReturnHistoryData) == 1) or (len(gadgetData) == 1) or (len(userData) == 1) or (len(gadgetBorrowHistoryData) == 1):
        print("Ups, maaf! Data tidak ditemukan (っ °Д °;)っ")
    else:
        # duplikasi data original dan diurutkan berdasarkan tanggal
        data = gadgetReturnHistoryData[:]
        urutDataBerdasarTanggal(data)
        if (len(data) <= 5):
            printDataDariAkhir(data, len(data), userData, gadgetData, gadgetBorrowHistoryData)
        else:
            printDataDariAkhir(data, 5, userData, gadgetData, gadgetBorrowHistoryData)
            kondisi = True
            halaman = 0
            while (kondisi == True):
                halaman += 1
                print("-"*25 + f" HALAMAN {halaman} " + "-"*25)
                printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
                while not((printSisa == 'Y') or (printSisa == 'y') or (printSisa == 'N') or (printSisa == 'n')):
                    print("Masukan invalid!")
                    printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
                if (printSisa == 'Y') or (printSisa == 'y'):
                    del data[(len(data) - 5):(len(data) + 1)]
                    print("")
                    if (len(data) > 5):
                        printDataDariAkhir(data, 5, userData, gadgetData, gadgetBorrowHistoryData)
                    else:
                        printDataDariAkhir(data, (len(data) - 1), userData, gadgetData, gadgetBorrowHistoryData)
                        halaman += 1
                        print("-"*25 + f" HALAMAN {halaman} " + "-"*25)
                        kondisi = False
                        print("Kamu di halaman terakhir! (o゜▽゜)o☆ \nKembali ke menu utama....")
                else:
                    kondisi = False
                    print("Kembali ke menu utama....")
