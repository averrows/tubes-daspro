# from CsvTools import parseCSV
# gadgetData = parseCSV("data" + "/gadget.csv")
# historyData = parseCSV("data" + "/2_gadget_borrow_history.csv")
from function.kembalikanGadget import validasiTanggal # pylint: disable=import-error
def pinjamGadget(dataGadget,dataRiwayat,idPeminjam):
    #Tanpa pemilihan nama dan id, hanya id saja
    idItem = input("Masukkan ID item: ")
    dataItem =isIdItemAda(idItem,dataGadget)
    if dataItem["keberadaan"]:
        # print("Tanggal Peminjaman: "+str(waktuSekarang.day)+"/"+str(waktuSekarang.month)+"/"+str(waktuSekarang.year))
        jumlahTersedia = int(dataGadget[dataItem["indeks"]]["jumlah"])
        namaGadget = dataGadget[dataItem["indeks"]]["nama"]
        print("Gadget tersebut adalah "+namaGadget)
        print(namaGadget + " tersedia sejumlah "+ str(jumlahTersedia))
        jumlahPeminjaman = int(input("Jumlah peminjaman: "))
        if jumlahTersedia >=  jumlahPeminjaman:
            jadiPinjam = input("Apakah jadi meminjam?")
            if jadiPinjam == "y" or jadiPinjam == "Y":
                dataGadget[dataItem["indeks"]]["jumlah"] = str(jumlahTersedia - jumlahPeminjaman)
                print("Kamu ada di 'kapan'?")
                day = int(input())
                month = int(input())
                year = int(input())
                validasiTanggal(day,)
                tanggal = str(day)+"/"+str(month)+"/"+str(year)
                dataRiwayatBaru = {
                    "id":dataRiwayat[len(dataRiwayat)-1]["id"][1:],
                    "id_peminjam":idPeminjam,
                    "id_gadget":idItem,
                    "tanggal_peminjaman":tanggal,
                    "jumlah":jumlahPeminjaman,
                    "is_returned": 0
                    }
                dataRiwayat.append(dataRiwayatBaru)
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
    indeks = 0
    for i in range(1,len(data)):
        if data[i]["id"] == id:
            return {"keberadaan":True,"indeks":indeks}
        indeks += 1
    return {"keberadaan":False}
    
