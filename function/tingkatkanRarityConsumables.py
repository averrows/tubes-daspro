import time
import datetime
import sys
import os
from function.mintaConsumable import *  # pylint: disable=import-error
from function.kembalikanGadget import validasiTanggal  # pylint: disable=import-error
from function.kembalikanGadget import validasiAngka  # pylint: disable=import-error
# from mintaConsumable import *
campurSkript = """
Halo {}, kamu ingin campur apa?
    Tekan:
        1 "Aku tahu ID consumable yang mau aku campur Dora !!!"
        2 "Aku cuma tahu beberapa katanya Dora !!!" -----Bingung Aku
        0 "udah gamau nyampur"
"""


def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def randomize(key, durasi):
    timeAwal = time.time()
    timeString = str((time.time())).replace(".", "")
    a = int(timeString[len(timeString)-3:])
    c = 0
    # String to be displayed when the application is loading
    load_str = "mengocok dadu...."
    ls_len = len(load_str)


    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    i = 0

    for seed in lcg(10007, a, c, key):
        timeJalan = time.time()
        if timeJalan > timeAwal + durasi:
            break
        else:
            # used to change the animation speed
            # smaller the value, faster will be the animation
            time.sleep(0.007) 
                                
            # converting the string to list
            # as string is immutable
            load_str_list = list(load_str) 
            
            # x->obtaining the ASCII code
            x = ord(load_str_list[i])
            
            # y->for storing altered ASCII code
            y = 0                             
    
            # if the character is "." or " ", keep it unaltered
            # switch uppercase to lowercase and vice-versa 
            if x != 32 and x != 46:             
                if x>90:
                    y = x-32
                else:
                    y = x + 32
                load_str_list[i]= chr(y)
            
            # for storing the resultant string
            res =''             
            for j in range(ls_len):
                res = res + load_str_list[j]
                
            # displaying the resultant string
            sys.stdout.write("\r"+res + animation[anicount])
            sys.stdout.flush()
    
            # Assigning loading string
            # to the resultant string
            load_str = res
    
            
            anicount = (anicount + 1)% 4
            i =(i + 1)% ls_len
    print("\n")
    return seed


def tentukanRange(rarity: dict):
    # range 1 milyar
    # 0 sampai satu milyar

    s = rarity["S"]/100
    a = rarity["A"]/100
    b = rarity["B"]/100
    c = rarity["C"]/100
    # (s,a,b,c) = normalize(s,a,b,c)
    batasAtas = 10000
    # tentukan range dari c
    rangeC = (0, c*batasAtas)
    rangeB = (rangeC[1], rangeC[1]+b*batasAtas)
    rangeA = (rangeB[1], rangeB[1]+a*batasAtas)
    rangeS = (rangeA[1], rangeA[1]+s*batasAtas)

    return {"S": rangeS, "A": rangeA, "B": rangeB, "C": rangeC}


def hasilRandomRarity(range: dict, random):
    for x in ["S", "A", "B", "C"]:
        rangeRarity = range[x]
        if random >= rangeRarity[0] and random < rangeRarity[1]:
            return x
    return "M"


def jumlahKeseluruhan(dataConsumable):
    jumlahKeseluruhan = 0
    for item in dataConsumable[1:]:
        jumlahKeseluruhan += int(item["jumlah"])
    return jumlahKeseluruhan


def rumusRarityUmum(pengaruhS, pengaruhA, pengaruhB, pengaruhC, dataConsumable):
    jumlah = jumlahKeseluruhan(dataConsumable)
    return {"S": pengaruhS, "A": pengaruhA, "B": pengaruhB, "C": pengaruhC}


def fraksiJumlah(rarity, dataConsumable):
    jumlahKeseluruhan = 0
    jumlah = 0
    for item in dataConsumable[1:]:
        jumlahKeseluruhan += int(item["jumlah"])
        if item["rarity"] == rarity:
            jumlah += int(item["jumlah"])
    return jumlah/jumlahKeseluruhan


def rumusRarityJumlahInventory(dataConsumable):
    pengaruh = {}
    for rarity in ["S", "A", "B", "C"]:
        fraksi = fraksiJumlah(rarity, dataConsumable)
        if fraksi == 0:
            pengaruh[rarity] = 0
        else:
            pengaruh[rarity] = 1/fraksi
    return pengaruh  # dictionary of integer


def rumusPengaruhKeseluruhan(pengaruhRarityUmum, pengaruhRarityJumlahInventory):
    for rarity2 in ["S", "A", "B", "C"]:
        for rarity3 in ["S", "A", "B", "C"]:
            pengaruhRarityUmum[rarity2][rarity3] = pengaruhRarityUmum[rarity2][rarity3] * \
                pengaruhRarityJumlahInventory[rarity2]
    return pengaruhRarityUmum


def rarityPascaPenambahanItem(rarity: str, jumlah: int, pengaruhKeseluruhan: dict, rarityBasis: dict):
    rarityBaru = {}
    for rarity2 in ["S", "A", "B", "C"]:
        rarityBaru[rarity2] = rarityBasis[rarity2] + \
            jumlah*pengaruhKeseluruhan[rarity][rarity2]

    return rarityBaru  # dictionary of integer


def tingkatkanRarityConsumables(dataConsumable, dataRiwayat, username, idPencampur):
    print("Sebelum main, masukkan tanggal dulu yah hehe.... ")
    masukkanTanggal = False
    while not masukkanTanggal:
        # tanggal
        day = input("Masukkan tanggal: ")
        while (validasiAngka(day) == False): # pylint: disable=E0602, E0603
            print("Masukkan angka! (˘･_･˘)")
            day = input("Masukkan tanggal: ")
        day = int(day)
        # bulan
        month = input("Masukkan bulan: ")
        while (validasiAngka(month) == False):
            print("Masukkan angka! (˘･_･˘)")
            month = input("Masukkan bulan: ")
        month = int(month)
        # tahun
        year = input("Masukkan tahun: ")
        while (validasiAngka(year) == False):
            print("Masukkan angka! (˘･_･˘)")
            year = input("Masukkan tahun: ")
        year = int(year)
        # validasi
        masukkanTanggal = validasiTanggal(day, month, year)
        if masukkanTanggal == False:
            print(
                "Tanggal yang dimasukkan tidak ada, harap masukkan ulang")
    dmy = datetime.datetime(year, month, day)
    tanggal = dmy.strftime(
        "%d") + "/" + dmy.strftime("%m") + "/" + dmy.strftime("%Y")
    
    idConsumable = dapatkanItem( # pylint: disable=E0602, E0603
        dataConsumable, username, campurSkript)  
    siap = False
    rarityBasis = {"S": 2, "A": 16, "B": 36, "C": 46}
    pengaruhRarityUmum = {"S": rumusRarityUmum(0.4, -0.4/21, -1.6/21, -6.4/21, dataConsumable), "A": rumusRarityUmum(0.2, 0.4, -0.2, -0.4, dataConsumable),
                                               "B": rumusRarityUmum(0.1, 0.2, 0., -0.12, dataConsumable), "C": rumusRarityUmum(0.00625, 0.025, 0.1, -0.13125, dataConsumable)}
    pengaruhRarityJumlahInventory = rumusRarityJumlahInventory(
        dataConsumable)  # {"S":20}
    pengaruhRarityKeseluruhan = rumusPengaruhKeseluruhan(
        pengaruhRarityUmum, pengaruhRarityJumlahInventory)
    jumlahBarangDicampur = 0
    while not (siap):
        existStatus = isIdItemAda( # pylint: disable=E0602, E0603
            idConsumable, dataConsumable)  # pylint: disable=E0602, E0603
        if existStatus["keberadaan"]:
            indeks = existStatus["indeks"]
            print("{} | rarity: {} | jumlah: {}".format(dataConsumable[indeks]["nama"],dataConsumable[indeks]["rarity"],dataConsumable[indeks]["jumlah"]))
            jumlah = getJumlahPermintaan( # pylint: disable=E0602, E0603
                "campur")  
            while jumlah > int(dataConsumable[indeks]["jumlah"]):
                print("Jumlah yang kamu masukkan berlebih!")
                jumlah = getJumlahPermintaan( # pylint: disable=E0602, E0603
                    "campur")  
            rarityBasis = rarityPascaPenambahanItem(
                dataConsumable[indeks]["rarity"], jumlah, pengaruhRarityKeseluruhan, rarityBasis)
            dataConsumable[indeks]["jumlah"] = str(int(dataConsumable[indeks]["jumlah"]) - jumlah)
            idMinta = len(dataRiwayat)

            consumableHistoryDataBaru = {
                "id": str(idMinta),
                "id_pengambil": idPencampur,
                "id_consumable": idConsumable,
                "tanggal_pengambilan": tanggal,
                "jumlah": jumlah,
            }
            dataRiwayat.append(consumableHistoryDataBaru)
            jumlahBarangDicampur += 1
        else:
            print("item tersebut tidak ada")
        # campur lagi?
        lagi = input("Campur yang lain?(Yy)")
        if lagi.upper() == "Y":
            idConsumable = dapatkanItem(dataConsumable, username, campurSkript)  # pylint: disable=E0602, E0603
            siap = False
        else:
            siap = True
    else:
        pass

    if jumlahBarangDicampur > 0:
        rangeDistribusi = tentukanRange(rarityBasis)
        angkaRandom = randomize(jumlahBarangDicampur, 1)
        rarityHasil = hasilRandomRarity(rangeDistribusi, angkaRandom)
        print("Selamat kamu mendapatkan rarity baru {}".format(rarityHasil))
    else:
        print("Kamu tidak mencampur apa-apa")

    # rarityBasis = {"S":2,"A":16,"B":36,"C":46}
    # pengaruhRarityUmum = {"S":rumusRarityUmum(0.4,-0.4/21,-1.6/21,-6.4/21),"A":rumusRarityUmum(0.1,0.4,-0.1,-0.4),"B":rumusRarityUmum(0.025,0.1,0.4,-0.525),"C":rumusRarityUmum(0.00625,0.025,0.1,-0.13125)}
    # pengaruhRarityJumlahInventory = rumusRarityJumlahInventory(dataConsumable) #{"S":20}
    # pengaruhRarityKeseluruhan = rumusPengaruhKeseluruhan(pengaruhRarityUmum,pengaruhRarityJumlahInventory)
    # rarity = input(">>> ")
    # jumlah = int(input(">>> "))

def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "mengocok dadu...."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
    print("\n")
bonus = {"S": "Okeh siap aing guys wkwkwk"}