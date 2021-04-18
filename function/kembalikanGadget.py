from CsvTools import parseCSV
userData = parseCSV("data" + "/user.csv")
gadgetData = parseCSV("data" + "/gadget.csv")
gadgetBorrowHistoryData = parseCSV("data" + "/gadget_borrow_history.csv")
gadgetReturnHistoryData = parseCSV("data" + "/gadget_return_history.csv")

def daftarIDPinjamanUser(username, gadgetBorrowHistoryData):
    # membuat array berisi daftar ID gadget yang dipinjam seorang user
    daftarPinjaman = []
    for i in range(len(gadgetBorrowHistoryData)):
        if (username == gadgetBorrowHistoryData[i]['id_peminjam']):
            daftarPinjaman.append(gadgetBorrowHistoryData[i]['id_gadget'])
    return daftarPinjaman

def convertDaftarIDKeNama(daftarPinjaman, gadgetData):
    # mengubah array ID gadget pinjaman menjadi array nama gadget
    daftarNamaGadgetPinjaman = []
    for i in range(len(daftarPinjaman)):
        for j in range(len(gadgetData)):
            if (daftarPinjaman[i] == gadgetData[j]['id']):
                daftarNamaGadgetPinjaman.append(gadgetData[j]['nama'])
    return daftarNamaGadgetPinjaman

def kembalikanGadget(daftarNamaGadgetPinjaman):
    # mencetak daftar pinjaman gadget
    for i in range(len(daftarNamaGadgetPinjaman)):
        print(str(i+1) + ". " + daftarNamaGadgetPinjaman[i])
    print()

    # memilih gadget yang ingin dikembalikan & jumlah yang ingin dikembalikan
    nomorGadget = int(input("Masukkan nomor peminjaman: "))
    jumlahPengembalian = int(input(f"Masukkan jumlah {daftarNamaGadgetPinjaman[nomorGadget - 1]} yang ingin dikembalikan: "))


username = 'rojapthecat'
daftarPinjaman = daftarIDPinjamanUser(username, gadgetBorrowHistoryData)
daftarNamaGadgetPinjaman = convertDaftarIDKeNama(daftarPinjaman, gadgetData)
kembalikanGadget(daftarNamaGadgetPinjaman)