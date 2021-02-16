print("UJIAN 16 FEBRUARI 2021")
print("Albert Aldo")
print("Soal 1 - Time Converter")
print("="*30)

"""
Soal 1 - Time Converter (30 Poin)
Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). 
Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

HH : Hours, 2 digits, range: 00 - 99

MM : Minutes, 2 digits, range: 00 - 59

SS : Seconds, 2 digits, range: 00 - 59

Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, 
jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string 
akan keluar notifikasi. Invalid Input

Catatan:

Silakan Commit & push (Upload) source code project ke Github Anda, buatlah repo dengan nama Time_Converter. 
Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan 
operational_jkt@purwadhika.com dengan subjek email Exam Modul 1 - JCDS12 - Nama, url bisa dikirimkan 
dalam 1 email yg sama
"""

# masuk = 3666
# print("Masuk =", masuk)
# jam = masuk // 3600
# print("Jam =", jam)
# sisajam = masuk % 3600
# # print("Sisa Jam =", sisajam)
# menit = sisajam // 60
# print("Menit =", menit)
# detik = sisajam % 60
# print("Detik =", detik)

def timeConverter(seconds):
    jam = seconds // 3600
    sisajam = seconds % 3600
    menit = sisajam // 60
    detik = sisajam % 60
    return print("Konversi : " + "%02d" % jam ,":", "%02d" % menit ,":", "%02d" % detik)

try:
    masuk = input("Masukkan detik : ")
    seconds = int(masuk)
    if seconds < 0:
        print("Invalid Input!")
    elif seconds > 359999:
        print("Invalid Input!")
    else:
        timeConverter(seconds)
except:
    print("Invalid Input!")