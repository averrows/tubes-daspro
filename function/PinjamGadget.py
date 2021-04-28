# from CsvTools import parseCSV
# gadgetData = parseCSV("data" + "/gadget.csv")
# historyData = parseCSV("data" + "/2_gadget_borrow_history.csv")
from function.kembalikanGadget import validasiTanggal # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal # pylint: disable=import-error
def pinjamGadget(dataGadget,dataRiwayat,idPeminjam):
    #Tanpa pemilihan nama dan id, hanya id saja
    if len(dataGadget) == 1:
        print("Ups, maaf! Data Gadget masih kosong, belum ada peminjaman dapat dilakukan (っ °Д °;)っ")
    elif len(dataGadget)>1:
        idItem = input("Masukkan ID item: ")
        dataItem =isIdItemAda(idItem,dataGadget)
        if dataItem["keberadaan"]:
            # print("Tanggal Peminjaman: "+str(waktuSekarang.day)+"/"+str(waktuSekarang.month)+"/"+str(waktuSekarang.year))
            jumlahTersedia = int(dataGadget[dataItem["indeks"]]["jumlah"])
            namaGadget = dataGadget[dataItem["indeks"]]["nama"]
            print("Gadget tersebut adalah "+namaGadget)
            print(namaGadget + " tersedia sejumlah "+ str(jumlahTersedia))
            jumlahPeminjaman = int(input("Masukkan jumlah yang ingin dipinjam: "))
            if jumlahTersedia >=  jumlahPeminjaman:
                jadiPinjam = input("Apakah jadi meminjam?(Yy)")
                if jadiPinjam == "y" or jadiPinjam == "Y":
                    dataGadget[dataItem["indeks"]]["jumlah"] = str(jumlahTersedia - jumlahPeminjaman)
                    print("Kamu ada di 'kapan'?")
                    masukkanTanggal = False
                    while not masukkanTanggal:
                        day = int(input("Masukkan tanggal:"))
                        month = int(input("Masukkan bulan:"))
                        year = int(input("Masukkan tahun:"))
                        masukkanTanggal = validasiTanggal(day,month,year)
                        if masukkanTanggal == False:
                            print("Tanggal yang dimasukkan tidak ada, harap masukkan ulang")
                    tanggal = str(day)+"/"+str(month)+"/"+str(year)
                    dataRiwayatBaru = {
                        "id":str(5), #masih masalah,
                        "id_peminjam":idPeminjam,
                        "id_gadget":idItem,
                        "tanggal_peminjaman":tanggal,
                        "jumlah":str(jumlahPeminjaman),
                        "is_returned": str(0)
                        }
                    dataRiwayat.append(dataRiwayatBaru)
                    urutDataBerdasarTanggal(dataRiwayat)
                    print("Peminjaman {}(x{}) berhasil dilakukan oleh {} pada tanggal {}".format(
                        namaGadget,str(jumlahPeminjaman),idPeminjam,tanggal
                    ))
                else:
                    pass
            else:
                print("Jumlah tidak cukup")
        else:
            print("Gadget dengan ID tersebut tidak ada")
def isIdItemAda(id,data):
    #Input : id, data
    #Output : dictionary
    indeks = 1
    for i in range(1,len(data)):
        if data[i]["id"] == id:
            return {"keberadaan":True,"indeks":indeks}
        indeks += 1
    return {"keberadaan":False}
    
