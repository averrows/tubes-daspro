from CsvTools import parseCSV
userData = parseCSV("data" + "/user.csv")
gadgetData = parseCSV("data" + "/gadget.csv")
gadgetBorrowHistoryData = parseCSV("data" + "/gadget_borrow_history.csv")
gadgetReturnHistoryData = parseCSV("data" + "/gadget_return_history.csv")

import datetime

def convertToInteger_BorrowHistory(gadgetBorrowHistoryData):
    # mengubah nilai string angka ke data integer agar dapat dikalkulasikan
    for i in range(len(gadgetBorrowHistoryData)):
        gadgetBorrowHistoryData[i]['jumlah'] = int(gadgetBorrowHistoryData[i]['jumlah'])
        gadgetBorrowHistoryData[i]['sisa_peminjaman'] = int(gadgetBorrowHistoryData[i]['sisa_peminjaman'])

def convertToInteger_GadgetData(gadgetData):
    # mengubah nilai string angka ke data integer agar dapat dikalkulasikan
    for i in range(len(gadgetData)):
        gadgetData[i]['jumlah'] = int(gadgetData[i]['jumlah'])

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

def validasiTanggal(tanggal, bulan, tahun):
    # kabisat = habis dibagi 4 dan tidak habis dibagi 100. atau habis dibagi 400
    # kabisat bulan februarinya 29
    if (bulan == 1) or (bulan == 3) or (bulan == 5) or (bulan == 7) or (bulan == 8) or (bulan == 10) or (bulan == 12):
        if (tanggal >= 1) and (tanggal <= 31):
            return True
        else:
            return False
    elif (bulan == 4) or (bulan == 6) or (bulan == 9) or (bulan == 11):
        if (tanggal >=1) and (tanggal <= 30):
            return True
        else:
            return False
    elif (bulan == 2):
        if ((tahun % 4 == 0) and (tahun % 100 != 0)) or (tahun % 400 == 0):
            if (tanggal >=1) and (tanggal <= 29):
                return True
            else:
                return False
        else:
            if (tanggal >= 1) and (tanggal <= 28):
                return True
            else:
                return False
    else:
        return False

def cariIDGadget (nama_selected_gadget, gadgetData):
    for i in range (len(gadgetData)):
        if (nama_selected_gadget == gadgetData[i]['nama']):
            id_selected_gadget = gadgetData[i]['id']
    return id_selected_gadget

def kembalikanGadget(username, daftarNamaGadgetPinjaman, gadgetBorrowHistoryData):
    # mencetak daftar pinjaman gadget
    for i in range(len(daftarNamaGadgetPinjaman)):
        print(str(i+1) + ". " + daftarNamaGadgetPinjaman[i])
    print()

    # memilih gadget yang ingin dikembalikan & jumlah yang ingin dikembalikan
    nomorGadget = int(input("Masukkan nomor peminjaman: "))
    nama_selected_gadget = daftarNamaGadgetPinjaman[nomorGadget - 1]
    id_selected_gadget = cariIDGadget(nama_selected_gadget, gadgetData)
    for i in range (len(gadgetBorrowHistoryData)):
        if (id_selected_gadget == gadgetBorrowHistoryData[i]['id_gadget']):
            sisa_peminjaman = gadgetBorrowHistoryData[i]['sisa_peminjaman']
    jumlahPengembalian = int(input(f"Masukkan jumlah {nama_selected_gadget} yang ingin dikembalikan: "))
    while (jumlahPengembalian > int(sisa_peminjaman)):
        print("Jumlah peminjaman tidak mencukupi!")
        jumlahPengembalian = int(input(f"Masukkan jumlah {nama_selected_gadget} yang ingin dikembalikan: "))

    # pengurangan data gadget
    for i in range (len(gadgetBorrowHistoryData)):
        if (id_selected_gadget == gadgetBorrowHistoryData[i]['id_gadget']):
            gadgetBorrowHistoryData[i]['sisa_peminjaman'] = gadgetBorrowHistoryData[i]['sisa_peminjaman'] - jumlahPengembalian
    for j in range (len(gadgetData)):
        if (id_selected_gadget == gadgetData[j]['id']):
            gadgetData[j]['jumlah'] = gadgetData[j]['jumlah'] + jumlahPengembalian

    # input dan validasi tanggal pengembalian
    tanggal = int(input("Masukkan tanggal pengembalian: "))
    bulan = int(input("Masukkan bulan pengembalian: "))
    tahun = int(input("Masukkan tahun pengembalian: "))
    while (validasiTanggal(tanggal, bulan, tahun) == False):
        print("Tanggal tidak valid!")
        tanggal = int(input("Masukkan tanggal pengembalian: "))
        bulan = int(input("Masukkan bulan pengembalian: "))
        tahun = int(input("Masukkan tahun pengembalian: "))
    x = datetime.datetime(tahun, bulan, tanggal)
    tanggal_pengembalian = x.strftime("%x")

    # gadget berhasil dikembalikan
    print(f"Item {nama_selected_gadget} (x{jumlahPengembalian}) telah dikembalikan.")

    # penggabungan data baru dan lama
    id_new_return_data = str(len(gadgetReturnHistoryData) + 1)
    new_return_data = {'id': id_new_return_data, 'id_peminjam': username, 'id_gadget': id_selected_gadget, 'tanggal_pengembalian': tanggal_pengembalian, 'jumlah_pengembalian': str(jumlahPengembalian)}
    gadgetReturnHistoryData.append(new_return_data)

# variabel username merupakan input dari user yang disimpan ketika proses login
convertToInteger_BorrowHistory(gadgetBorrowHistoryData)
convertToInteger_GadgetData(gadgetData)
daftarPinjaman = daftarIDPinjamanUser(username, gadgetBorrowHistoryData)
daftarNamaGadgetPinjaman = convertDaftarIDKeNama(daftarPinjaman, gadgetData)
kembalikanGadget(username, daftarNamaGadgetPinjaman, gadgetBorrowHistoryData)