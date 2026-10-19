# Tugas Algoritma Enemy Mendeteksi dan Mengejar Player

## Studi Kasus
Player bergerak di dalam sebuah dungeon. Enemy harus:
1. Mendeteksi keberadaan player.
2. Menentukan apakah player berada dalam jangkauan deteksi.
3. Jika player berada dalam jangkauan, mencari jalur menuju player.
4. Bergerak mengikuti jalur yang ditemukan menuju player.

## 1. Identifikasi Algoritma

Algoritma yang digunakan dapat dibagi menjadi beberapa bagian:

### A. Distance / Range Detection
Enemy menghitung jarak antara posisi enemy dan player. Jika jarak lebih kecil atau sama dengan radius deteksi, player dianggap berada dalam jangkauan.

Rumus jarak Euclidean:

`distance = sqrt((x2-x1)^2 + (y2-y1)^2)`

### B. Pathfinding A*
Untuk mencari jalur dari enemy menuju player digunakan algoritma **A* (A-Star)**.

A* cocok digunakan pada dungeon/grid karena dapat mencari jalur dengan mempertimbangkan:
- `g(n)` = biaya dari posisi awal ke node saat ini.
- `h(n)` = perkiraan biaya dari node saat ini ke tujuan.
- `f(n) = g(n) + h(n)` = total nilai untuk menentukan node yang diprioritaskan.

### C. Enemy Movement
Setelah jalur ditemukan, enemy bergerak dari satu posisi ke posisi berikutnya sampai mencapai player.

## 2. Flowchart

Flowchart lengkap tersedia pada file `flowchart.md`.

Alur utamanya:

```text
Mulai
  |
Enemy mendeteksi Player
  |
Hitung jarak Enemy-Player
  |
Apakah Player dalam jangkauan?
  | Tidak
  v
Patroli / menunggu
  |
  +----------------------+
  | Ya                   |
  v                      |
Cari jalur dengan A*     |
  |                      |
Apakah jalur ditemukan?  |
  | Tidak                |
  v                      |
Patroli / menunggu       |
  |                      |
  | Ya                   |
  v                      |
Ambil node berikutnya    |
  |
Enemy bergerak
  |
Apakah sudah mencapai Player?
  | Tidak
  +------> Hitung/update jalur
  |
  | Ya
  v
Selesai / Serang Player
```

## 3. Code Snippet

Kode utama ada di `main.py`.

Program menggunakan:
- Python
- Euclidean distance untuk deteksi jarak
- A* untuk pathfinding
- Grid sederhana sebagai representasi dungeon

## Cara Menjalankan

Pastikan Python sudah terinstall.

```bash
python main.py
```

Program akan menampilkan posisi enemy, player, dan jalur yang ditemukan oleh A*.

## Kesimpulan

Pada kasus ini, kombinasi **Range Detection + A* Pathfinding + Movement** digunakan agar enemy dapat mengetahui apakah player dekat, mencari jalan yang dapat dilewati, lalu bergerak menuju player.
