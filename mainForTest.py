# Argparse
from function.tambahItem import tambahitem
from function.save import saveMain
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
    print("MAIN INI ADALAH MAIN TEST, JANGAN LUPA")
    print("""
        USER YANG LOGIN CERITANYA ADALAH: faynadia 
        DENGAN ID: 4 
        faynadia ADALAH TUHAN, BISA APA PUN YANG DILAKUKAN ADMIN DAN USER (OMNIPOTENT) 
        KECUALI LOGIN KARENA LOGIN BISA MERUSAK KEESAANNYA
        """)
    print("="*25 + " MENU UTAMA " + "="*25)             # (50 + 2 + 10) characters
    (userData,
     gadgetData,
     consumableData,
     gadgetBorrowHistoryData,
     gadgetReturnHistoryData,
     consumableHistoryData,
     ) = load(folderData)
    if len(userData) == 1: #PROPERTI TES
        userData.append({"id":"4","nama":"Fayza Puyeng","username":"faynadia","password":"86108466174912395105981176311337","alamat":"New York","role":"admin"})
    kondisi = True
    user_status = {"id": "4", "username": "faynadia", "role": ""}
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
        elif perintah == "save":
            print("="*28 + " SAVE " + "="*28)           # (56 + 2 + 4) characters
            newDatas = {  # hanya untuk read, tidak bisa mengganti datanya.
                "userData": userData,
                "gadgetData": gadgetData,
                "consumableData": consumableData,
                "consumableHistoryData": consumableHistoryData,
                "gadgetBorrowHistoryData": gadgetBorrowHistoryData,
                "gadgetReturnHistoryData": gadgetReturnHistoryData
            }
            saveMain(newDatas)
            print("="*62)
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
            pinjamGadget(gadgetData, gadgetBorrowHistoryData, user_status["id"],user_status["username"])
            print("="*62)
        elif perintah == "save":
            print("="*28 + " SAVE " + "="*28)           # (56 + 2 + 4) characters
            newDatas = {  # hanya untuk read, tidak bisa mengganti datanya.
                "userData": userData,
                "gadgetData": gadgetData,
                "consumableData": consumableData,
                "consumableHistoryData": consumableHistoryData,
                "gadgetBorrowHistoryData": gadgetBorrowHistoryData,
                "gadgetReturnHistoryData": gadgetReturnHistoryData
            }
            saveMain(newDatas)
            print("="*62)
        elif perintah == "kembalikan":
            print("="*25 + " KEMBALIKAN " + "="*26)     # (51 + 2 + 9) characters
            kembalikanGadgetMain(user_status["id"], gadgetBorrowHistoryData, gadgetReturnHistoryData, gadgetData)
            print("="*62)
        elif perintah == "minta":
            print("="*27 + " MINTA " + "="*26)          # (55 + 2 + 5) characters
            mintaConsumable(consumableData,consumableHistoryData,user_status["id"],user_status["username"])
            print("="*62)
    while kondisi:
        print("MAIN INI ADALAH MAIN TEST, JANGAN LUPA")
        print("masukkan perintah: (bingung? masukkan 'bantuan')")
        perintah = input(">>> ")
        print("")
        if perintah == "bantuan":
            print("BANTUAN UNTUK ADMIN  ---Hanya properti tes")
            bantuan("admin")
            print("BANTUAN UNTUK USER  ---Hanya properti tes")
            bantuan("user")
            print("BANTUAN UNTUK STRANGER  ---Hanya properti tes")
            bantuan("")
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
        adminAllowedAction(perintah)
        userAllowedAction(perintah)

if __name__ == "__main__":
    main()