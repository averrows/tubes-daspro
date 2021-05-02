from function.validasiTahundanJumlah import jumlahbesarkecil # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error
from function.pinjamGadget import isIdItemAda # pylint: disable=import-error
from function.kembalikanGadget import validasiAngka # pylint: disable=import-error




def ubahjumlah(gadgetData,consumableData):
    # ALGORITMA
    status = False
    while not status:
        ID = input("Masukkan ID: ")
        if IDValid(ID):
            if ID[0] == "G":
                ubahData(ID, gadgetData)
            elif ID[0] == "C":
                ubahData(ID, consumableData)
            status = True
        else:
            print("Id tidak valid, masukkan ulang")
            ID = input(">>> ")

def ubahData(id, data):
    statusItem = isIdItemAda(id, data) #mengembalikan dictionary berisi status keberadaan dan indeks pada data
    if statusItem["keberadaan"]:
        jumlahPerubahan = getJumlah()
        doChange(statusItem["indeks"], jumlahPerubahan, data)
    else: #statusItem["keberadaan"] == False
        print("Tidak ada item dengan id tersebut")
    
def getJumlah():
    jumlah = input("Masukkan perubahan jumlah: ")

    # Cek apakah jumlah adalah suatu angka
    while isinstance(jumlah,int):
        print("Harap masukkan angka!")
        jumlah = input(">>> ")
    
    return int(jumlah)

def doChange(indeks,jumlahPerubahan, data):
    jumlahAwal = int(data[indeks]["jumlah"])
    jumlahAkhir = jumlahAwal + jumlahPerubahan
    namaItem = data[indeks]["nama"]
    if jumlahAkhir >= 0:
        if jumlahAkhir > jumlahAwal:
            data[indeks]["jumlah"] = str(jumlahAkhir)
            print(f"{abs(jumlahPerubahan)} {namaItem} berhasil ditambahkan. Stok sekarang: {jumlahAkhir}")
        elif jumlahAkhir < jumlahAwal:
            data[indeks]["jumlah"] = str(jumlahAkhir)
            print(f"{abs(jumlahPerubahan)} {namaItem} berhasil dibuang. Stok sekarang: {jumlahAkhir}")
        else: #jumlahAkhir == jumlahAwal
            print(f"Tidak ada perubahan stok {namaItem}")
    else: #jumlahAkhir < 0
        print(f"{abs(jumlahPerubahan)} {namaItem} gagal dibuang karena stok kurang. Stok sekarang: {jumlahAwal} (< {abs(jumlahPerubahan)})")
