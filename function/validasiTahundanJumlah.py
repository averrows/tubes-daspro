def tahunvalid(tahun):
    tahuninteger = False
    tahunstring = str(tahun)
    panjangtahun = len(tahun)
    if panjangtahun<=4:
        i = 0
        while i < panjangtahun and not tahuninteger:
            if tahun[i] not in "1234567890":
                tahuninteger = True
            else:
                i += 1
        if tahuninteger:
            return False
        else:
            return True
    else:
        return False

def jumlahvalid(jumlah):
    jumlahinteger = False
    jumlahstring = str(jumlah)
    panjangjumlah = len(jumlah)
    i = 0
    while i < panjangjumlah and not jumlahinteger:
        if jumlah[i] not in "1234567890":
            jumlahinteger = True
        else:
            i += 1
    if jumlahinteger:
        return False
    else:
        return True
    
def jumlahbesarkecil(jumlah):
    statusjumlah = False
    jumlahstring = str(jumlah)
    panjangjumlah = len(jumlahstring)
    if jumlahstring[0] not in "-1234567890":
        statusjumlah = False
        return False
    else:
        i = 1
        while i < panjangjumlah and not statusjumlah:
            if jumlahstring[i] not in "1234567890":
                statusjumlah = True
            else:
                i += 1
        if statusjumlah:
            return False
        else:
            return True