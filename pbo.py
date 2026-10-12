class PersegiPanjang:
    # class variabel
    jumlah = 0

    def __init__(self, inputPanjang, inputLebar):
        # instance variabel
        self.panjang = inputPanjang
        self.lebar = inputLebar
        PersegiPanjang.jumlah += 1

    def siapa(self):
        return f"Persegi panjang memiliki panjang {self.panjang} dan lebar {self.lebar}"

    def ubahUkuran(self, panjangBaru, lebarBaru):
        self.panjang = panjangBaru
        self.lebar = lebarBaru

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)


persegi1 = PersegiPanjang(10, 5)
persegi2 = PersegiPanjang(8, 4)

print(persegi1.siapa())
persegi1.ubahUkuran(12, 6)

print(f"Panjang {persegi1.panjang}")
print(f"Lebar {persegi1.lebar}")
print(f"Jumlah objek = {PersegiPanjang.jumlah}")

print(f"Luas persegi panjang 1 = {persegi1.hitungLuas()}")
print(f"Keliling persegi panjang 1 = {persegi1.hitungKeliling()}")

print(f"Luas persegi panjang 2 = {persegi2.hitungLuas()}")
print(f"Keliling persegi panjang 2 = {persegi2.hitungKeliling()}")
