from function.CsvTools import parseCSV # pylint: disable=import-error
userData = parseCSV("data" + "/user.csv")
gadgetData = parseCSV("data" + "/gadget.csv")
gadgetBorrowHistoryData = parseCSV("data" + "/gadget_borrow_history.csv")
gadgetReturnHistoryData = parseCSV("data" + "/gadget_return_history.csv")

import datetime

def daftarIDPinjamanUser(username, gadgetBorrowHistoryData):
    # membuat array berisi daftar ID gadget yang dipinjam seorang user
    daftarPinjaman = []
    for i in range(len(gadgetBorrowHistoryData)):
        if (username == gadgetBorrowHistoryData[i]['id_peminjam']) and (gadgetBorrowHistoryData[i]['is_returned'] != '1'):
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

def kembalikanGadget(username, daftarNamaGadgetPinjaman, gadgetBorrowHistoryData, gadgetReturnHistoryData):
    # mencetak daftar pinjaman gadget
    for i in range(len(daftarNamaGadgetPinjaman)):
        print(str(i+1) + ". " + daftarNamaGadgetPinjaman[i])
    print()

    # memilih gadget yang ingin dikembalikan dan jumlah pengembalian
    nomorGadget = int(input("Masukkan nomor peminjaman: "))
    while (nomorGadget > (len(daftarNamaGadgetPinjaman) + 1)):
        print("Nomor peminjaman tidak ada!")
        nomorGadget = int(input("Masukkan nomor peminjaman: "))
    nama_selected_gadget = daftarNamaGadgetPinjaman[nomorGadget - 1]
    id_selected_gadget = cariIDGadget(nama_selected_gadget, gadgetData)
    jumlahPengembalian = int(input(f"Masukkan jumlah {nama_selected_gadget} yang ingin dikembalikan: "))

    # memeriksa apakah barang sudah pernah dikembalikan parsial atau belum
    for i in range (len(gadgetBorrowHistoryData)):
        if (id_selected_gadget == gadgetBorrowHistoryData[i]['id_gadget']):
            cek_returned = gadgetBorrowHistoryData[i]['is_returned']
            jumlahPeminjaman = gadgetBorrowHistoryData[i]['jumlah']
            id_peminjaman = gadgetBorrowHistoryData[i]['id']

    # penyesuaian jumlah gadget pada data
    if (cek_returned == '0'):     # tidak pernah dikembalikan sama sekali
        while (jumlahPengembalian > jumlahPeminjaman):
            print("Jumlah peminjaman tidak mencukupi!")
            jumlahPengembalian = int(input(f"Masukkan jumlah {nama_selected_gadget} yang ingin dikembalikan: "))
        for i in range (len(gadgetData)):
            if (id_selected_gadget == gadgetData[i]['id']):
                gadgetData[i]['jumlah'] = gadgetData[i]['jumlah'] + jumlahPengembalian
        sisaAkhirPengembalian = jumlahPeminjaman - jumlahPengembalian
    else:                       # pernah dikembalikan secara parsial
        for i in range (len(gadgetReturnHistoryData)):
            if (id_peminjaman == gadgetReturnHistoryData[i]['id_peminjaman']) and (gadgetReturnHistoryData[i]['last_returned'] == 'True'):
                sisaAwalPengembalian = int(gadgetReturnHistoryData[i]['sisa_pengembalian'])
                gadgetReturnHistoryData[i]['last_returned'] = 'False'
        while (jumlahPengembalian > sisaAwalPengembalian):
            print("Jumlah peminjaman tidak mencukupi!")
            jumlahPengembalian = int(input(f"Masukkan jumlah {nama_selected_gadget} yang ingin dikembalikan: "))
        for i in range (len(gadgetData)):
            if (id_selected_gadget == gadgetData[i]['id']):
                gadgetData[i]['jumlah'] = gadgetData[i]['jumlah'] + jumlahPengembalian
        sisaAkhirPengembalian = sisaAwalPengembalian - jumlahPengembalian

    # ubah nilai flag is_returned
    for i in range (len(gadgetBorrowHistoryData)):
        if (id_selected_gadget == gadgetBorrowHistoryData[i]['id_gadget']):
            if (sisaAkhirPengembalian == 0):
                gadgetBorrowHistoryData[i]['is_returned'] = '1'
            else:
                gadgetBorrowHistoryData[i]['is_returned'] = '2'

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
    tanggal_pengembalian = x.strftime("%d") + "/" + x.strftime("%m") + "/" + x.strftime("%Y")

    # gadget berhasil dikembalikan
    print(f"Item {nama_selected_gadget} (x{jumlahPengembalian}) telah dikembalikan.")

    # penggabungan data baru dan lama
    id_new_return_data = str(len(gadgetReturnHistoryData) + 1)
    new_return_data = {
        'id': id_new_return_data,
        'id_peminjaman': str(id_peminjaman),
        'tanggal_pengembalian': tanggal_pengembalian,
        'jumlah_pengembalian': str(jumlahPengembalian),
        'sisa_pengembalian': str(sisaAkhirPengembalian),
        'last_returned': 'True'
        }
    gadgetReturnHistoryData.append(new_return_data)

def kembalikanGadgetMain(username, gadgetBorrowHistoryData, gadgetReturnHistoryData, gadgetData):
    # mengubah nilai string angka ke data integer untuk perhitungan
    for i in range(len(gadgetBorrowHistoryData)):
        gadgetBorrowHistoryData[i]['jumlah'] = int(gadgetBorrowHistoryData[i]['jumlah'])
    for i in range(len(gadgetData)):
        gadgetData[i]['jumlah'] = int(gadgetData[i]['jumlah'])
    
    # prosedur
    daftarPinjaman = daftarIDPinjamanUser(username, gadgetBorrowHistoryData)
    if (len(daftarPinjaman) != 0):
        daftarNamaGadgetPinjaman = convertDaftarIDKeNama(daftarPinjaman, gadgetData)
        kembalikanGadget(username, daftarNamaGadgetPinjaman, gadgetBorrowHistoryData, gadgetReturnHistoryData)
    else:       # tidak ada barang yang dipinjam
        print("Tidak ada barang yang dapat dikembalikan!")

    # mengubah kembali data integer ke string angka
    for i in range(len(gadgetBorrowHistoryData)):
        gadgetBorrowHistoryData[i]['jumlah'] = str(gadgetBorrowHistoryData[i]['jumlah'])
    for i in range(len(gadgetData)):
        gadgetData[i]['jumlah'] = str(gadgetData[i]['jumlah'])
