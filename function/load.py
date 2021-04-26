from function.CsvTools import parseCSV # pylint: disable=import-error
import os 
def load(folderData):
    print("Loading...")
    fixingCsvTidakAda(folderData)
    required_csv =  ["user.csv","gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]
    data = []
    for File in required_csv:
        data.append(parseCSV(folderData+"/"+File))
    print("Selamat datang di \"Kantong Ajaib!\"")
    return tuple(data)
def createNewFile(fileName, header):
    newFile = open(fileName,'w')
    newFile.write(header)

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