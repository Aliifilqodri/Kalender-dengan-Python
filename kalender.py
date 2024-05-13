# Tampilkan header secara bertahap
print("|===============================")
input("|                               |\n|  Tekan Enter untuk Melanjutkan |\n|===============================|")
print("|                               |")
print("|  Program Menampilkan Kalender |")
print("|===============================|")

# Import library
import calendar

# Input tahun dan bulan
tahun = int(input("\nMasukkan Tahun: "))
bulan = int(input("Masukkan Bulan: "))

# Output hasil
print("\nHasil:")
print(calendar.month(tahun, bulan))
