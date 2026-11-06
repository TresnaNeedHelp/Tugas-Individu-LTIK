def kacau ():
    print("ini adalah fungsi kacaw")

a = int(input("Angka 1 : "))
b = int(input("Angka 2 : "))

def pertambahan():
    hasil = a + b
    print(hasil)

#aisfoiaoifjasoifjoedhfskfj
kacau()
pertambahan()


def LuasBalok(lebar, panjang):
    hasil = lebar * panjang
    print(hasil)


L = 5
P = 10

LuasBalok(L, P)



# seorang mahasiswa ingin membuat program membaca hati seorang wanita
# rumusnya:
# 1. tidak sama dengan iya
# 2. iya sama dengan harus
# 3. pergi sama dengan kejar
# 4. diam sama dengan cukup


def perasaan(sifat):
    if sifat == "tidak":
        print("Wanita tersebut menyatakan iya")
    elif sifat == "iya":
        print("Wanita tersebut menyatakan harus")
    elif sifat == "pergi":
        print("Wanita tersebut menyatakan kejar")
    elif sifat == "diam":
        print("Wanita tersebut menyatakan cukup")

kejadian = 4
pernyataan = []
for tiapkejadian in range (kejadian):
    pernyataan.append(input(f"hal ke-{tiapkejadian + 1} dia merasakan :"))

print(pernyataan)

for tiapPernyataan in pernyataan:
    perasaan(tiapPernyataan)


dataproduk = {
    "P001" : ["Keyboard", 85, "ini adalah tes 1"],
    "P002" : ["Mouse", 88]
}

for TiapKode in dataproduk:
    print("Produk   : ", dataproduk[TiapKode][0])
    print("Nilai    : ", dataproduk[TiapKode][1])
    print("test : ", dataproduk["P001"][2])



def volumeBalok(p, l, t):
    
    VBalok = p * l * t
    print(VBalok)

def volumeKubus(s):
    VKubus = s * 6
    print(VKubus)

def piramidBintang(baris):
    tengah = baris 
    bintang = 1
    for tinggiPiramidBintang in range (baris):
        print(" " * tengah, "* " * bintang)
        tengah -= 1
        bintang += 1


def piramidBalok(BarisBalok):
    tengahBalok = BarisBalok
    Balok = 1

    for tinggiPiramidBalok in range (BarisBalok):
        print(" " * tengahBalok, "[]" * Balok)
        tengahBalok -= 1
        Balok += 1

def nilaiABC(nilai):
    if nilai >= 100:
        print("buset, nilai diatas kemampuan manusia")
    elif nilai >= 50:
        print("yaaa... nilai masih dalam kemampuan manusia")
    else:
        print("Nilai AMSSRBLHGSHARK")

#piramidBalok(int(input("Masukkan tinggi piramid: ")))

volumeBalok(2, 6, 2)

inputuser = int(input("Pilih pilihan 1-5: "))

if inputuser == 1:
    print("Ini adalah program membuat piramida bintang")
    Keinginan = int(input("Masukkan tinggi piramid: "))
    piramidBalok(Keinginan)

if inputuser == 2:
    print("Ini adalah program membuat piramida balok")
    Keinginan = int(input("Masukkan tinggi piramid: "))
    piramidBintang(Keinginan)

if inputuser == 3:
    print("Ini adalah program menghitung volume balok")
    volumeBalok(int(input("Masukkan panjang: ")), int(input("Masukkan lebar: ")), int(input("Masukkan tinggi: ")))

if inputuser == 4:
    print("Ini adalah program menghitung volume kubus")
    volumeKubus(int(input("Masukkan panjang sisi: ")))

if inputuser == 5:
    print("Ini adalah program mencari tahu nilai")
    nilaiABC(int(input("Masukkan nilai: ")))


def sapa(nama, a):
    umur = a + 2
    print(f"Halo {nama}")
    return umur # untuk membuat variabel umur menjadi diketahui secara global, engga cuma di function ini aja

print(sapa("raci", 2))

def sesuatu(*angka):
    print(f"{angka} ")

sesuatu(1,4,1,3,6,2,5,2)


