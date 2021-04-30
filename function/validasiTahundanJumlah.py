def tahunvalid(tahun):
    tahuninteger = False
    tahunstring = str(tahun)
    panjangtahun = len(tahun)
    i = 0
    while i < panjangtahun and not tahuninteger:
        if tahun[i] not in "1234567890":
            tahuninteger = True
        else:
            i += 1
    if tahunInteger:
        return False
    else:
        return True

def jumlahvalid(jumlah):
    jumlahinteger = False
    jumlahstring = str(jumlah)
    panjangjumlah = len(jumlah)
    i = 1
    while i < panjangjumlah and not jumlahinteger:
        if jumlah[i] not in "1234567890":
            jumlahinteger = True
        else:
            i += 1
    if jumlahInteger:
        return False
    else:
        return True
    
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