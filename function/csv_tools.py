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
        print(split_value)
        return split_value

def parseCSV(csv_file):
    dataFile = open(csv_file)
    dataRaw = dataFile.read()
    dataFile.close()
    dataPerBaris = pisah(dataRaw,'\n')
    hasil = []
    headers = pisah(dataPerBaris[0],';')
    for data in dataPerBaris[1:]:
        dictData = {}
        data = pisah(data,';')
        i = 0
        for header in headers:
            dictData[header] = data[i]
            i += 1
        hasil.append(dictData)

    return hasil

def writeCSV(csv_file, newData):
    dataFile = open(csv_file,'w')
    isiBaruFile = ""
    #proses new_data {array of dictionary} menjadi csv
    header = list(newData[0].keys()) #dapatkan header

    def renderLine(line): #fungsi untuk merender suatu line ke dalam isiBaruFile
        i = 0
        global isiBaruFile
        while i<len(line): 
            if i == len(line) - 1:
                isiBaruFile += line[i]
                isiBaruFile += "\n"
            else:
                isiBaruFile += line[i]
                isiBaruFile += ";"
            i += 1

    renderLine(header)#render header
    for x in newData:#render isi
        #x adalah sebuah dictionary
        isi = list(x.values())
        #render isi    
        renderLine(isi)
    dataFile.write(isiBaruFile)
    dataFile.close()
    
