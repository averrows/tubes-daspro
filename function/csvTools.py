import os

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
    i = 0
    isiBaruFile = ""
    while i < len(line):
        if i == len(line) - 1:
            isiBaruFile += str(line[i])
            isiBaruFile += "\n"
        else:
            isiBaruFile += str(line[i])
            isiBaruFile += ";"
        i += 1
    return isiBaruFile


def parseCSV(csv_file):
    # csv_file harus berisi setidaknya sebaris data header
    dataFile = open(csv_file)
    dataRaw = dataFile.read()
    dataFile.close()
    hasil = []
    if dataRaw == "":  # untuk data yang bahkan header tidak ada
            headers = {
                "consumable_history.csv" :"id;id_pengambil;id_consumable;tanggal_pengambilan;jumlah",
                "consumable.csv":"id;nama;deskripsi;jumlah;rarity",
            "gadget.csv":"id;nama;deskripsi;jumlah;rarity;tahun ditemukan",
            "user.csv":"nama;username;password;alamat;role",
            "gadget_return_history.csv":"id;id_peminjaman;tanggal_pengembalian;jumlah_pengembalian;sisa_pengembalian;last_returned",
            "gadget_borrow_history.csv":"id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned"}
            #extract namafile
            namaFile = os.path.split(csv_file)[1]
            hasil.append(pisah(headers[namaFile],";"))
    else:
        dataPerBaris = pisah(dataRaw, '\n')
        onlyHeader = pisah(dataPerBaris[0], ';')
        hasil.append(onlyHeader)
        if len(dataPerBaris) == 1:
            pass
        else:
            for data in dataPerBaris[1:]:
                dictData = {}
                data = pisah(data, ';')
                i = 0
                for header in onlyHeader:
                    if i > len(data)-1:
                        print(f"Terdapat kesalahan isi csv file {csv_file}. Data yang terload hanya header saja")
                        return [onlyHeader]
                    else:
                        dictData[header] = data[i]
                    i += 1
                hasil.append(dictData)
    return hasil


def writeCSV(csv_file, newData):
    # csv_file adalah file yang akan dioverwrite, dan newData (array of dict) adalah data baru yang menggantikan data sebelumnya
    dataFile = open(csv_file, 'w')
    header = newData[0]  # dapatkan header
    if len(newData) == 1:
        isiBaruFile = renderLine(header)
    elif len(newData) > 1:
        isiBaruFile = renderLine(header)  # render header
        for x in newData[1:]:  # render isi
            # x adalah sebuah dictionary
            isi = list(x.values())
            # render isi
            isiBaruFile += renderLine(isi)
    dataFile.write(isiBaruFile)
    dataFile.close()
