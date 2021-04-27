
def pisah(kalimat,pemisah):
        # kalimat = 'baris 1 \n baris 2'
        split_value = []
        tmp = ''
        for c in kalimat:
            if c == pemisah:
                split_value.append(tmp)
                tmp = ''
            else:
                tmp += c
        if tmp:
            split_value.append(tmp)
        return split_value

def urutDataBerdasarTanggal(data):
    headerRequired = ["tanggal_peminjaman","tanggal_pengembalian"]
    headerExisted = data[0]
    if(isHeaderExisted(headerRequired,headerExisted)):
        header = getHeaderExisted(headerRequired,headerExisted)
        sort(data, header)
    else:
        pass

def convertTanggal(tanggal):
    tanggalArray = pisah(tanggal,"/")
    return int(tanggalArray[0]) + (int(tanggalArray[1])-1)*30 + (int(tanggalArray[2]))*365
def isHeaderExisted(headerRequired,headerExisted):
    for x in headerExisted:
        if x in headerRequired:
            return True
    return False
def getHeaderExisted(headerRequired,headerExisted):
    for x in headerExisted:
        if x in headerRequired:
            return x


def get_min(data, index_start, header):
  # mendapatkan maksimum array dari indeks indeks_start sampai selesai
    minimum = convertTanggal(data[index_start][header]) #Inisiasi
    for x in data[index_start:]:
        pembanding = convertTanggal(x[header])
        if minimum > pembanding:
            minimum = pembanding
    return minimum   

def get_idx(data, tanggalConverted,header):
   # mendapatkan index dari suatu angka dalam array
    for i in range(1,len(data)):
        if convertTanggal(data[i][header]) == tanggalConverted:
            return i
def swap(data, indeks_1, indeks_2,header):
  # swap elemen array indeks 1 dengan indeks 2
    temp = data[indeks_1]
    data[indeks_1] = data[indeks_2]
    data[indeks_2] = temp
def sort(data,header):
    for i in range(1,len(data)):
        maxArr = get_min(data, i, header)
        maxIdx = get_idx(data, maxArr, header)  
        swap(data, i, maxIdx, header)


