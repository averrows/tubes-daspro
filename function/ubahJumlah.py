from function.validasiTahundanJumlah import jumlahbesarkecil # pylint: disable=import-error
from function.validasiID import IDValid, IDditemukan # pylint: disable=import-error

def ubahjumlah(gadgetData,consumableData):
    # ALGORITMA
    status = False
    while not status:
        ID = input("Masukkan ID: ")
        if IDValid(ID):
            if ID[0] == "G":
                if len(gadgetData) == 1:
                # validasi data kosong    
                    print("Maaf data tidak tersedia")
                else:
                    if IDditemukan(ID, gadgetData):
                        ubahGadget(ID, gadgetData)
                    else:
                        print("Gagal menambahkan item karena ID tidak tersedia.")

def ubahGadget(ID, gadgetData):
    