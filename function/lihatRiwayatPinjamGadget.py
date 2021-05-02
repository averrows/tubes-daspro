from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal # pylint: disable=import-error
from math import ceil
def printDataDariAkhir(data, jumlah, currentHalaman, halamanKeseluruhan,dataUser):
    #KAMUS LOKAL
    #data : array of dictionary
    #jumlah : integer
    #Melakukan print dari data dimulai dari urutan terakhir sampai jumlah
    #dibutuhkan
    print("-"*25 + f" HALAMAN {currentHalaman}/{halamanKeseluruhan} " + "-"*25)
    print("\n")
    headersDariData = data[0]
    headersData = ["ID Peminjaman","Nama Peminjam","Nama Gadget","Tanggal Peminjaman","Jumlah"]
    for i in range(jumlah):
        dataDiPrint = data[len(data)-1-i]
        print(susunanPrint(dataDiPrint,headersData,headersDariData,dataUser))

def susunanPrint(dict,headers,headersDariData,dataUser):
    #Mengembalikan suatu string yang diformat
    panjangHeaderTerpanjang = getPanjangElemenTerpanjang(headers)
    hasil = ""
    for i in range(len(headers)):
        hasil += headers[i]
        hasil += spasiTambahan(len(headers[i]),panjangHeaderTerpanjang)
        hasil += ":"
        hasil += " "
        if headersDariData[i] == "id_peminjam":
            username = getNameFromId(dataUser,dict["id_peminjam"])
            hasil += username
        else:
            hasil += dict[headersDariData[i]]
        hasil += "\n"
    return hasil
def spasiTambahan(panjangString,acuan):
    jumlahSpasi = acuan - panjangString + 2
    hasil = ""
    i = 1
    while i <= jumlahSpasi:
        hasil += " "
        i += 1
    return hasil

        
def getPanjangElemenTerpanjang(list):
    #Mengembalikan panjang dari elemen terpanjang di list
    panjangElemenTerpanjang = len(list[0])
    i = 1
    while i < len(list):
        if panjangElemenTerpanjang < len(list[i]):
            panjangElemenTerpanjang = len(list[i])
        i += 1
    return panjangElemenTerpanjang 

counterLihatRiwayat = 0

def lihatRiwayatPinjamGadget(dataRiwayat,dataUser,counter,halamanKeseluruhan):
    dataRiwayat = urutDataBerdasarTanggal(dataRiwayat)
    jumlahDataRiwayat = len(dataRiwayat[1:])
    currentHalaman = counter
    if counter == 1:
        halamanKeseluruhan = ceil(jumlahDataRiwayat / 5)
    if jumlahDataRiwayat == 0:
        print("Belum ada peminjaman gadget dilakukan")
    elif jumlahDataRiwayat < 5:
        printDataDariAkhir(dataRiwayat, jumlahDataRiwayat, currentHalaman, halamanKeseluruhan,dataUser)
        counter += 1
        print("Data sudah habis! (o゜▽゜)o☆ Kembali ke menu utama....")
    else:
        print("\n")
        printDataDariAkhir(dataRiwayat, 5, currentHalaman, halamanKeseluruhan,dataUser)
        counter += 1
        printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn)")
        decision = False
        while not decision:
            if printSisa == "Y" or printSisa == "y":
                lihatRiwayatPinjamGadget(dataRiwayat[:(len(dataRiwayat)-5)],dataUser,counter,halamanKeseluruhan)
                decision = True
            elif printSisa.upper() == "N":
                print("Okay, kalau begitu kita kembali ke menu utama...")
                decision = True
            else:
                print("Masukan invalid!")
                printSisa = input(">>> ")

def getNameFromId(dataUser, id):
    for item in dataUser[1:]:
        if item["id"] == id:
            return item["nama"]
    return ""

        
