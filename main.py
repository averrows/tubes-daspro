# Argparse
from function.tambahItem import tambahitem
from function.simpan import simpan
from function.register import register
from function.pinjamGadget import pinjamGadget
from function.login import login
from function.lihatRiwayatPinjamGadget import lihatRiwayatPinjamGadget
from function.kembalikanGadget import kembalikanGadgetMain
from function.keluar import keluar
from function.cariTahun import cariTahun
from function.cariRarity import cariRarity
from function.load import load
from function.bantuan import bantuan
from function.mintaConsumable import mintaConsumable
from function.lihatRiwayatKembalikanGadget import lihatRiwayatKembalikanGadget
import os
clear = lambda: os.system('cls')
# from function.CsvTools import parseCSV
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderData", help="folder dari data",
                    type=str)
args = parser.parse_args()
folderData = args.folderData

# Import fungsi secara keseluruhan


def main():
    clear()
    print("="*25 + " MENU UTAMA " + "="*25)             # (50 + 2 + 10) characters
    (userData,
     gadgetData,
     consumableData,
     gadgetBorrowHistoryData,
     gadgetReturnHistoryData,
     consumableHistoryData,
     ) = load(folderData)
    
    kondisi = True
    user_status = {"id": "", "username": "", "role": ""}
    def adminAllowedAction(perintah):
        if perintah == "register":
            print("="*25 + " REGISTER " + "="*26)       # (51 + 2 + 9) characters
            register(userData)
            print("="*62)
        elif perintah == "carirarity":
            print("="*25 + " CARI RARITY " + "="*24)    # (49 + 2 + 11) characters
            cariRarity(gadgetData)
            print("="*62)
        elif perintah == "caritahun":
            print("="*25 + " CARI TAHUN " + "="*25)     # (50 + 2 + 10) characters
            cariTahun(gadgetData)
            print("="*62)
        elif perintah == "tambahitem":
            print("="*25 + " TAMBAH ITEM " + "="*24)    # (49 + 2 + 11) characters 
            tambahitem(gadgetData, consumableData)
            print("="*62)
        elif perintah == "hapusitem":
            pass
        elif perintah == "ubahjumlah":
            pass
        elif perintah == "riwayatpinjam":
            print("="*23 + " RIWAYAT PINJAM " + "="*23)  # (46 + 2 + 14) characters
            lihatRiwayatPinjamGadget(gadgetBorrowHistoryData)
            print("="*62)
        elif perintah == "riwayatkembali":
            print("="*23 + " RIWAYAT KEMBALI " + "="*22)   # (45 + 2 + 15) characters
            lihatRiwayatKembalikanGadget(gadgetReturnHistoryData,userData,gadgetData,gadgetBorrowHistoryData)
            print("="*62)
        elif perintah == "riwayatambil":
            pass
    def userAllowedAction(perintah):
        if perintah == "carirarity":
            print("="*25 + " CARI RARITY " + "="*24)    # (49 + 2 + 11) characters
            cariRarity(gadgetData)
            print("="*62)
        elif perintah == "caritahun":
            print("="*25 + " CARI TAHUN " + "="*25)     # (50 + 2 + 10) characters
            cariTahun(gadgetData)
            print("="*62)
        elif perintah == "pinjam":
            print("="*27 + " PINJAM " + "="*27)         # (54 + 2 + 6) characters
            pinjamGadget(gadgetData, gadgetBorrowHistoryData, user_status["id"])
            print("="*62)
        elif perintah == "kembalikan":
            print("="*25 + " KEMBALIKAN " + "="*26)     # (51 + 2 + 9) characters
            kembalikanGadgetMain(user_status["username"], gadgetBorrowHistoryData, gadgetReturnHistoryData, gadgetData)
            print("="*62)
        elif perintah == "minta":
            print("="*27 + " MINTA " + "="*26)          # (55 + 2 + 5) characters
            mintaConsumable(consumableData,consumableHistoryData,user_status["username"])
            print("="*62)
    
    while kondisi:
        print("")
        print("masukkan perintah: (bingung? masukkan 'bantuan')")
        perintah = input(">>> ")
        print("")
        if perintah == "bantuan":
            role = user_status["role"]
            bantuan(role)
        elif perintah == "keluar":
            print("="*27 + " KELUAR " + "="*27)          # (54 + 2 + 6) characters
            newDatas = {  # hanya untuk read, tidak bisa mengganti datanya.
                "userData": userData,
                "gadgetData": gadgetData,
                "consumableData": consumableData,
                "consumableHistoryData": consumableHistoryData,
                "gadgetBorrowHistoryData": gadgetBorrowHistoryData,
                "gadgetReturnHistoryData": gadgetReturnHistoryData
            }
            kondisi = keluar(kondisi, newDatas, folderData)
        
        elif user_status["role"] == "admin":
            adminAllowedAction(perintah)
        elif user_status["role"] == "user":
            userAllowedAction(perintah)
        else:       # user_status["role"] == ""
            if perintah == "login":
                print("="*27 + " LOGIN " + "="*26)      # (55 + 2 + 5) characters
                user_status = login(userData)
                print("="*62)
            else:
                print("Perintah tersebut tidak tersedia!")

if __name__ == "__main__":
    main()