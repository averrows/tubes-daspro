def pisah(kalimat, pemisah):
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


def renderLine(line):  # fungsi untuk merender suatu line ke dalam isiBaruFile
    i = 1
    isiBaruFile = ""
    while i < len(line):
        if i == len(line) - 1:
            isiBaruFile += line[i]
            isiBaruFile += "\n"
        else:
            isiBaruFile += line[i]
            isiBaruFile += ";"
        i += 1
    return isiBaruFile


def parseCSV(csv_file):
    # csv_file harus berisi setidaknya sebaris data header
    dataFile = open(csv_file)
    dataRaw = dataFile.read()
    dataFile.close()
    if dataRaw == "":  # untuk data yang bahkan header tidak ada
        print("file tidak dapat diparse karena masih kosong, gunakan prosedur load() dibanding langsung parseCSV")
    else:
        dataPerBaris = pisah(dataRaw, '\n')
        hasil = []
        onlyHeader = pisah(dataPerBaris[0], ';')
        hasil.append(onlyHeader)
        if len(dataPerBaris) == 1:  # untuk data yang hanya header
            return hasil
        else:
            for data in dataPerBaris[1:]:
                dictData = {}
                data = pisah(data, ';')
                i = 0
                for header in onlyHeader:
                    dictData[header] = data[i]
                    i += 1
                hasil.append(dictData)
            return hasil


def writeCSV(csv_file, newData):
    # csv_file adalah file yang akan dioverwrite, dan newData (array of dict) adalah data baru yang menggantikan data sebelumnya
    header = newData[0]  # dapatkan header
    if len(newData) == 1:
        isiBaruFile = renderLine(header)
    elif len(newData) > 1:
        dataFile = open(csv_file, 'w')
        isiBaruFile = renderLine(header)  # render header
        for x in newData[1:]:  # render isi
            # x adalah sebuah dictionary
            isi = list(x.values())
            # render isi
            isiBaruFile += renderLine(isi)
        dataFile.write(isiBaruFile)
        dataFile.close()
