from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal #pylint: disable=import-error

def printDataDariAkhir(gadgetReturnHistoryData, n, userData, gadgetData, gadgetBorrowHistoryData):
    jumlahData = len(1, gadgetReturnHistoryData)
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
        # duplikasi data original dan menghapus element header pada array
        data = gadgetReturnHistoryData[:]
        data.pop(0)
        urutDataBerdasarTanggal(data)
        jumlahData = len(data)
        if (jumlahData <= 5):
            printDataDariAkhir(data, jumlahData, userData, gadgetData, gadgetBorrowHistoryData)
        else:
            printDataDariAkhir(data, 5, userData, gadgetData, gadgetBorrowHistoryData)
            while (jumlahData - 5 > 0):
                printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
                while not((printSisa == 'Y') or (printSisa == 'y') or (printSisa == 'N') or (printSisa == 'n')):
                    print("Masukan invalid!")
                    printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
                if (printSisa == 'Y') or (printSisa == 'y'):
                    del data[(jumlahData - 5):(jumlahData + 1)]
                    print("")
                    if (jumlahData > 5):
                        printDataDariAkhir(data, 5, userData, gadgetData, gadgetBorrowHistoryData)
                    else:
                        printDataDariAkhir(data, jumlahData, userData, gadgetData, gadgetBorrowHistoryData)
                else:
                    pass
