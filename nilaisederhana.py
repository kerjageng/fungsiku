nama = input("Masukkan Nama\t\t: ")
absen = float(input("Masukkan nilai Absen\t: "))
tugas = float(input("Masukkan nilai Tugas\t: "))
ujian = float(input("Masukkan nilai Ujian\t: "))
na =(absen*0.2)+(tugas*0.3)+(ujian*0.5)
txt = f"Nama\t\t: {nama}\nNilai Absen\t: {absen}\nNilai Tugas\t: {tugas}\n"
txt += f"Nilai Ujian\t: {ujian}\nNilai Akhir\t: {na}\nStatus\t\t: {na >=70}\n"
print(txt)
