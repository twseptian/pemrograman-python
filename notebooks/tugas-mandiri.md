# Tugas Mandiri - Praktikum Algoritma & Pemrograman

Silahkan anda kerjakan tugas mandiri sebagai berikut:
1. Buat program dengan menampilkan sebuah permainan: Gunting, Batu, Kertas. seperti pada output video berikut (klik play button video tersebut):

[![asciicast](https://asciinema.org/a/e8P0MH8rpfZWhjmtXqhTyY7ow.svg)](https://asciinema.org/a/e8P0MH8rpfZWhjmtXqhTyY7ow)


2. Buat program dengan menghitung jumlah karakter huruf dan angka pada sebuah string, dengan memanfaatkan function `isdigit` dan `isalpha`, berikut sebagai contoh:

```
inputan = input("Inputan: ")
angka = 0
for x in inputan:
    if x.isdigit():
        angka=angka+1

print("Jumlah Angka: ", angka)
```

ketika dijalankan akan menampilkan output sebagai berikut:

[![asciicast](https://asciinema.org/a/nRIu3jc0vNqWz4LRrTBJaxVut.svg)](https://asciinema.org/a/nRIu3jc0vNqWz4LRrTBJaxVut)

Sebagai catatan, untuk menghitung jumlah karakter huruf, silahkan anda gantikan `isdigit` pada source code di atas dengan `isalpha`. 

**Task:** Tugas anda adalah menggabungkan `isdigit` dan `isalpha` dalam menghitung sejumlah karakter angka dan huruf, seperti pada output video di bawah

[![asciicast](https://asciinema.org/a/rv2dZkUY9vRYwD4EvkB2g9zxP.svg)](https://asciinema.org/a/rv2dZkUY9vRYwD4EvkB2g9zxP)
