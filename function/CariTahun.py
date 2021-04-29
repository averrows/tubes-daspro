# Program CariTahun
# berisi prosedur untuk melakukan pencarian gadget sesuai kategori tahun

def cariTahun(data):
    def isFound(year, cat):
    # fungsi IsFound menghasilkan True jika menemukan barang
    # sesuai rarity yang dicari dan False jika tidak ditemukan
        found = False
        i = 1
        while i < len(data) and not found:
            if cat == "<" and int(data[i]["tahun_ditemukan"]) < year:
                found = True
            elif cat == "<=" and int(data[i]["tahun_ditemukan"]) <= year:
                found = True
            elif cat == "=" and int(data[i]["tahun_ditemukan"]) == year:
                found = True
            elif cat == ">=" and int(data[i]["tahun_ditemukan"]) >= year:
                found = True
            elif cat == ">" and int(data[i]["tahun_ditemukan"]) > year:
                found = True
            else:
                i += 1
        if found:
            return True
        else:
            return False

# ALGORITMA    
    if len(data) == 1:  # data hanya berisi header
        print("Ups, maaf! Data tidak ditemukan (っ °Д °;)っ")
    else:
        tahun = int(input("Masukkan tahun: "))
        kategori = input("Masukkan kategori: ")
        print("\nHasil pencarian:\n")

        if isFound(tahun, kategori):
            for i in range(1, len(data)):
                gadget = ("Nama            : {0}\n" + 
                          "Deskripsi       : {1}\n" +
                          "Jumlah          : {2}\n" +
                          "Rarity          : {3}\n" +                
                          "Tahun Ditemukan : {4}\n").format(data[i]["nama"], data[i]["deskripsi"], data[i]["jumlah"],
                          data[i]["rarity"],data[i]["tahun_ditemukan"])
                     
                if kategori == "<" and int(data[i]["tahun_ditemukan"]) < tahun:
                    print(gadget)
                elif kategori == "<=" and int(data[i]["tahun_ditemukan"]) <= tahun:
                    print(gadget)
                elif kategori == "=" and int(data[i]["tahun_ditemukan"]) == tahun:
                    print(gadget)
                elif kategori == ">=" and int(data[i]["tahun_ditemukan"]) >= tahun:
                    print(gadget)
                elif kategori == ">" and int(data[i]["tahun_ditemukan"]) > tahun:
                    print(gadget)
        else:
            print(f"Gadget dengan kategori {kategori}{tahun} tidak ditemukan!")
