class Mobil:
    # Constructor
    def __init__(self, merek, warna, tahun):
        # 3 atribut
        self.merek = merek
        self.warna = warna
        self.tahun = tahun

    # Method 1
    def tampilkan_info(self):
        print("=== Informasi Mobil ===")
        print("Merek :", self.merek)
        print("Warna :", self.warna)
        print("Tahun :", self.tahun)

    # Method 2
    def nyalakan_mesin(self):
        print(self.merek, "mesinnya dinyalakan.")

    # Method 3
    def klakson(self): 
        print(self.merek, "berbunyi: TIN TIN!")


# Object 1 memanggil method pertama
mobil1 = Mobil("Toyota", "Hitam", 2022)
mobil1.tampilkan_info()


# Object 2 memanggil method kedua
mobil2 = Mobil("Honda", "Merah", 2023)
mobil2.nyalakan_mesin()

# Object 3 memanggil method ketiga
mobil3 = Mobil("BMW", "Putih", 2024)
mobil3.klakson()
