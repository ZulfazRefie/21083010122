# -*- coding: utf-8 -*-
"""Finpro_Prakiraan Cuaca di Provinsi Jawa Barat_B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6-5K7W1NSBGwSLYYxxwEOMn6WOKHJl0
"""

import os
import sys
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-JawaBarat.xml"
response = requests.get(url,verify=False)
r = response.text

data = ['Bandung', 'Banjar', 'Bekasi', 'Ciamis', 'Cianjur', 'Cibinong', 'Cikarang', 'Cimahi', 'Cipanas', 'Cirebon', 'Cisarua', 'Depok', 'Gadog', 'Garut', 'Indramayu', 'Karawang', 'Kota Bogor', 'Kuningan', 'Lembang','Malajengka', 'Parigi', 'Pelabuhan Ratu', 'Puwakarta', 'Singaparna', 'Soreang', 'Subang', 'Kab.Sukabumi', 'Sumber', 'Sumedang', 'Tasikmalaya']
def daftar_kota():
    print("+===========================================================================+", "\n|                                DAFTAR KOTA                                |", "\n+===========================================================================+")
    print('   1. Bandung',  ' '*23, '|  16. Karawang', '\n   2. Banjar', ' '*24, '|  17. Kota Bogor', '\n   3. Bekasi', ' '*24, '|  18. Kuningan', '\n   4. Ciamis', ' '*24, '|  19. Lembang', '\n   5. Cianjur', ' '*23, '|  20. Malajengka', '\n   6. Cibinong', ' '*22, '|  21. Parigi', '\n   7. Cikarang', ' '*22, '|  22. Pelabuhan Ratu', '\n   8. Cimahi', ' '*24, '|  23. Puwakarta', '\n   9. Cipanas', ' '*23, '|  24. Singaparna', '\n  10. Cirebon', ' '*23, '|  25. Soreang', '\n  11. Cisarua', ' '*23, '|  26. Subang', '\n  12. Depok', ' '*25, '|  27. Kab.Sukabumi', '\n  13. Gadog', ' '*25, '|  28. Sumber', '\n  14. Garut', ' '*25, '|  29. Sumedang', '\n  15. Indramayu', ' '*21, '|  30. Tasikmalaya')
    print("+===========================================================================+")

prakiraan = {'Pagi': '' , 'Siang': '', 'Malam': ''}
kode = {
'0': 'Cerah / Clear Skies',
'1': 'Cerah Berawan / Party Cloudy',
'2': 'Cerah Berawan / Partly Cloudy',
'3': 'Berawan / Mostly Cloudy',
'4': 'Berawan Tebal / Overcast',
'5': 'Udara Kabur / Haze',
'10': 'Asap / Smoke',
'45': 'Kabut / Fog',
'60': 'Hujan Ringan / Light Rain',
'61': 'Hujan Sedang / Rain',
'63': 'Hujan Lebat / Heavy Rain',
'80': 'Hujan Lokal / Isolated Shower',
'95': 'Hujan Petir / Severe Thunderstorm',
'97': 'Hujan Petir / Severe Thunderstorm'
}

JawaBarat = bs(r,"xml")

def waktu_akan_datang(date_format="%A, %d %B %Y", add_days=''):
    waktu_n_datang = datetime.now() + timedelta(days=add_days)
    return waktu_n_datang.strftime(date_format)
x = datetime.now()
y = waktu_akan_datang(add_days= 1)
z = waktu_akan_datang(add_days= 2)
a = x.strftime("%A, %d %B %Y")
b_now = x.strftime("%Y%m%d")
b_tom = waktu_akan_datang(date_format="%Y%m%d", add_days=1)
b_dtom = waktu_akan_datang(date_format="%Y%m%d", add_days=2)

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali ke main menu ")
    os.system('clear' if (os.name=='nt') else 'clear')
while True:
    print("\n",
          "\n+===========================================================================+",
          "\n|                SELAMAT DATANG DI APLIKASI PRAKIRAAN CUACA                 |",
          "\n|                    Khusus Wilayah Jawa Barat dari BMKG                    |",
          "\n+===========================================================================+",
          "\n")
    print("+===========================================================================+",
          "\n|                                    MENU                                   |", 
          "\n+===========================================================================+",
          "\n   1. Prakiraan Cuaca Hari Ini \n   2. Prakiraan Cuaca Selama 3 Hari \n   3. Exit", 
          "\n+===========================================================================+")
    menu = input("Masukkan pilihan Anda : ")
    print("\n")
    if menu == "1":
        daftar_kota()
        desc = int(input("Pilih kota (1-38): "))
        print('\n')
        if desc in range (1,39):
            cuacaJabar = JawaBarat.find(description=data[desc-1]).find(id="weather")
            h6 = cuacaJabar.find(h='6').value.string
            h12 = cuacaJabar.find(h='12').value.string
            h18 = cuacaJabar.find(h='18').value.string
            
            prakiraan['Pagi'] = kode[h6]
            prakiraan['Siang'] = kode[h12]
            prakiraan['Malam'] = kode[h18]

            tminJabar = JawaBarat.find(description=data[desc-1]).find(id="tmin")
            tminnow = tminJabar.find(day=b_now).value.string
        
            tmaxJabar = JawaBarat.find(description=data[desc-1]).find(id="tmax")
            tmaxnow = tmaxJabar.find(day=b_now).value.string
            
            huminJabar = JawaBarat.find(description=data[desc-1]).find(id="humin")
            huminnow = huminJabar.find(day=b_now).value.string
            
            humaxJabar = JawaBarat.find(description=data[desc-1]).find(id="humax")
            humaxnow = humaxJabar.find(day=b_now).value.string
            
            print("+===========================================================================+")
            print('|'+'Prakiraan Cuaca Hari Ini di {}'.format(data[desc-1]).center(75, ' ')+'|')
            print('|'+"{}".format(a).center(75, ' ')+'|')
            print("+===========================================================================+")
            print('  Pagi        : ', prakiraan['Pagi'])
            print('  Siang       : ', prakiraan['Siang'])
            print('  Malam       : ', prakiraan['Malam'])
            print('  Temperatur  : ', tminnow, '-', tmaxnow, 'celcius')
            print('  Kelembapan  : ', huminnow, '% -', humaxnow, '%')
            print("+===========================================================================+")
            kembali()
        else:
            print("+===========================================================================+")
            print("|                        Maaf Pilihan Anda Tidak Ada                        |")
            print("|     Silahkan Coba Lagi dan Pastikan Pilihan Anda Terdapat pada Daftar     |")
            print("+===========================================================================+")
            kembali()
            
    elif menu == "2":
        daftar_kota()
        desc = int(input("Pilih kota (1-38): "))
        print('\n')
        if desc in range (1,39): 
            cuacaJabar = JawaBarat.find(description=data[desc-1]).find(id="weather")
            h6 = cuacaJabar.find(h='6').value.string
            h12 = cuacaJabar.find(h='12').value.string
            h18 = cuacaJabar.find(h='18').value.string
            h30 = cuacaJabar.find(h='30').value.string
            h36 = cuacaJabar.find(h='36').value.string
            h42 = cuacaJabar.find(h='42').value.string
            h54 = cuacaJabar.find(h='54').value.string
            h60 = cuacaJabar.find(h='60').value.string
            h66 = cuacaJabar.find(h='66').value.string
            
            prakiraan['Pagi'] = kode[h6]
            prakiraan['Siang'] = kode[h12]
            prakiraan['Malam'] = kode[h18]
            prakiraan['Besok Pagi'] = kode[h30]
            prakiraan['Besok Siang'] = kode[h36]
            prakiraan['Besok Malam'] = kode[h42]
            prakiraan['Lusa Pagi'] = kode[h54]
            prakiraan['Lusa Siang'] = kode[h60]
            prakiraan['Lusa Malam'] = kode[h66]
            
            tminJabar = JawaBarat.find(description=data[desc-1]).find(id="tmin")
            tminnow = tminJabar.find(day=b_now).value.string
            tmintom = tminJabar.find(day=b_tom).value.string
            tmindtom = tminJabar.find(day=b_dtom).value.string
        
            tmaxJabar = JawaBarat.find(description=data[desc-1]).find(id="tmax")
            tmaxnow = tmaxJabar.find(day=b_now).value.string
            tmaxtom = tmaxJabar.find(day=b_tom).value.string
            tmaxdtom = tmaxJabar.find(day=b_dtom).value.string
            
            huminJabar = JawaBarat.find(description=data[desc-1]).find(id="humin")
            huminnow = huminJabar.find(day=b_now).value.string
            humintom = huminJabar.find(day=b_tom).value.string
            humindtom = huminJabar.find(day=b_dtom).value.string
            
            humaxJabar = JawaBarat.find(description=data[desc-1]).find(id="humax")
            humaxnow = humaxJabar.find(day=b_now).value.string
            humaxtom = huminJabar.find(day=b_tom).value.string
            humaxdtom = huminJabar.find(day=b_dtom).value.string
            
            print("+===========================================================================+")
            print('|'+'Prakiraan Cuaca di {}'.format(data[desc-1]).center(75, ' ')+'|')
            print("+===========================================================================+")
            print("{}".format(a).center(77, ' '))
            print(' ')
            print('  Pagi        : ', prakiraan['Pagi'])
            print('  Siang       : ', prakiraan['Siang'])
            print('  Malam       : ', prakiraan['Malam'])
            print('  Temperatur  : ', tminnow, '-', tmaxnow, 'celcius')
            print('  Kelembapan  : ', huminnow, '% -', humaxnow, '%')
            print('_'*77)
            print("{}".format(y).center(77, ' '))
            print(' ')
            print('  Pagi        : ', prakiraan['Besok Pagi'])
            print('  Siang       : ', prakiraan['Besok Siang'])
            print('  Malam       : ', prakiraan['Besok Malam'])
            print('  Temperatur  : ', tmintom, '-', tmaxtom, 'celcius')
            print('  Kelembapan  : ', humintom, '% -', humaxtom, '%')
            print('_'*77)
            print("{}".format(z).center(77, ' '))
            print(' ')
            print('  Pagi        : ', prakiraan['Lusa Pagi'])
            print('  Siang       : ', prakiraan['Lusa Siang'])
            print('  Malam       : ', prakiraan['Lusa Malam'])
            print('  Temperatur  : ', tmindtom, '-', tmaxdtom, 'celcius')
            print('  Kelembapan  : ', humindtom, '% -', humaxdtom, '%')
            print("+===========================================================================+")
            kembali()
        else:
            print("+===========================================================================+")
            print("|                        Maaf Pilihan Anda Tidak Ada                        |")
            print("|     Silahkan Coba Lagi dan Pastikan Pilihan Anda Terdapat pada Daftar     |")
            print("+===========================================================================+")
            kembali()
            
    elif menu == "3":
        print("+===========================================================================+")
        print("|                Terima Kasih Telah Menggunakan Layanan Kami                |")
        print("|                    Kepuasan Anda Adalah Prioritas Kami                    |")
        print("+===========================================================================+")
        break
        
    else:
        print("+===========================================================================+")
        print("|                        Maaf Pilihan Anda Tidak Ada                        |")
        print("|      Silahkan Coba Lagi dan Pastikan Pilihan Anda Terdapat pada Menu      |")
        print("+===========================================================================+")
        kembali()

