def temukanGadget(identifier,valueDesired):
    return []

def pinjamGadget(datas):
    print("Pinjam Gadget")
    identifier = input("identifier apa yang ingin dipakai? (Tekan 1 untuk id. Tekan 2 untuk nama)")
    if identifier == 1:
        pass
    elif identifier == 2:
        namaGadgetDiinginkan = input()
        gadgetSesuai = temukanGadget("nama",namaGadgetDiinginkan)#mengembalikan sebuah array of dict
        jumlahDitemukan = len(gadgetSesuai)    
        for i in range(len(gadgetSesuai)):
            print(i)
            isi = ["id","nama","deskripsi","jumlah","rarity","tahun ditemukan"]
            gadget = ("Nama            : {0}\n" + 
                      "Deskripsi       : {1}\n" +
                      "Jumlah          : {2}\n" +
                      "Rarity          : {3}\n" +                
                      "Tahun Ditemukan : {4}\n").format(gadgetSesuai[i]["nama"], gadgetSesuai[i]["deskripsi"], gadgetSesuai[i]["jumlah"],
                      gadgetSesuai[i]["rarity"],gadgetSesuai[i]["tahun ditemukan"])
    else:
        pass