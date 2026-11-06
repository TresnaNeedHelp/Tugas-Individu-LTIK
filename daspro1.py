#Iqbal Fadhil Tresnadarma
#2611911
#RPL 1C

print("Latihan 1.1 - Fibonacci")
def deretFibonaci(TotalDeretanAngka):
    listFibonaci = []
    a = 1
    b = 1
    listFibonaci.append(a)
    listFibonaci.append(b)

    for tiapangka in range (TotalDeretanAngka):
        c = a + b

        listFibonaci.append(c)

        a = b
        b = c

    print(listFibonaci)


deretFibonaci(int(input("Masukkan total deret angka: ")))
print()


print("Latihan 1.2 - Volume Tabung")
def VolumeTabung (tinggi, jarijari):
    VTabung = (22/7 * jarijari ** 2 * tinggi) // 1
    print(VTabung)

VolumeTabung(12, 8)
print()

print("Latihan 1.3 - Rata rata tanpa diketahui batasnya berapa")
input_angka = []

def nilai_total(*angka):
    total = sum(angka)
    return total

def nilai_rata_rata(*angka):
    total = sum(angka)
    jumlah_angka = len(angka)
    rata_rata = total / jumlah_angka
    return rata_rata

jumlah_angka = int(input('Masukan jumlah angka nya: '))

for i in range(jumlah_angka): 
    input_angka.append(int(input(f"Masukan Angka ke {i+1}: ")))

print(f"Total : {nilai_total(*input_angka)}")
print(f"Rata-rata : {nilai_rata_rata(*input_angka)}")
print()

print("""Halo Daspro2023""")
def login (PasswordInput):
    kesempatan = 2
    password = "Latihan"

    PasswordInput = ""
    while kesempatan > 0 :
        if PasswordInput == password :
            print("Selamat datang Daspro2023 !")
            break
        else:
            print("Password salah! ")
            kesempatan -= 1
            PasswordInput = input("Masukkan Password : ")
        if kesempatan == 0 :
            print("gagal login")
            break

login(input("Masukkan password : "))



print("Latihan 2 - Login")

jumlah_kesempatan = 3

def kesempatan(password):
    if password == "Latihan":
        return True
    else:
        return False
        

print("Login: \n")
jumlah_kesempatan = 3

while jumlah_kesempatan != 0:
    username = input("Usename: ")
    password = kesempatan(input("Password: "))
    if not password:
        print("Password salah")
        jumlah_kesempatan -= 1
        if jumlah_kesempatan != 0:
            print(f"Sisa kesempatan login {jumlah_kesempatan}x lagi")
    else:
        print("Login berhasil")
        break
else:
    print("Kesempatan login Anda habis.")

print()



print("Latihan 3 - konversi waktu")

def konversi_ke_detik(jam, menit, detik):
    return (jam * 3600) + (menit * 60) + detik


def selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    total_mulai = konversi_ke_detik(jam_mulai, menit_mulai, detik_mulai)
    total_selesai = konversi_ke_detik(jam_selesai, menit_selesai, detik_selesai)

    selisih = total_selesai - total_mulai

    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60

    return jam, menit, detik


# Input dari user
print("=== Waktu Mulai ===")
jam_mulai = int(input("Jam   : "))
menit_mulai = int(input("Menit : "))
detik_mulai = int(input("Detik : "))

print("=== Waktu Selesai ===")
jam_selesai = int(input("Jam   : "))
menit_selesai = int(input("Menit : "))
detik_selesai = int(input("Detik : "))

hasil_jam, hasil_menit, hasil_detik = selisih_waktu(
    jam_mulai, menit_mulai, detik_mulai,
    jam_selesai, menit_selesai, detik_selesai
)

print(f"Selisihnya adalah {hasil_jam} jam - {hasil_menit} menit - {hasil_detik} detik")