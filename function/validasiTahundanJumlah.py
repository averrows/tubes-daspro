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
    statusjumlah = False
    jumlahstring = str(jumlah)
    panjangjumlah = len(jumlahstring)
    kodesatu = jumlahstring[0:panjangjumlah]
    kodesisa = jumlahstring[1:panjangjumlah]
    for i in kodesatu:
        if jumlahstring[0] not in "-1234567890":
            statusjumlah = False
        else:
            for i in kodesisa:
                if i not in "1234567890":
                    statusjumlah = False
                else:
                    statusjumlah = True
    if statusjumlah:
        return True
    else:
        return False