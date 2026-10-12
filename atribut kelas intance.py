class Mahasiswa: 
    
    jumlah_mahasiswa = 0
    
    def __init__(self, name, nim, prodi): 
        self.name = name 
        self.nim = nim 
        self.prodi = prodi
        Mahasiswa.jumlah_mahasiswa += 2
        print("Membuat Object Mahasiswa dengan nama " + self.name)
        
mhs1 = Mahasiswa("Valerie Yusga", "25241034", "Teknologi Informasi")
print("Total Mahasiswa : " + str(mhs1.jumlah_mahasiswa))
mhs2 = Mahasiswa("Dapa Roka", "25214006", "Teknik Geodesi")
print("Total Mahasiswa : " + str(mhs2.jumlah_mahasiswa))

print()
print("Total Mahasiswa : " + str(Mahasiswa.jumlah_mahasiswa))