from function.CsvTools import writeCSV # pylint: disable=import-error
import os
def fixingCsvTidakAda(folderData):
    required_csv =  ["gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","user.csv","consumable_history.csv"]
    for (root, dirs, files) in os.walk(folderData,topdown=True):
        Files = files
    headers = {
    "consumable_history.csv" :"id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah",
    "consumable.csv":"id;nama;deskripsi;jumlah;rarity",
    "gadget.csv":"id;nama;deskripsi;jumlah;rarity;tahun ditemukan",
    "user.csv":"nama;username;password;alamat;role",
    "gadget_return_history.csv":"id;id_peminjaman;tanggal_pengembalian;jumlah_pengembalian;sisa_pengembalian;last_returned",
    "gadget_borrow_history.csv":"id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned"
    }
    required_csv =  ["gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","user.csv","consumable_history.csv"]
    for x in required_csv: 
        if x in Files: #jika sudah ada filenya
            pass
        else: #jika tidak ada file tersebut
            createNewFile(folderData+"/"+x,headers[x])
def createNewFile(fileName, header):
    newFile = open(fileName,'w')
    newFile.write(header)
def simpan(newData,folderData):
    print("Sedang menyimpan...")
    fixingCsvTidakAda(folderData)
    dataList =  ["userData",
                "gadgetData",
                "consumableData",
                "consumableHistoryData",
                "gadgetBorrowHistoryData",
                "gadgetReturnHistoryData"]
    required_csv =  ["gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","user.csv","consumable_history.csv"]
    for i in range(len(dataList)):
        writeCSV(folderData+"/"+required_csv[i],newData[dataList[i]])
    print("data berhasil tersimpan")