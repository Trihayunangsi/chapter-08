Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================== RESTART: C:/Users/acer/Desktop/tugas 08.py ==================
tugas
angka = []
sum = 0
total = 0
while True: 
        data = str(input("Masukkan bilangan : "))
        
        angka.append(data)
       
        if data == "0":
            break
            
       
for datas in angka:
        sum = sum + int(datas)
        
hasil = sum / len(angka)
print("------------------------")
print("Total data  : " +str(len(angka)))
print("Data dalam list : " +str(angka))
print("Jumlah data : " +str(sum))
print("Nilai Rata-ratanya adalah : "+ str(hasil))
print("------------------------")