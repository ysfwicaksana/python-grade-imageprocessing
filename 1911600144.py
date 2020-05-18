# install library tabulate & numpy menggunakan pip
# saran : pakai virtualenv
from tabulate import tabulate
import numpy as numpy

def main():
    mahasiswa = int(input("Jumlah mahasiswa: "))
    total = []
    hitung = 0
    insert_data = []

    for mhs in range(mahasiswa):
        print("Input data ke-", mhs+1)
        nama = input("Nama: ")
        nim = input("Nim: ")
        tugas = int(input("Tugas: "))
        uts = int(input("UTS: "))
        uas = int(input("UAS: "))

        # hitung nilai akhir
        nilai_akhir = hitungNilai(tugas, uts, uas)

        total.append(nilai_akhir)

        # konversi huruf mutu
        huruf_mutu = konversiGrade(nilai_akhir)

        hitung = hitung + 1

        elements = [hitung, nama, nim, tugas,
                    uts, uas, nilai_akhir, huruf_mutu]
        insert_data.append(elements)
        data = numpy.array((insert_data), dtype=object)
        print(" ")

    return insert_data, total, data


def cetakData():
    insert_data, total, data = main()
    print("Laporan Nilai Mata Kuliah Data Sains")
    rerata = sum(total) / len(total)

    print(tabulate(insert_data, headers=[
          'No', 'Nama', 'Nim', 'Tugas', 'UTS', 'UAS', 'Nilai nilai', 'Huruf Mutu']))
    print("Total nilai: ", sum(total))
    print("Total rata-rata: ", round(rerata, 2))
    print("Total terendah:", numpy.amin(data[:, 6]))
    print("Total tertinggi:", numpy.amax(data[:, 6]))


def hitungNilai(tugas, uts, uas):
    hasil = int((tugas/100*30) + int(uts/100*30) + int(uas/100*40))
    return hasil


def konversiGrade(nilai_akhir):
    nilai = int(nilai_akhir)
    if nilai >= 90:
        grade = "A"
    elif nilai >= 85:
        grade = "A-"
    elif nilai >= 80:
        grade = "B+"
    elif nilai >= 75:
        grade = "B"
    elif nilai >= 70:
        grade = "B-"
    elif nilai >= 65:
        grade = "C+"
    elif nilai >= 60:
        grade = "C-"
    elif nilai >= 50:
        grade = "D"
    elif nilai >= 40:
        grade = "E"
    elif nilai < 40:
        grade = "T"
    return grade

cetakData()
