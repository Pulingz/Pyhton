from KaryawanClass import Karyawan
from HelloClass import Hello

x = Hello()
karyawan1 = Karyawan("Udin",500)
karyawan2 = Karyawan("Ucup",1000)
karyawan3 = Karyawan("Ucup",8000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)

print(x.greetings())
