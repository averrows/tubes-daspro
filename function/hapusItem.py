from function.validasiID import IDValid, IDditemukan #pylint: disable=import-error

def hapusitem(gadgetData, consumableData, gadget_borrow_history_Data):
    # ALGORITMA
    validID = False
    while not validID:
        ID = input("Masukkan ID: ")

        if IDValid(ID) and ID[0] == "G":    # hapus gadget
            if len(gadgetData) == 1:        # jika data gadget hanya header
                print("Maaf data tidak tersedia")
                validID = True
            else:
                if IDditemukan(ID, gadgetData) and (isBorrowed(ID, gadget_borrow_history_Data)==False):
                    hapusGadget(ID, gadgetData)
                    validID = True
                elif IDditemukan(ID, gadgetData) and (isBorrowed(ID, gadget_borrow_history_Data)==True):
                    print("Gadget sedang dipinjam. Minta user kembalikan terlebih dahulu.")
                    validID = True
                else:
                    print("Tidak ada item dengan ID tersebut")
                
        elif IDValid(ID) and ID[0] == "C":  # hapus consumable
            if len(consumableData) == 1:    # jika data consumable hanya header
                print("Maaf data tidak tersedia")
                validID = True
            else:
                if IDditemukan(ID, consumableData):
                    hapusConsumable(ID, consumableData)
                    validID = True
                else:
                    print("Tidak ada item dengan ID tersebut")

        else:
            print("Input ID tidak valid!")


def hapusGadget(ID, gadgetData):
    # mencari gadget
    gadget_will_delete = {}
    for i in range(1, len(gadgetData)):
        if gadgetData[i]["id"] == ID:
            gadget_will_delete = gadgetData[i]

    # tanya user
    tanya = input("Apakah anda ingin menghapus " + gadget_will_delete["nama"] + "?(Yy/Nn) ")
    while tanya not in "YyNn":
        tanya = input("Apakah anda ingin menghapus " + gadget_will_delete["nama"] + "?(Yy/Nn) ")
    
    if tanya in "Yy":
        gadgetData.remove(gadget_will_delete)
        print("Item telah berhasil dihapus")
    else:
        print("Penghapusan tidak jadi dilakukan, kamu akan kembali ke menu")


def hapusConsumable(ID, consumableData):
    # mencari comsumable
    consumable_will_delete = {}
    for i in range(1, len(consumableData)):
        if consumableData[i]["id"] == ID:
            consumable_will_delete = consumableData[i]

    # tanya user
    tanya = input("Apakah anda ingin menghapus " + consumable_will_delete["nama"] + "?(Yy/Nn) ")
    while tanya not in "YyNn":
        tanya = input("Apakah anda ingin menghapus " + consumable_will_delete["nama"] + "?(Yy/Nn) ")
    
    if tanya in "Yy":
        consumableData.remove(consumable_will_delete)
        print("Item telah berhasil dihapus")
    else:
        print("Penghapusan tidak jadi dilakukan, kamu akan kembali ke menu")
        

def isBorrowed(ID, gadgetBorrowHistoryData):
    count = 0
    for i in range(1, len(gadgetBorrowHistoryData)):
        if (gadgetBorrowHistoryData[i]['id_gadget'] == ID):
            if (gadgetBorrowHistoryData[i]['is_returned'] == '1'):
                pass
            else:
                count = count + 1 
    if (count > 0):
        return True
    else:
        return False