import datetime

from function.kembalikanGadget import validasiTanggal  # pylint: disable=import-error
from function.kembalikanGadget import validasiAngka  # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal  # pylint: disable=import-error

yakinSkript = """
Apakah kamu yakin ingin meminjam {} sebanyak {}?
    1 Yakin
    2 Ubah Jumlah
    3 Ubah Item
    0 Kembali """
pinjamSkript = """Halo {}, kamu ingin pinjam apa?
    Tekan:
        1 "Aku tahu ID gadget yang mau aku pinjam Dora !!!"
        2 "Aku cuma tahu beberapa katanya Dora !!!" -----Bingung Aku
        0 "Gajadi minjem ah" """
def dapatkanItem(data,username):
    print(pinjamSkript.format(username))
    tipeMasukan = input(">>> ")
    print("")
    if tipeMasukan == "1":
        return input("Masukkan ID: ")
    elif tipeMasukan == "2":
        key = input("Masukkan kata berkaitan gadget itu yang kamu ingat: ")
        print("\n")
        listGadgetSesuai = cariBendaReturnId(key, data)
        jumlahGadgetSesuai = len(listGadgetSesuai)
        if jumlahGadgetSesuai == 0:
            print("Tidak ada gadget yang sesuai dengan kata kunci tersebut")
            return "0000000"
        elif jumlahGadgetSesuai > 0:
            i = 1
            for item in listGadgetSesuai:
                print("Ketik {} untuk gadget ini".format(i))
                print("Nama        : {}".format(item["nama"]))
                print("Deskripsi   : {}".format(item["deskripsi"]))
                print("\n")
                i += 1
            pilihanGadget = input(">>> ")
            while not (validasiAngka(pilihanGadget) and (int(pilihanGadget)>=1 and int(pilihanGadget) <= len(listGadgetSesuai) )):
                print("Masukkan pilihan yang benar")
                pilihanGadget = input(">>> ")
            
            indeksPilihan = int(pilihanGadget) - 1
            return listGadgetSesuai[indeksPilihan]["id"]
    elif tipeMasukan == "0":
        pass


def cekPinjam(idItem, dataRiwayat):
    for i in range(1, len(dataRiwayat)):
        if (idItem == dataRiwayat[i]['id_gadget']) and (dataRiwayat[i]['is_returned'] != "1"):
            return False    # Gadget sedang dipinjam user
    return True             # Gadget tidak sedang dipinjam user

def getJumlahPeminjaman():
    jumlahPeminjaman = input("Masukkan jumlah yang ingin dipinjam: ")

            # Masukkan jumlah peminjaman
    while (validasiAngka(jumlahPeminjaman) == False):
        print("Masukkan angka! (˘･_･˘)")
        jumlahPeminjaman = input(
        "Masukkan jumlah yang ingin dipinjam: ")
    jumlahPeminjaman = int(jumlahPeminjaman)    
    return jumlahPeminjaman

def pinjamGadget(dataGadget, dataRiwayat, idPeminjam, username):
    # PROSEDUR UMUM PEMINJAMAN
    def prosedurPinjam():
        #PROSEDUR DARI MASUKKAN JUMLAH
        def prosedurMasukkanJumlahToNext():
            #PROSEDUR DIJALANKAN JIKA JADI MEMINJAM
            def prosedurJadiPinjam():    
                dataGadget[dataItem["indeks"]]["jumlah"] = str(
                    jumlahTersedia - jumlahPeminjaman)
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
                    # validasi
                    masukkanTanggal = validasiTanggal(day, month, year)
                    if masukkanTanggal == False:
                        print(
                            "Tanggal yang dimasukkan tidak ada, harap masukkan ulang")
                dmy = datetime.datetime(year, month, day)
                tanggal = dmy.strftime(
                    "%d") + "/" + dmy.strftime("%m") + "/" + dmy.strftime("%Y")
                idBorrow = len(dataRiwayat)
                dataRiwayatBaru = {
                    "id": str(idBorrow),
                    "id_peminjam": idPeminjam,
                    "id_gadget": idItem,
                    "tanggal_peminjaman": tanggal,
                    "jumlah": str(jumlahPeminjaman),
                    "is_returned": str(0)
                }
                dataRiwayat.append(dataRiwayatBaru)
                print("")
                print("Peminjaman {}(x{}) berhasil dilakukan oleh {} pada tanggal {}".format(
                    namaGadget, str(
                        jumlahPeminjaman), username, tanggal
                ))
            
            # masukkan jumlah
            jumlahPeminjaman = getJumlahPeminjaman()

            # lakukan tergantung jumlah peminjaman
            if jumlahPeminjaman == 0:
                print("\nBerarti gak ada yang dipinjam dong... ┌( ´_ゝ` )┐")
            else:
                if jumlahTersedia >= jumlahPeminjaman:
                    #pilihan 1,2,3,0 cek pilihan jadi atau tidak
                    nextChoiceDecided = False
                    while not nextChoiceDecided:
                        print(yakinSkript.format(namaGadget,jumlahPeminjaman))
                        pilihanSelanjutnya = input(">>> ")
                        if pilihanSelanjutnya == "1":
                            nextChoiceDecided = True
                            prosedurJadiPinjam()
                        elif pilihanSelanjutnya == "2":
                            nextChoiceDecided = True
                            prosedurMasukkanJumlahToNext()     
                        elif pilihanSelanjutnya == "3":
                            nextChoiceDecided = True
                            prosedurPinjam()
                        elif pilihanSelanjutnya == "0":
                            nextChoiceDecided = True
                            print("Anda tidak jadi meminjam")
                else:
                    print("Jumlah tidak cukup")               

        idItem = dapatkanItem(dataGadget,username)
        # cek apakah item ada, jika ada, jalankan algoritma
        dataItem = isIdItemAda(idItem, dataGadget)
        if (dataItem["keberadaan"]) and (cekPinjam(idItem, dataRiwayat) == True):
            jumlahTersedia = int(dataGadget[dataItem["indeks"]]["jumlah"])
            indeksGadget = dataItem["indeks"]
            namaGadget = dataGadget[indeksGadget]["nama"]
            print("Gadget tersebut adalah "+namaGadget)
            print(namaGadget + " tersedia sejumlah " + str(jumlahTersedia))
            prosedurMasukkanJumlahToNext()
        elif (dataItem["keberadaan"]) and (cekPinjam(idItem, dataRiwayat) == False):
            print("Gadget tersebut masih kamu pinjam.\nSilahkan kembalikan terlebih dahulu atau pinjam yang lain! ヾ(^▽^*)")
        else:
            print("Gadget dengan ID tersebut tidak ada")
    

    # Tanpa pemilihan nama dan id, hanya id saja
    if len(dataGadget) == 1:
        print("Ups, maaf! Data Gadget masih kosong, peminjaman belum dapat dilakukan (っ °Д °;)っ")
    elif len(dataGadget) > 1:
        prosedurPinjam()




def isIdItemAda(id, data):
    # Input : id, data
    #Output : dictionary
    indeks = 1
    for i in range(1, len(data)):
        if data[i]["id"] == id:
            return {"keberadaan": True, "indeks": indeks}
        indeks += 1
    return {"keberadaan": False}


def cariBendaReturnId(key: str, data: list) -> list:
    # ambil id, nama, dan deskripsi
    # cek apakah dalam nama atau desripsi terdapat string key
    # return yang list berisi id-nya
    hasil = []
    for item in data[1:]:
        if key in item["nama"] or key in item["deskripsi"]:
            hasil.append(item)
    return hasil







