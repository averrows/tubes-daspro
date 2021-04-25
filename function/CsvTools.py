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



def parseCSV(csv_file):
    dataFile = open(csv_file)
    dataRaw = dataFile.read()
    dataFile.close()
    dataPerBaris = pisah(dataRaw,'\n')
    hasil = []
    if len(dataPerBaris) == 0:
        return hasil
    elif len(dataPerBaris) == 1:
        onlyHeaders = pisah(dataPerBaris[0],';')
        dictData = {}
        for header in onlyHeaders:
            dictData[header] = None
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
    #csv_file adalah file yang akan dioverwrite, dan newData (array of dict) adalah data baru yang menggantikan data sebelumnya
    if newData == []:
        pass
    #proses new_data {array of dictionary} menjadi csv
    else:
        header = list(newData[0].keys()) #dapatkan header
        def renderLine(line): #fungsi untuk merender suatu line ke dalam isiBaruFile
            i = 0
            isiBaruFile = ""
            while i<len(line): 
                if i == len(line) - 1:
                    isiBaruFile += line[i]
                    isiBaruFile += "\n"
                else:
                    isiBaruFile += line[i]
                    isiBaruFile += ";"
                i += 1
            return isiBaruFile
        dataFile = open(csv_file,'w')
        isiBaruFile = renderLine(header)#render header
        for x in newData:#render isi
            #x adalah sebuah dictionary
            isi = list(x.values())
            #render isi    
            isiBaruFile += renderLine(isi)
        dataFile.write(isiBaruFile)
        dataFile.close()
    
