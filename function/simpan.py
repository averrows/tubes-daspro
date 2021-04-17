from CsvTools import writeCSV

def simpan(newData,folderData):
    #KAMUS
    #newData: dictionary of array of dictionary
    #folderData: string
    #ALGORITMA
    writeCSV(folderData + "/user.csv",newData["userData"])
    writeCSV(folderData + "/gadget.csv",newData["gadgetData"])
    writeCSV(folderData + "/consumable.csv",newData["consumableData"])
    writeCSV(folderData + "/consumable_history.csv",newData["consumableHistoryData"])
    writeCSV(folderData + "/gadget_borrow_history.csv",newData["gadgetBorrowHistoryData"])
    writeCSV(folderData + "/gadget_return_history.csv",newData["gadgetReturnHistoryData"])
        