class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0
    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_profil(self):
        print(f"Nama = {self.nama}")
        print(f"Gaji = {self.gaji}")

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)
