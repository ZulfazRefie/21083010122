from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

a=int(input("Batas: "))
print("")

def oddeven(i):
    if (i%2) == 0:
        return "genap"
    else:
        return "ganjil"

def cetak(i):
    print(i+1, oddeven(i+1), "- punya ID proses", getpid())
    sleep(1)

# Proses Sekuensial:
print("Sekuensial")
sekuensial_awal = time()
for i in range(a):
   cetak(i)
sekuensial_akhir=time()
print("")

# Multiprocessing dengan kelas Process:
print("Multiprocessing.process")
kumpulan_proses=[]
process_awal=time()
for i in range(a):
    p=Process(target=cetak, args=(i, ))
    kumpulan_proses.append(p)
    p.start()
for i in kumpulan_proses:
    p.join()
process_akhir=time()
print("")

#Multiprocessing Dengan Kelas Pool:
print("Multiprocessing.pool")
pool_awal=time()
pool = Pool()
pool.map(cetak,range(0,a))
pool.close()
pool_akhir=time()
print("")

#Bandingkan Waktu Eksekusi
print("Waktu eksekusi Sekuensial:", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi kelas Process:", process_akhir - process_awal, "detik")
print("Waktu eksekusi kelas Pool:", pool_akhir - pool_awal, "detik")
