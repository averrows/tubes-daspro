# from CsvTools import parseCSV
# gadgetData = parseCSV("data" + "/gadget.csv")
# historyData = parseCSV("data" + "/2_gadget_borrow_history.csv")
import datetime

from function.kembalikanGadget import validasiTanggal # pylint: disable=import-error
from function.kembalikanGadget import validasiAngka # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal # pylint: disable=import-error

def cekPinjam(idItem,dataRiwayat):
    for i in range(1, len(dataRiwayat)):
        if (idItem == dataRiwayat[i]['id_gadget']) and (dataRiwayat[i]['is_returned'] != 1):
            return False    # Gadget sedang dipinjam user
    return True             # Gadget tidak sedang dipinjam user

def pinjamGadget(dataGadget,dataRiwayat,idPeminjam):
    #Tanpa pemilihan nama dan id, hanya id saja
    if len(dataGadget) == 1:
        print("Ups, maaf! Data Gadget masih kosong, peminjaman belum dapat dilakukan (っ °Д °;)っ")
    elif len(dataGadget)>1:
        idItem = input("Masukkan ID item: ")
        dataItem =isIdItemAda(idItem,dataGadget)
        if (dataItem["keberadaan"]) and (cekPinjam(idItem, dataRiwayat) == True):
            # print("Tanggal Peminjaman: "+str(waktuSekarang.day)+"/"+str(waktuSekarang.month)+"/"+str(waktuSekarang.year))
            jumlahTersedia = int(dataGadget[dataItem["indeks"]]["jumlah"])
            namaGadget = dataGadget[dataItem["indeks"]]["nama"]
            print("Gadget tersebut adalah "+namaGadget)
            print(namaGadget + " tersedia sejumlah "+ str(jumlahTersedia))
            jumlahPeminjaman = int(input("Masukkan jumlah yang ingin dipinjam: "))
            if jumlahTersedia >=  jumlahPeminjaman:
                jadiPinjam = input("Apakah jadi meminjam? (Yy): ")
                if jadiPinjam == "y" or jadiPinjam == "Y":
                    dataGadget[dataItem["indeks"]]["jumlah"] = str(jumlahTersedia - jumlahPeminjaman)
                    print("Kamu ada di 'kapan'?")
                    masukkanTanggal = False
                    while not masukkanTanggal:
                        # tanggal
                        day = input("Masukkan tanggal: ")
                        while (validasiAngka(day) == False):
                            print("Masukkan angka! (˘･_･˘)")
                            day = input("Masukkan tanggal: ")
                        day = int(day)
                        # bulan
                        month = input("Masukkan bulan: ")
                        while (validasiAngka(month) == False):
                            print("Masukkan angka! (˘･_･˘)")
                            month = input("Masukkan bulan: ")
                        month = int(month)
                        # tahun
                        year = input("Masukkan tahun: ")
                        while (validasiAngka(year) == False):
                            print("Masukkan angka! (˘･_･˘)")
                            year = input("Masukkan tahun: ")
                        year = int(year)
                        #validasi
                        masukkanTanggal = validasiTanggal(day, month, year)
                        if masukkanTanggal == False:
                            print("Tanggal yang dimasukkan tidak ada, harap masukkan ulang")
                    dmy = datetime.datetime(year, month, day)
                    tanggal = dmy.strftime("%d") + "/" + dmy.strftime("%m") + "/" + dmy.strftime("%Y")
                    #tanggal = str(day)+"/"+str(month)+"/"+str(year)
                    idBorrow = len(dataRiwayat)
                    dataRiwayatBaru = {
                        "id":str(idBorrow),
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
        elif (dataItem["keberadaan"]) and (cekPinjam(idItem, dataRiwayat) == False):
            print("Gadget tersebut masih kamu pinjam.\nSilahkan kembalikan terlebih dahulu atau pinjam yang lain! ヾ(^▽^*)))")
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
    
