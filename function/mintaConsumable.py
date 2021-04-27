from function.kembalikanGadget import validasiTanggal # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal # pylint: disable=import-error

def mintaConsumable(consumableData,consumableHistoryData,idPeminta):
    if len(consumableData) == 1:
        print("Consumable masih kosong, tidak dapat dilakukan peminjaman")
    elif len(consumableData)>1:
        idItem = input("Masukkan ID consumable: ")
        dataItem =isIdItemAda(idItem,consumableData)
        if dataItem["keberadaan"]:
            jumlahTersedia = int(consumableData[dataItem["indeks"]]["jumlah"])
            namaConsumable = consumableData[dataItem["indeks"]]["nama"]
            print("Consumable tersebut adalah "+namaConsumable)
            print(namaConsumable + " tersedia sejumlah "+ str(jumlahTersedia))
            jumlahPermintaan = int(input("Masukkan jumlah yang ingin diminta: "))
            if jumlahTersedia >=  jumlahPermintaan:
                jadiMinta = input("Apakah jadi meminta?(Yy)")
                if jadiMinta == "y" or jadiMinta == "Y":
                    consumableData[dataItem["indeks"]]["jumlah"] = str(jumlahTersedia - jumlahPermintaan)
                    print("Kamu ada di 'kapan'?")
                    masukkanTanggal = False
                    while not masukkanTanggal:
                        day = int(input())
                        month = int(input())
                        year = int(input())
                        masukkanTanggal = validasiTanggal(day,month,year)
                        if masukkanTanggal == False:
                            print("Tanggal yang dimasukkan tidak ada, harap masukkan ulang")
                    tanggal = str(day)+"/"+str(month)+"/"+str(year)
                    consumableHistoryDataBaru = {
                        "id": str(len(consumableHistoryData)),
                        "id_pengambil":idPeminta,
                        "id_consumable":idItem,
                        "tanggal_pengambilan":tanggal,
                        "jumlah":jumlahPermintaan,
                        }
                    consumableHistoryData.append(consumableHistoryDataBaru)
                    urutDataBerdasarTanggal(consumableHistoryData)
                    print("Peminjaman {}(x{}) berhasil dilakukan oleh {} pada tanggal {}".format(
                        namaConsumable,str(jumlahPermintaan),idPeminta,tanggal
                    ))
                    print(consumableHistoryData)
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