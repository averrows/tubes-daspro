# Program Bantuan
# Berisi prosedur untuk menampilkan bantuan/panduan penggunaan sistem

def bantuan(role):
# I.S. role terdefinisi ("" jika belum login)
# F.S. menampilkan bantuan penggunaan sistem
# KAMUS LOKAL
        
# ALGORITMA
    print("="*25 + " BANTUAN " + "="*25)
    if role == "admin":
        print("register - untuk mendaftarkan user baru")
        print("carirarity - untuk mencari gadget berdasarkan rarity")
        print("caritahun - untuk mencari gadget berdasarkan tahun ditemukan")
        print("tambahitem - untuk menambahkan item ke dalam inventori")
        print("hapus item - untuk menghapus item di dalam inventori")
        print("ubahjumlah - untuk mengubah jumlah gadget dan consumable di dalam inventori")
        print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
        print("riwayatkembali - untuk melihat riwayat pengembalian gadget")
        print("riwayatambil - untuk melihat riwayat pengambilan consumable")
        print("save - untuk menyimpan file yang sudah diubah")
        print("bantuan - untuk memunculkan panduan penggunaan sistem")
        print("keluar - untuk keluar dari sistem")
    elif role == "user":
        print("carirarity - untuk mencari gadget berdasarkan rarity")
        print("caritahun - untuk mencari gadget berdasarkan tahun ditemukan")
        print("pinjam - untuk melakukan peminjaman gadget")
        print("kembalikan - untuk melakukan pengembalian gadget")
        print("minta - untuk meminta consumable")
        print("save - untuk menyimpan file yang sudah diubah")
        print("bantuan - untuk memunculkan panduan penggunaan sistem")
        print("keluar - untuk keluar dari sistem")
    elif role == "":  # jika pengguna belum login
        print("Anda belum login. Silakan login terlebih dahulu.\n")
        print("login - untuk melakukan login ke sistem")
        print("bantuan - untuk memunculkan panduan penggunaan sistem")
        print("keluar - untuk keluar dari sistem")
    print("="*59)
