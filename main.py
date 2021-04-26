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
from function.lihatRiwayatKembalikanGadget import lihatRiwayatKembalikanGadget
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
    user_status = {"username": "", "role": ""}
    def adminAllowedAction(perintah):
        if perintah == "register":
            register(userData)
        elif perintah == "carirarity":
            CariRarity(gadgetData)
        elif perintah == "caritahun":
            CariTahun(gadgetData)
        elif perintah == "tambahitem":
            tambahitem(gadgetData, consumableData)
        elif perintah == "hapusitem":
            pass
        elif perintah == "ubahjumlah":
            pass
        elif perintah == "riwayatpinjam":
            lihatRiwayatPinjamGadget(gadgetBorrowHistoryData)
        elif perintah == "riwayatkembali":
            lihatRiwayatKembalikanGadget(gadgetReturnHistoryData)
        elif perintah == "riwayatambil":
            pass


    def userAllowedAction(perintah):
        if perintah == "carirarity":
            CariRarity(gadgetData)
        elif perintah == "caritahun":
            CariTahun(gadgetData)
        elif perintah == "pinjam":
            pinjamGadget(gadgetData, gadgetBorrowHistoryData, user_status["username"])
        elif perintah == "kembalikan":
            kembalikanGadgetMain(
                user_status["username"], gadgetBorrowHistoryData, gadgetReturnHistoryData, gadgetData)
        elif perintah == "minta":
            pass
    while kondisi:
        perintah = input()
        if perintah == "login":
            user_status = login(userData)
        elif perintah == "bantuan":
            role = user_status["role"]
            Bantuan(role)
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
        if user_status["role"] == "admin":
            adminAllowedAction(perintah)
        elif user_status["role"] == "user":
            userAllowedAction(perintah)


if __name__ == "__main__":
    main()
