from function.csvTools import parseCSV # pylint: disable=import-error

import os 
def load(folderData):
    print("Loading...")
    fixingFolderTidakAda(folderData)
    fixingCsvTidakAda(folderData)
    required_csv =  ["user.csv","gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]
    data = []
    for File in required_csv:
            data.append(parseCSV(os.path.join(folderData,File)))
    print("Data berhasil diload dari {}".format(folderData))
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
    def rekursiBuatFolder(path):
        #basis
        if os.path.dirname(path) == "":
            if os.path.exists(path) == False:
                os.mkdir(path)
            return path
        else: #rekurens
            path = os.path.join(rekursiBuatFolder(os.path.dirname(path)),os.path.basename(path))
            if os.path.exists(path) == False:
                os.mkdir(path)
            return path
    if os.path.isdir(folderData):
        pass
    else:
        rekursiBuatFolder(folderData)