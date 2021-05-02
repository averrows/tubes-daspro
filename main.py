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
from function.hapusItem import hapusitem
from function.lihatRiwayatPengambilanConsumable import lihatRiwayatPengambilanConsumable
from function.ubahJumlah import ubahjumlah
from function.tingkatkanRarityConsumables import tingkatkanRarityConsumables
from function.hapusItem import hapusitem
import os
clear = lambda: os.system('cls')
# from function.CsvTools import parseCSV

# text art interface
doraemon_stenbaimi = r"""
                  ,,;yyWW$$@l@l@@$$$$@gyw,,                 
            ,y@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$gw,           
        ,@$$$$$$$@*'      "*$$$$@*`     `"M$$$$$$$$g,       
     w$$$$$$$$$F             1$"            "%$$$$$$$$&,    
  ,$$$$$$$$$$$                L               ]$$$$$$$$$$g, 
g$$$$$$$$$$$$`          ,,,   L   ,,           ]$$$$$$$$$$$@
$$$$$$$$$$$@M          $wg@K  L  @wg@C         j%@$$$$$$$$$$
$$$$$$$N"'   L         "&$& ,gg,,"&$M          L   "*B$$$$$$
$$$$M`        ,           g$$$$$$$g           '       -"%@$$
$@""~,           .     ,.$$$$$$$$$$F,     ,+"         ,wr"1$
`      `^                "*^*^*^^**''          ''  ^"`''''''
"""
title = r"""
             _  __           _                    
            | |/ /          | |                   
            | ' / __ _ _ __ | |_ ___  _ __   __ _ 
            |  < / _` | '_ \| __/ _ \| '_ \ / _` |
            | . \ (_| | | | | || (_) | | | | (_| |
            |_|\_\__,_|_| |_|\__\___/|_| |_|\__, |
                /\   (_)     (_) |           __/ |
               /  \   _  __ _ _| |__        |___/ 
              / /\ \ | |/ _` | | '_ \            
             / ____ \| | (_| | | |_) |           
            /_/    \_\ |\__,_|_|_.__/            
                    _/ |                         
                    |__/                          
"""

# Import fungsi secara keseluruhan


def main(folderData):
    clear()
    print("="*25 + " MENU UTAMA " + "="*25)             # (50 + 2 + 10) characters
    print(title)
    print(doraemon_stenbaimi)
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
            print("="*25 + " HAPUS ITEM " + "="*25)     # (50 + 2 + 10) characters
            hapusitem(gadgetData, consumableData)
            print("="*62)
        elif perintah == "ubahjumlah":
            print("="*25 + " UBAH JUMLAH " + "="*24)     # (49 + 2 + 11) characters
            ubahjumlah(gadgetData, consumableData)
            print("="*62)
        elif perintah == "riwayatpinjam":
            print("="*23 + " RIWAYAT PINJAM " + "="*23)  # (46 + 2 + 14) characters
            lihatRiwayatPinjamGadget(gadgetBorrowHistoryData,userData,1,0)
            print("="*62)
        elif perintah == "riwayatkembali":
            print("="*23 + " RIWAYAT KEMBALI " + "="*22)   # (45 + 2 + 15) characters
            lihatRiwayatKembalikanGadget(gadgetReturnHistoryData,userData,gadgetData,gadgetBorrowHistoryData)
            print("="*62)
        elif perintah == "riwayatambil":
            print("="*23 + " RIWAYAT AMBIL " + "="*23)   # (46 + 2 + 14) characters
            lihatRiwayatPengambilanConsumable(consumableHistoryData,userData,consumableData)
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
            saveMain(newDatas,folderData)
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
            pinjamGadget(gadgetData, gadgetBorrowHistoryData, user_status["id"], user_status["username"])
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
            saveMain(newDatas,folderData)
            print("="*62)
        elif perintah == "kembalikan":
            print("="*25 + " KEMBALIKAN " + "="*26)     # (51 + 2 + 9) characters
            kembalikanGadgetMain(user_status["id"], gadgetBorrowHistoryData, gadgetReturnHistoryData, gadgetData)
            print("="*62)
        elif perintah == "minta":
            print("="*27 + " MINTA " + "="*26)          # (55 + 2 + 5) characters
            mintaConsumable(consumableData,consumableHistoryData,user_status["id"],user_status["username"])
            print("="*62)
        elif perintah == "gacha":
            tingkatkanRarityConsumables(consumableData,consumableHistoryData,user_status["username"],user_status["id"])
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('folderData', nargs='?')
    args = parser.parse_args()

    if args.folderData is not None:
        folderData = args.folderData
        main(folderData)
    else:
        print("Tidak ada nama folder yang diberikan!")
        print("Pemakaian: python main.py <namafolder>")


