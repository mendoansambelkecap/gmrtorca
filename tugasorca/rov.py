class KomponenROV:
    def __init__(self, nama, status):
        self.nama = nama
        self.status = status

    def info(self):
        print(self.nama, self.status)

class Thruster(KomponenROV):
    def __init__(self, nama, status, power):
        self.nama = nama
        self.status = status
        self.power = power

    def info(self):
        print("Thruster", self.nama, self.status, self.power)

class Sensor(KomponenROV):
    def __init__(self, nama, status, nilai):
        self.nama = nama
        self.status = status
        self.nilai = nilai

    def info(self):
        print("Sensor", self.nama, self.status, self.nilai)

jumlah = int(input())
daftar_komponen = []

for i in range(jumlah):
    baris = input()
    data = baris.split()
    
    jenis = data[0]
    nama = data[1]
    status = data[2]
    nilai = data[3]

    if jenis.lower() == "thruster":
        objek = Thruster(nama, status, nilai)
        daftar_komponen.append(objek)
    elif jenis.lower() == "sensor":
        objek = Sensor(nama, status, nilai)
        daftar_komponen.append(objek)

print(jumlah)
for k in daftar_komponen:
    k.info()