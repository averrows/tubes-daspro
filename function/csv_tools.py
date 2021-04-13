def parseCSV(csv_file):
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
    dataFile = open(csv_file)
    dataRaw = dataFile.read()
    dataFile.close()
    dataPerBaris = pisah(dataRaw,'\n')
    hasil = []
    headers = pisah(dataPerBaris[0],';')
    for data in dataPerBaris[1:]:
        dictData = {}
        data = pisah(data,',')
        i = 0
        for header in headers:
            dictData[header] = data[i]
            i += 1
        hasil.append(dictData)

    print(hasil)
    return hasil

def writeCSV(csv_file):
    


    
