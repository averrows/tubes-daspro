def mintaConsumable(consumableData,consumableHistoryData,idPeminta):
    if len(consumableData) == 1:
        print("Consumable masih kosong, tidak dapat dilakukan peminjaman")
    elif len(consumableData)>1:
        idItem = input("Masukkan ID consumable: ")
        dataItem =isIdItemAda(idItem,consumableData)
        if dataItem["keberadaan"]:
            jumlahTersedia = int(consumableData[dataItem["indeks"]]["jumlah"])
            namaGadget = consumableData[dataItem["indeks"]]["nama"]
            print("Gadget tersebut adalah "+namaGadget)
            print(namaGadget + " tersedia sejumlah "+ str(jumlahTersedia))
            jumlahPeminjaman = int(input("Masukkan jumlah yang ingin dipinjam: "))
            if jumlahTersedia >=  jumlahPeminjaman:
                jadiPinjam = input("Apakah jadi meminjam?(Yy)")
                if jadiPinjam == "y" or jadiPinjam == "Y":
                    consumableData[dataItem["indeks"]]["jumlah"] = str(jumlahTersedia - jumlahPeminjaman)
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
                        "id":consumableHistoryData[len(consumableHistoryData)-1]["id"][1:],
                        "id_peminjam":idPeminta,
                        "id_gadget":idItem,
                        "tanggal_peminjaman":tanggal,
                        "jumlah":jumlahPeminjaman,
                        "is_returned": 0
                        }
                    consumableHistoryData.append(consumableHistoryDataBaru)
                    urutDataBerdasarTanggal(consumableHistoryData)
                    print("Peminjaman {}(x{}) berhasil dilakukan oleh {} pada tanggal {}".format(
                        namaGadget,str(jumlahPeminjaman),idPeminta,tanggal
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