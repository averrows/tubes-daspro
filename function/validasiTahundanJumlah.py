def tahunvalid(tahun):
    tahuninteger = False
    tahunstring = str(tahun)
    panjangtahun = len(tahun)
    kodetahun = tahunstring[0:panjangtahun]
    for i in kodetahun:
        if i not in "1234567890":
            tahuninteger = False
        else:
            tahuninteger = True
    if tahuninteger:
        return True
    else:
        return False

def jumlahvalid(jumlah):
    jumlahinteger = False
    jumlahstring = str(jumlah)
    panjangjumlah = len(jumlah)
    kodejumlah = jumlahstring[0:panjangjumlah]
    for i in kodejumlah:
        if i not in "1234567890":
            jumlahinteger = False
        else:
            jumlahinteger = True
    if jumlahinteger:
        return True
    else:
        return False

def jumlahbesarkecil(jumlah):
    if jumlah < 0:
        jumlahkurang = False
        jumlahstring = str(jumlah)
        panjangjumlah = len(jumlah)
        kodejumlah = jumlahstring[0:panjangjumlah]
        for i in kodejumlah:
            if i not in "1234567890":
                jumlahkurang = False
            else:
                jumlahkurang = True
        if jumlahkurang:
            return True
        else:
            return False
    else :
        jumlahlebih = False
        jumlahstring = str(jumlah)
        panjangjumlah = len(jumlah)
        kodejumlah = jumlahstring[0:panjangjumlah]
        for i in kodejumlah:
            if i not in "-1234567890":
                jumlahlebih = False
            else:
                jumlahlebih = True
        if jumlahlebih:
            return True
        else:
            return False