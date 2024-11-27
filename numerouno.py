# Mengimpor modul random yang digunakan untuk menghasilkan angka acak
import random

# Kelas untuk merepresentasikan pemain
class Pemain:
    def __init__(self, nama):
        self.nama = nama  # Menyimpan nama pemain yang diberikan saat membuat objek Pemain
        self.score = 0  # Skor pemain dimulai dari 0

    def tambah_skor(self, skor):
        """Menambah skor pemain"""
        self.score += skor  # Menambahkan skor baru ke skor total pemain

    def tampilkan_skor(self):
        """Menampilkan skor saat ini"""
        print(f"\nSkor saat ini untuk {self.nama}: {self.score}")  # Menampilkan skor pemain saat ini


# Kelas untuk mengatur level kesulitan permainan
class Level:
    def __init__(self):
        self.max_number = 100  # Default batas angka maksimal untuk level Hard

    def pilih_level(self):
        """Memilih level kesulitan dan menentukan batas angka maksimal"""
        print("\nPilih level kesulitan:")
        print("1. Easy (Tebakan Angka dari 1-25)")
        print("2. Medium (Tebakan Angka dari 1-50)")
        print("3. Hard (Tebakan Angka dari 1-100)")
        
        # Looping untuk memastikan pemain memilih level yang valid
        while True:
            level = input("Masukkan level yang diinginkan (1/2/3): ")
            if level == "1":
                self.max_number = 25  # Jika level Easy, angka yang bisa ditebak antara 1-25
                break
            elif level == "2":
                self.max_number = 50  # Jika level Medium, angka yang bisa ditebak antara 1-50
                break
            elif level == "3":
                self.max_number = 100  # Jika level Hard, angka yang bisa ditebak antara 1-100
                break
            else:
                print("Pilihan tidak valid. Silakan pilih level yang tersedia.")  # Jika input tidak valid, ulangi

        # Menampilkan level yang dipilih dan batas angka yang relevan
        print(f"\nLevel {['Easy', 'Medium', 'Hard'][int(level) - 1]} dipilih! Angka rahasia berada antara 1 dan {self.max_number}.")

    def get_max_number(self):
        """Mengembalikan batas angka maksimal untuk level yang dipilih"""
        return self.max_number  # Mengembalikan angka maksimal sesuai level yang dipilih


# Kelas untuk logika permainan
class TebakAngkaGame:
    def __init__(self, pemain, level):
        self.pemain = pemain  # Objek pemain yang sedang bermain
        self.level = level  # Objek level yang dipilih

    def mulai_permainan(self):
        """Logika utama permainan tebak angka"""
        # Angka rahasia dihasilkan secara acak antara 1 dan batas angka level
        angka_rahasia = random.randint(1, self.level.get_max_number())
        kesempatan = 5  # Pemain memiliki 5 kesempatan untuk menebak
        skor_giliran = 100  # Skor awal untuk setiap giliran adalah 100
        print(f"\nKamu akan menebak angka antara 1 hingga {self.level.get_max_number()}.")

        giliran = 1  # Menyimpan nomor giliran yang sedang berlangsung
        while kesempatan > 0:  # Selama pemain memiliki kesempatan
            if giliran == 5:  # Pada giliran ke-5, beri opsi menggunakan petunjuk
                gunakan_clue = input("Apakah Anda ingin menggunakan petunjuk terakhir? (y/n): ").lower()
                if gunakan_clue == 'y':
                    skor_giliran -= 15  # Mengurangi skor jika menggunakan petunjuk
                    lower_bound = max(1, angka_rahasia - 5)  # Batas bawah petunjuk
                    upper_bound = min(self.level.get_max_number(), angka_rahasia + 5)  # Batas atas petunjuk
                    print(f"Petunjuk: Angka yang benar berada antara {lower_bound} hingga {upper_bound}.")
                    print("Skor dikurangi -45 poin karena ini giliran terakhir dan kamu menggunakan petunjuk.")
                else:
                    skor_giliran -= 10  # Mengurangi skor jika tidak menggunakan petunjuk
                    print("Skor dikurangi -40 poin karena ini giliran terakhir tanpa menggunakan petunjuk.")

            try:
                tebakan = int(input("Masukkan tebakanmu: "))  # Meminta input dari pemain
            except ValueError:
                print("Harap masukkan angka yang valid.")  # Menangani input yang bukan angka
                continue
            
            if tebakan == angka_rahasia:
                print("Selamat! Kamu berhasil menebak angka dengan benar!")  # Jika tebakan benar
                self.pemain.tambah_skor(skor_giliran)  # Menambahkan skor
                break  # Keluar dari loop jika tebakan benar
            else:
                # Memberikan petunjuk jika tebakan salah
                if tebakan < angka_rahasia:
                    print("Angka yang benar lebih besar!")
                else:
                    print("Angka yang benar lebih kecil!")
                
                # Mengurangi skor berdasarkan giliran
                if giliran == 2:
                    skor_giliran -= 10  # Skor berkurang 10 poin pada giliran ke-2
                    print("Skor dikurangi -10 poin untuk giliran ke-2.")
                elif giliran == 3:
                    skor_giliran -= 10  # Skor berkurang 20 poin pada giliran ke-3
                    print("Skor dikurangi -20 poin untuk giliran ke-3.")
                elif giliran == 4:
                    skor_giliran -= 10  # Skor berkurang 30 poin pada giliran ke-4
                    print("Skor dikurangi -30 poin untuk giliran ke-4.")
                
                kesempatan -= 1  # Mengurangi kesempatan pemain
                giliran += 1  # Meningkatkan nomor giliran
                print(f"Kesempatan tersisa: {kesempatan}")  # Menampilkan sisa kesempatan

        if kesempatan == 0 and tebakan != angka_rahasia:
            print(f"Maaf, kamu kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}.")  # Jika pemain kehabisan kesempatan

        # Menampilkan skor akhir setelah permainan selesai
        print(f"\nSkor akhir kamu dalam permainan ini: {self.pemain.score}")

    def lihat_skor(self):
        """Menampilkan skor pemain"""
        self.pemain.tampilkan_skor()  # Memanggil metode untuk menampilkan skor pemain

    def cara_bermain(self):
        """Menampilkan petunjuk cara bermain"""
        print("\nCara Bermain - Panduan Lengkap:")
        print("1. Pilih Level Kesulitan:")
        print("   - Easy   : Angka rahasia antara 1 hingga 25.")
        print("   - Medium : Angka rahasia antara 1 hingga 50.")
        print("   - Hard   : Angka rahasia antara 1 hingga 100.")
        print("   Pilih level yang sesuai dengan kepercayaan dirimu!")
        
        print("\n2. Game Memilih Angka Rahasia:")
        print("   Setelah memilih level, game akan secara acak memilih sebuah angka rahasia.")
        print("   Tugas kamu adalah menebaknya dengan benar.")

        print("\n3. Lakukan Tebakan:")
        print("   - Kamu memiliki 5 kesempatan untuk menebak angka.")
        print("   - Setiap tebakan yang salah, Game akan memberi petunjuk:")
        print("     > Apakah angka yang benar lebih besar atau lebih kecil dari tebakanmu.")

        print("\n4. Penilaian Skor:")
        print("   - Setiap tebakan yang salah, skor kamu akan berkurang sesuai giliran:")
        print("     * Giliran ke-2: Skor berkurang 10 poin.")
        print("     * Giliran ke-3: Skor berkurang 20 poin.")
        print("     * Giliran ke-4: Skor berkurang 40 poin.")
        print("   - Pada giliran terakhir, kamu memiliki opsi untuk meminta petunjuk:")
        print("     * Jika menggunakan petunjuk, skor berkurang 15 poin.")
        print("     * Jika tidak, skor tetap berkurang 10 poin.")

        print("\n5. Tujuan Permainan:")
        print("   - Tebak angka rahasia dengan jumlah tebakan seminimal mungkin.")
        print("   - Semakin cepat kamu menebak dengan benar, semakin tinggi skor yang didapatkan.")
        
        print("\nTips:")
        print("   - Jangan ragu meminta petunjuk jika kamu merasa buntu, terutama di giliran terakhir.")
        print("   - Tebak angka secara strategis, berdasarkan petunjuk yang diberikan sebelumnya.")
        
        print("\nSelamat bermain dan semoga berhasil!")

    def deskripsi_permainan(self):
        """Menampilkan deskripsi permainan"""
        print("\nDeskripsi Permainan:")
        print('"Numero Uno" adalah permainan tebak angka yang menguji ketajaman insting dan strategi pemain.')
        print("Dalam permainan ini, pemain akan diminta untuk menebak angka rahasia yang telah dipilih secara acak oleh Game.")
        print("Namun, permainan ini bukan hanya soal menebak angka. Setiap tebakan yang salah akan memberi petunjuk berharga,")
        print("memberikan peluang bagi pemain untuk mendekati angka yang benar. Petunjuk yang diberikan akan membantu pemain untuk mengecilkan pilihan,")
        print("dengan memberikan informasi apakah angka yang benar lebih besar atau lebih kecil dari tebakan yang telah dibuat.")
        
        print("\nPermainan ini berlangsung dalam lima giliran, dan setiap giliran membawa tantangan tersendiri.")
        print("Pada setiap tebakan yang salah, pemain akan kehilangan sejumlah poin, dengan pengurangan poin yang semakin besar di setiap giliran.")
        print("Namun, pada giliran terakhir, pemain memiliki kesempatan untuk meminta petunjuk lebih lanjut,")
        print("meskipun akan ada pengurangan skor jika petunjuk digunakan. Ini adalah kesempatan terakhir untuk memenangkan permainan dengan maksimal.")
        
        print("\nTebakan yang benar akan segera mengakhiri permainan dan memberikan skor yang telah dikumpulkan.")
        print("Semakin cepat pemain berhasil menebak angka rahasia, semakin banyak poin yang akan didapatkan.")
        print("Namun, jika kesempatan habis dan pemain belum berhasil menebak angka yang benar, permainan akan berakhir,")
        print("dan angka rahasia akan dibuka sebagai tantangan bagi pemain yang berikutnya.")
        
        print("\nPermainan ini mengajak pemain untuk berpikir secara strategis, memilih apakah akan terus menebak dengan insting atau menggunakan petunjuk,")
        print("dengan mempertimbangkan konsekuensi pada skor di setiap langkah.")
        print("\nApakah kamu siap untuk tantangan ini? Ayo mulai permainan dan buktikan apakah kamu bisa menjadi juara Numero Uno!")


    def mainkan(self):
        """Loop utama untuk menu permainan"""
        print(f"Selamat datang, {self.pemain.nama}!")  # Menyapa pemain dengan nama mereka
        
        # Loop utama untuk memilih menu permainan
        while True:
            print("\nMenu:")
            print("1. Mulai permainan")
            print("2. Lihat skor")
            print("3. Cara Bermain Game Numero Uno")
            print("4. Deskripsi Permainan Numero Uno")
            print("5. Keluar")
            pilihan = input("Pilih opsi (1/2/3/4/5): ")  # Meminta input untuk memilih opsi
            
            if pilihan == "1":
                self.level.pilih_level()  # Memilih level permainan
                self.mulai_permainan()  # Memulai permainan
            elif pilihan == "2":
                self.lihat_skor()  # Menampilkan skor pemain
            elif pilihan == "3":
                self.cara_bermain()  # Menampilkan cara bermain
            elif pilihan == "4":
                self.deskripsi_permainan()  # Menampilkan deskripsi permainan
            elif pilihan == "5":
                print("\nTerima kasih telah bermain!")  # Pesan ketika keluar dari permainan
                print(f"Skor akhir: {self.pemain.score}")  # Menampilkan skor akhir
                break  # Keluar dari loop permainan
            else:
                print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")  # Jika input tidak valid

# Inisialisasi dan mulai permainan jika file ini dijalankan sebagai program utama
if __name__ == "__main__":
    nama = input("Masukkan Nama Pemain: ")  # Meminta nama pemain
    pemain = Pemain(nama)  # Membuat objek pemain
    level = Level()  # Membuat objek level
    game = TebakAngkaGame(pemain, level)  # Membuat objek game dengan pemain dan level
    game.mainkan()  # Memulai permainan