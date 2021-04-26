# Argparse
from function.TambahItem import tambahitem
from function.simpan import simpan
from function.register import register
from function.PinjamGadget import pinjamGadget
from function.login import login
from function.LihatRiwayatPinjamGadget import lihatRiwayatPinjamGadget
from function.kembalikanGadget import kembalikanGadgetMain
from function.keluar import Keluar
from function.CariTahun import CariTahun
from function.CariRarity import CariRarity
from function.load import load
from function.bantuan import Bantuan
# from function.CsvTools import parseCSV
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderData", help="folder dari data",
                    type=str)
args = parser.parse_args()
folderData = args.folderData

# Import fungsi secara keseluruhan


def main():
    (userData,
    gadgetData,
    consumableData,
    consumableHistoryData,
    gadgetBorrowHistoryData,
    gadgetReturnHistoryData) = load(folderData)
    kondisi = True
    while kondisi:
        perintah = input()
        if perintah == "register":
            register(userData)
        elif perintah == "login":
            user = login(userData)
        if user:
            
            if perintah == "keluar":
                pass
            elif perintah == "simpan":
                newDatas = {  # hanya untuk read, tidak bisa mengganti datanya.
                    "userData": userData,
                    "gadgetData": gadgetData,
                    "consumableData": consumableData,
                    "consumableHistoryData": consumableHistoryData,
                    "gadgetBorrowHistoryData": gadgetBorrowHistoryData,
                    "gadgetReturnHistoryData": gadgetReturnHistoryData
                }
                simpan(newDatas, folderData)
            elif perintah == "pinjam":
                pinjamGadget(gadgetData, gadgetBorrowHistoryData, user)
        elif perintah == "keluar":
            newDatas = {  # hanya untuk read, tidak bisa mengganti datanya.
                "userData": userData,
                "gadgetData": gadgetData,
                "consumableData": consumableData,
                "consumableHistoryData": consumableHistoryData,
                "gadgetBorrowHistoryData": gadgetBorrowHistoryData,
                "gadgetReturnHistoryData": gadgetReturnHistoryData
            }
            kondisi = Keluar(kondisi, newDatas, folderData)


if __name__ == "__main__":
    main()
