from CsvTools import parseCSV
data = parseCSV("../data/gadget_borrow_history.csv")


def printDataDariAkhir(data, jumlah):
    #KAMUS LOKAL
    #data : array of dictionary
    #jumlah : integer
    #Melakukan print dari data dimulai dari urutan terakhir sampai jumlah
    #dibutuhkan
    headersDariData = list(data[0].keys())
    headersData = ["ID Peminjaman","Nama Pengambil","Nama Gadget","Tanggal Peminjaman","Jumlah"]
    for i in range(jumlah):
        dataDiPrint = data[len(data)-1-i]
        print(susunanPrint(dataDiPrint,headersData,headersDariData))

def susunanPrint(dict,headers,headersDariData):
    #Mengembalikan suatu string yang diformat
    panjangHeaderTerpanjang = getPanjangElemenTerpanjang(headers)
    hasil = ""
    for i in range(len(headers)):
        hasil += headers[i]
        hasil += spasiTambahan(len(headers[i]),panjangHeaderTerpanjang)
        hasil += ":"
        hasil += " "
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

def lihatRiwayatPinjamGadget(dataRiwayat):
    jumlahDataRiwayat = len(dataRiwayat)
    if jumlahDataRiwayat == 0:
        print("Belum ada peminjaman gadget dilakukan")
    elif jumlahDataRiwayat < 5:
        print("\n")
        printDataDariAkhir(dataRiwayat, len(dataRiwayat))
    else:
        print("\n")
        printDataDariAkhir(dataRiwayat, 5)
        printSisa = input("Lihat riwayat selanjutnya?(Yy/Nn)")
        if printSisa == "Y" or printSisa == "y":
            lihatRiwayatPinjamGadget(dataRiwayat[:(len(dataRiwayat)-5)])
        else:
            print("oke")

lihatRiwayatPinjamGadget(data)
        