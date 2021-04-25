from CsvTools import parseCSV
from urutDataBerdasarTanggal import *

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
    data = gadgetReturnHistoryData[:]
    urutDataBerdasarTanggal(data)
    jumlahData = len(data)
    if (jumlahData == 0):
        print("Belum ada pengembalian gadget dilakukan!")
    elif (jumlahData <= 5):
        printDataDariAkhir(data, jumlahData)
    else:
        printDataDariAkhir(data, 5)
        printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
        while not((printSisa == 'Y') or (printSisa == 'y') or (printSisa == 'N') or (printSisa == 'n')):
            print("Masukan invalid!")
            printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn): ")
        if (printSisa == 'Y') or (printSisa == 'y'):
            data_copy = data[:]
            del data_copy[(jumlahData - 5):(jumlahData + 1)]
            print("")
            if ((len(data_copy)) > 5):
                printDataDariAkhir(data_copy, 5)
            else:
                printDataDariAkhir(data_copy, len(data_copy))
        else:
            pass

lihatRiwayatKembalikanGadget(gadgetReturnHistoryData)