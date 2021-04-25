from CsvTools import parseCSV

userData = parseCSV("data" + "/user.csv")
gadgetData = parseCSV("data" + "/gadget.csv")
gadgetBorrowHistoryData = parseCSV("data" + "/gadget_borrow_history.csv")
gadgetReturnHistoryData = parseCSV("data" + "/gadget_return_history.csv")

def printDataDariAkhir(gadgetReturnHistoryData, n):
    jumlahData = len(gadgetReturnHistoryData)
    for i in range((jumlahData - 1), (jumlahData - n - 1), -1):
        susunanPrint(i, gadgetReturnHistoryData)
        print("")

def cariNamaPengambil(userData, gadgetBorrowHistoryData, id_peminjaman):
    for i in range(len(gadgetBorrowHistoryData)):
        if (id_peminjaman == gadgetBorrowHistoryData[i]['id']):
            id_peminjam = gadgetBorrowHistoryData[i]['id_peminjam']
    for i in range(len(userData)):
        if (id_peminjam == userData[i]['username']):
            nama_pengambil = userData[i]['nama']
    return nama_pengambil

def cariNamaGadget(gadgetData, gadgetBorrowHistoryData, id_peminjaman):
    for i in range(len(gadgetBorrowHistoryData)):
        if (id_peminjaman == gadgetBorrowHistoryData[i]['id']):
            id_gadget = gadgetBorrowHistoryData[i]['id_gadget']
    for i in range(len(gadgetData)):
        if (id_gadget == gadgetData[i]['id']):
            nama_gadget = gadgetData[i]['nama']
    return nama_gadget

def susunanPrint(i, gadgetReturnHistoryData):
    id_peminjaman = gadgetReturnHistoryData[i]['id_peminjaman']
    print("ID Pengembalian      : " + gadgetReturnHistoryData[i]['id'])
    print("Nama Pengambil       : " + cariNamaPengambil(userData, gadgetBorrowHistoryData, id_peminjaman))
    print("Nama Gadget          : " + cariNamaGadget(gadgetData, gadgetBorrowHistoryData, id_peminjaman))
    print("Jumlah Pengembalian  : " + gadgetReturnHistoryData[i]['jumlah_pengembalian'])
    print("Tanggal Pengembalian : " + gadgetReturnHistoryData[i]['tanggal_pengembalian'])

def lihatRiwayatKembalikanGadget(gadgetReturnHistoryData):
    jumlahData = len(gadgetReturnHistoryData)
    if (jumlahData == 0):
        print("Belum ada pengembalian gadget dilakukan!")
    elif (jumlahData <= 5):
        printDataDariAkhir(gadgetReturnHistoryData, jumlahData)
    else:
        printDataDariAkhir(gadgetReturnHistoryData, 5)
        printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
        while not((printSisa == 'Y') or (printSisa == 'y') or (printSisa == 'N') or (printSisa == 'n')):
            print("Masukan invalid!")
            printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
        if (printSisa == 'Y') or (printSisa == 'y'):
            gadgetReturnHistoryData_copy = gadgetReturnHistoryData[:]
            del gadgetReturnHistoryData_copy[(jumlahData - 5):(jumlahData + 1)]
            if ((len(gadgetReturnHistoryData_copy)) > 5):
                printDataDariAkhir(gadgetReturnHistoryData_copy, 5)
            else:
                printDataDariAkhir(gadgetReturnHistoryData_copy, len(gadgetReturnHistoryData_copy))
        else:
            pass

# data belum di-sort