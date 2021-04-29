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
        writeCSV(folderData+"/"+required_csv[i],newData[dataList[i]])
    print("Data telah disimpan pada folder {folderData}")

def saveMain(newData):
    folder = input("Masukkan nama folder penyimpanan: ")
    fixingFolderTidakAda(folder)
    save(newData,folder)
