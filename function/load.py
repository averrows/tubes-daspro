from function.csvTools import parseCSV # pylint: disable=import-error
from function.urutDataBerdasarTanggal import urutDataBerdasarTanggal # pylint: disable=import-error

import os 
def load(folderData):
    print("Loading...")
    fixingFolderTidakAda(folderData)
    fixingCsvTidakAda(folderData)
    required_csv =  ["user.csv","gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]
    data = []
    for File in required_csv:
            data.append(parseCSV(folderData+"/"+File))
    print("Selamat datang di \"Kantong Ajaib!\"")
    return tuple(data)
def createNewFile(fileName):
    newFile = open(fileName,'w')
    newFile.close()
def fixingCsvTidakAda(folderData):
    required_csv =  ["gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","user.csv","consumable_history.csv"]
    for (root, dirs, files) in os.walk(folderData,topdown=False):
        Files = files
    
    for x in required_csv: 
        if x in Files: #jika sudah ada filenya
            pass
        else: #jika tidak ada file tersebut
            createNewFile(folderData+"/"+x)

def fixingFolderTidakAda(folderData):
    Dirs = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            Dirs.append((root+"/"+name)[2:].replace("\\","/"))
    if folderData in Dirs:
        pass
    else: #folderData not in Dirs
        os.mkdir("./"+folderData)