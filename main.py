# Argparse
from function.CsvTools import parseCSV
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderData", help="folder dari data",
                    type=str)
args = parser.parse_args()
folderData = args.folderData

# Import fungsi secara keseluruhan
from function.bantuan import *
from function.CariRarity import *
from function.CariTahun import *
from function.CsvTools import *
from function.Hashing import *
from function.keluar import *
from function.kembalikanGadget import *
from function.LihatRiwayatPinjamGadget import *
from function.login import *
from function.PinjamGadget import pinjamGadget
from function.register import register
from function.simpan import simpan
from function.TambahItem import *
from function.urutDataBerdasarTanggal import *

def main():
    userData = parseCSV(folderData + "/user.csv")
    gadgetData = parseCSV(folderData + "/gadget.csv")
    consumableData = parseCSV(folderData + "/consumable.csv")
    consumableHistoryData = parseCSV(folderData + "/consumable_history.csv")
    gadgetBorrowHistoryData = parseCSV(folderData + "/gadget_borrow_history.csv")
    gadgetReturnHistoryData = parseCSV(folderData + "/gadget_return_history.csv")
    kondisi = True
    while kondisi:
        perintah = input()
        if perintah == "register":
            register(userData)
        elif perintah == "login":
            user = "tes" #login(userData)
            pass
        if user:
            if perintah == "keluar":
                pass
            elif perintah == "simpan":
                newDatas = { #hanya untuk read, tidak bisa mengganti datanya. 
                "userData":userData,
                "gadgetData":gadgetData,
                "consumableData":consumableData,
                "consumableHistoryData":consumableHistoryData,
                "gadgetBorrowHistoryData":gadgetBorrowHistoryData,
                "gadgetReturnHistoryData":gadgetReturnHistoryData
                }
                simpan(newDatas,folderData)
            elif perintah == "pinjam":
                pinjamGadget(gadgetData,gadgetBorrowHistoryData,user)
        elif perintah == "keluar":
            newDatas = { #hanya untuk read, tidak bisa mengganti datanya. 
                "userData":userData,
                "gadgetData":gadgetData,
                "consumableData":consumableData,
                "consumableHistoryData":consumableHistoryData,
                "gadgetBorrowHistoryData":gadgetBorrowHistoryData,
                "gadgetReturnHistoryData":gadgetReturnHistoryData
                }
            kondisi = Keluar(kondisi,newDatas,folderData)
if __name__ == "__main__":
    main()
