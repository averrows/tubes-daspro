from function.csvTools import writeCSV # pylint: disable=import-error
import os
from function.load import fixingCsvTidakAda # pylint: disable=import-error
from function.load import fixingFolderTidakAda # pylint: disable=import-error

def save(newData,folderData):
    print("Sedang menyimpan...")
    fixingCsvTidakAda(folderData)
    dataList =  ["userData",
                "gadgetData",
                "consumableData",
                "consumableHistoryData",
                "gadgetBorrowHistoryData",
                "gadgetReturnHistoryData"]
    required_csv =  ["user.csv","gadget.csv","consumable.csv","consumable_history.csv","gadget_borrow_history.csv","gadget_return_history.csv"]
    for i in range(len(dataList)):
        writeCSV(os.path.join(folderData,required_csv[i]),newData[dataList[i]])
    print("Data berhasil disimpan pada folder {}".format(folderData))

def saveMain(newData,lameFolder):
    pilihan = input("Pakai folder tadi (1), atau folder lain(2) ?")
    terpilih = False
    while not terpilih:
        if pilihan == "1":
            folder = lameFolder
            terpilih = True
        elif pilihan == "2":
            folder = input("Masukkan nama folder penyimpanan(contoh: test_data/saya): ")
            terpilih = True
        else:
            print("Masukkan antara dua pilihan itu aja yaa...")
            pilihan = input(">>> ")

    fixingFolderTidakAda(folder)
    save(newData,folder)
