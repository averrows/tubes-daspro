import time
from function.mintaConsumable import * # pylint: disable=import-error
# from mintaConsumable import * 
campurSkript =    """
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


def randomize(key,durasi):
    timeAwal = time.time()
    timeString = str((time.time())).replace(".","")
    a = int(timeString[len(timeString)-3:])
    c = 0
    for seed in lcg(10007,a,c,key):
        timeJalan = time.time()
        if  timeJalan > timeAwal + durasi:
            break
        else:
            pass
    return seed


def tentukanRange(rarity:dict):
    #range 1 milyar
    #0 sampai satu milyar
    s = rarity["S"]/100
    a = rarity["A"]/100
    b = rarity["B"]/100
    c = rarity["C"]/100
    
    batasAtas = 10000
    #tentukan range dari c
    rangeC = (0,c*batasAtas)
    rangeB = (rangeC[1],rangeC[1]+b*batasAtas)
    rangeA = (rangeB[1],rangeB[1]+a*batasAtas)
    rangeS = (rangeA[1],rangeA[1]+s*batasAtas)
    
    return {"S":rangeS,"A":rangeA,"B":rangeB,"C":rangeC}

def hasilRandomRarity(range:dict, random):
    print(range)
    print(random)
    for x in ["S","A","B","C"]:
        rangeRarity = range[x]
        if random >= rangeRarity[0] and random < rangeRarity[1]:
            return x
    return "M"

def jumlahKeseluruhan(dataConsumable):
    jumlahKeseluruhan = 0
    for item in dataConsumable[1:]:
        jumlahKeseluruhan += int(item["jumlah"])
    return jumlahKeseluruhan

def rumusRarityUmum(pengaruhS,pengaruhA,pengaruhB,pengaruhC,dataConsumable):
    jumlah = jumlahKeseluruhan(dataConsumable)
    return {"S":pengaruhS,"A":pengaruhA,"B":pengaruhB,"C":pengaruhC}


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
    for rarity in ["S","A","B","C"]:
        fraksi = fraksiJumlah(rarity,dataConsumable)
        if fraksi == 0:
            pengaruh[rarity] = 0
        else:
            pengaruh[rarity] = 1/fraksi
    print("inventori")
    print(pengaruh)
    return pengaruh #dictionary of integer

def rumusPengaruhKeseluruhan(pengaruhRarityUmum,pengaruhRarityJumlahInventory):
    for rarity2 in ["S","A","B","C"]:
        for rarity3 in ["S","A","B","C"]:
            pengaruhRarityUmum[rarity2][rarity3] = pengaruhRarityUmum[rarity2][rarity3] * pengaruhRarityJumlahInventory[rarity2]
    print(pengaruhRarityUmum)
    return pengaruhRarityUmum

def rarityPascaPenambahanItem(rarity:str ,jumlah:int, pengaruhKeseluruhan:dict, rarityBasis:dict):
    rarityBaru = {}
    print(rarityBasis)
    for rarity2 in ["S","A","B","C"]:
        rarityBaru[rarity2] = rarityBasis[rarity2] +jumlah*pengaruhKeseluruhan[rarity][rarity2]
    print(rarityBaru)
    return rarityBaru #dictionary of integer

def tingkatkanRarityConsumables(dataConsumable,username):

    # PROSES PENYUSUNAN DISTRIBUSI
    idConsumable = dapatkanItem(dataConsumable,username,campurSkript) # pylint: disable=E0602, E0603
    siap = False
    rarityBasis = {"S":2,"A":16,"B":36,"C":46}
    pengaruhRarityUmum = {"S":rumusRarityUmum(0.4,-0.4/21,-1.6/21,-6.4/21,dataConsumable),"A":rumusRarityUmum(0.7,-0.1,-0.2,-0.4,dataConsumable),"B":rumusRarityUmum(0.025,0.1,-0.025,-0.1,dataConsumable),"C":rumusRarityUmum(0.00625,0.025,0.1,-0.13125,dataConsumable)}
    pengaruhRarityJumlahInventory = rumusRarityJumlahInventory(dataConsumable) #{"S":20}
    pengaruhRarityKeseluruhan = rumusPengaruhKeseluruhan(pengaruhRarityUmum,pengaruhRarityJumlahInventory)
    jumlahBarangDicampur = 0
    while not (siap or idConsumable == "0000000"):
        existStatus = isIdItemAda(idConsumable, dataConsumable) # pylint: disable=E0602, E0603
        if existStatus["keberadaan"]:
            indeks = existStatus["indeks"]
            jumlah = getJumlahPermintaan("campur") # pylint: disable=E0602, E0603
            if jumlah <= int(dataConsumable[indeks]["jumlah"]):
                rarityBasis = rarityPascaPenambahanItem(dataConsumable[indeks]["rarity"],jumlah,pengaruhRarityKeseluruhan,rarityBasis)
                jumlahBarangDicampur += 1
            else:
                print("Jumlah yang kamu masukkan berlebih!")
        else:
            print("item tersebut tidak ada")
        
        # campur lagi?
        lagi = input("Campur yang lain?(Yy)")
        if lagi.upper() == "Y":
            idConsumable = dapatkanItem(dataConsumable,username,campurSkript) # pylint: disable=E0602, E0603
            siap = False
        else:
            siap = True
    else:
        pass

    if jumlahBarangDicampur > 0:
        rangeDistribusi =tentukanRange(rarityBasis)
        print("Dadu dikocok, apa yang akan kamu dapat?")
        angkaRandom = randomize(jumlahBarangDicampur, 3)
        rarityHasil = hasilRandomRarity(rangeDistribusi, angkaRandom)
        print(rarityHasil)
    else:
        print("Kamu tidak mencampur apa-apa")
    
        

    # rarityBasis = {"S":2,"A":16,"B":36,"C":46}
    # pengaruhRarityUmum = {"S":rumusRarityUmum(0.4,-0.4/21,-1.6/21,-6.4/21),"A":rumusRarityUmum(0.1,0.4,-0.1,-0.4),"B":rumusRarityUmum(0.025,0.1,0.4,-0.525),"C":rumusRarityUmum(0.00625,0.025,0.1,-0.13125)}
    # pengaruhRarityJumlahInventory = rumusRarityJumlahInventory(dataConsumable) #{"S":20}
    # pengaruhRarityKeseluruhan = rumusPengaruhKeseluruhan(pengaruhRarityUmum,pengaruhRarityJumlahInventory)
    # rarity = input(">>> ")
    # jumlah = int(input(">>> "))
    

