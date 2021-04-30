# from CsvTools import parseCSV
# consumableData = parseCSV("data" + "/consumable.csv")
# historyData = parseCSV("data" + "/2_consumable_borrow_history.csv")
import datetime

from function.kembalikanGadget import validasiTanggal  # pylint: disable=import-error
from function.kembalikanGadget import validasiAngka  # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal  # pylint: disable=import-error

yakinSkript = """
Apakah kamu yakin ingin meminjam {} sebanyak {}?
    1 Yakin
    2 Ubah Jumlah
    3 Ubah Item
    0 Kembali
"""
MintaSkript =    """
Halo {}, kamu ingin Minta apa?
    Tekan:
        1 "Aku tahu ID consumable yang mau aku Minta Dora !!!"
        2 "Aku cuma tahu beberapa katanya Dora !!!" -----Bingung Aku
        0 "Gajadi minjem ah"
"""
def dapatkanItem(data,username):
    print(MintaSkript.format(username))
    tipeMasukan = input(">>> ")
    if tipeMasukan == "1":
        return input("Masukkan ID: ")
    elif tipeMasukan == "2":
        key = input("Masukkan kata berkaitan consumable itu yang kamu ingat: ")
        print("\n")
        listconsumableSesuai = cariBendaReturnId(key, data)
        jumlahconsumableSesuai = len(listconsumableSesuai)
        if jumlahconsumableSesuai == 0:
            print("Tidak ada consumable yang sesuai dengan kata kunci tersebut")
            return "0000000"
        elif jumlahconsumableSesuai > 0:
            i = 1
            for item in listconsumableSesuai:
                print("Ketik {} untuk consumable ini".format(i))
                print("Nama        : {}".format(item["nama"]))
                print("Deskripsi   : {}".format(item["deskripsi"]))
                print("\n")
                i += 1
            pilihanconsumable = input(">>> ")
            while not (validasiAngka(pilihanconsumable) and (int(pilihanconsumable)>=1 and int(pilihanconsumable) <= len(listconsumableSesuai) )):
                print("Masukkan pilihan yang benar")
                pilihanconsumable = input(">>> ")
            
            indeksPilihan = int(pilihanconsumable) - 1
            return listconsumableSesuai[indeksPilihan]["id"]
    elif tipeMasukan == "0":
        pass


def cekMinta(idItem, dataRiwayat):
    for i in range(1, len(dataRiwayat)):
        if idItem == dataRiwayat[i]['id_consumable']:
            return False    # consumable sedang diMinta user
    return True             # consumable tidak sedang diminta user

def getJumlahPerMintaan():
    jumlahPerMintaan = input("Masukkan jumlah yang ingin diminta: ")

            # Masukkan jumlah PerMintaan
    while (validasiAngka(jumlahPerMintaan) == False):
        print("Masukkan angka! (˘･_･˘)")
        jumlahPerMintaan = input(
        "Masukkan jumlah yang ingin diminta: ")
    jumlahPerMintaan = int(jumlahPerMintaan)    
    return jumlahPerMintaan

def mintaConsumable(dataconsumable, dataRiwayat, idPeMinta, username):
    # PROSEDUR UMUM PerMintaan
    def prosedurMinta():
        #PROSEDUR DARI MASUKKAN JUMLAH
        def prosedurMasukkanJumlahToNext():
            #PROSEDUR DIJALANKAN JIKA JADI MEMINJAM
            def prosedurJadiMinta():    
                dataconsumable[dataItem["indeks"]]["jumlah"] = str(
                    jumlahTersedia - jumlahPerMintaan)
                print("Masukkan tanggal permintaan: ")
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
                consumableHistoryDataBaru = {
                        "id": str(idBorrow),
                        "id_pengambil":idPeMinta,
                        "id_consumable":idItem,
                        "tanggal_pengambilan":tanggal,
                        "jumlah":jumlahPerMintaan,
                        }
                dataRiwayat.append(consumableHistoryDataBaru)
                print("PerMintaan {}(x{}) berhasil dilakukan oleh {} pada tanggal {}".format(
                    namaconsumable, str(
                        jumlahPerMintaan), username, tanggal
                ))
            
            # masukkan jumlah
            jumlahPerMintaan = getJumlahPerMintaan()

            # lakukan tergantung jumlah PerMintaan
            if jumlahPerMintaan == 0:
                print("Berarti gak ada yang diminta dong... ┌( ´_ゝ` )┐")
            else:
                if jumlahTersedia >= jumlahPerMintaan:
                    #pilihan 1,2,3,0 cek pilihan jadi atau tidak
                    nextChoiceDecided = False
                    while not nextChoiceDecided:
                        print(yakinSkript.format(namaconsumable,jumlahPerMintaan))
                        pilihanSelanjutnya = input(">>> ")
                        if pilihanSelanjutnya == "1":
                            nextChoiceDecided = True
                            prosedurJadiMinta()
                        elif pilihanSelanjutnya == "2":
                            nextChoiceDecided = True
                            prosedurMasukkanJumlahToNext()     
                        elif pilihanSelanjutnya == "3":
                            nextChoiceDecided = True
                            prosedurMinta()
                        elif pilihanSelanjutnya == "0":
                            nextChoiceDecided = True
                            print("Yaah kamu gajadi minta ... ┌( ´_ゝ` )┐")
                        else:
                            print("Masukkan angka! (˘･_･˘)")
                else:
                    print("Jumlah tidak cukup")               

        idItem = dapatkanItem(dataconsumable,username)
        # cek apakah item ada, jika ada, jalankan algoritma
        dataItem = isIdItemAda(idItem, dataconsumable)
        if (dataItem["keberadaan"]) and (cekMinta(idItem, dataRiwayat) == True):
            jumlahTersedia = int(dataconsumable[dataItem["indeks"]]["jumlah"])
            indeksconsumable = dataItem["indeks"]
            namaconsumable = dataconsumable[indeksconsumable]["nama"]
            print("consumable tersebut adalah "+namaconsumable)
            print(namaconsumable + " tersedia sejumlah " + str(jumlahTersedia))
            prosedurMasukkanJumlahToNext()
        elif (dataItem["keberadaan"]) and (cekMinta(idItem, dataRiwayat) == False):
            print("Consumable tersebut masih kamu minta.\nSilahkan kembalikan terlebih dahulu atau Minta yang lain! ヾ(^▽^*)")
        else:
            print("Consumable dengan ID tersebut tidak ada")
    

    # Tanpa pemilihan nama dan id, hanya id saja
    if len(dataconsumable) == 1:
        print("Ups, maaf! Data consumable masih kosong, Permintaan belum dapat dilakukan (っ °Д °;)っ")
    elif len(dataconsumable) > 1:
        prosedurMinta()




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







