# Jawaban Tugas

## 1. Algoritma yang digunakan

Pada studi kasus enemy mengejar player, algoritma yang digunakan adalah kombinasi:

**1. Distance / Range Detection**
Digunakan untuk menghitung jarak antara enemy dan player. Jika jarak <= radius deteksi, player dianggap terdeteksi.

**2. A* (A-Star) Pathfinding**
Digunakan untuk mencari jalur dari posisi enemy menuju posisi player dengan melewati jalan yang tersedia dan menghindari dinding.

**3. Movement**
Enemy bergerak mengikuti setiap titik/node yang terdapat pada jalur hasil A*.

### Mengapa A*?

A* merupakan algoritma pathfinding yang menggunakan biaya perjalanan dan estimasi jarak menuju tujuan. Pada dungeon berbentuk grid, A* dapat digunakan untuk mencari jalur dengan efisien.

Rumus:

`f(n) = g(n) + h(n)`

Keterangan:
- `g(n)` = biaya dari titik awal menuju node saat ini.
- `h(n)` = estimasi jarak node saat ini menuju tujuan.
- `f(n)` = total nilai yang digunakan untuk memilih node.

## 2. Flowchart

Flowchart dapat dilihat pada `flowchart.md`.

Urutan proses:
1. Mulai.
2. Enemy mendeteksi player.
3. Hitung jarak enemy dengan player.
4. Jika player tidak berada dalam jangkauan, enemy patroli/menunggu.
5. Jika player berada dalam jangkauan, jalankan A*.
6. Jika jalur tidak ditemukan, enemy kembali patroli/menunggu.
7. Jika jalur ditemukan, enemy bergerak mengikuti jalur.
8. Jika belum mencapai player, proses pencarian/pergerakan dilanjutkan.
9. Jika sudah mencapai player, enemy dapat menyerang atau berinteraksi.

## 3. Implementasi Python

Implementasi lengkap tersedia pada `main.py`.

Program menggunakan grid dungeon:
- `0` = jalan yang dapat dilewati.
- `1` = dinding yang tidak dapat dilewati.

### Output yang diharapkan

Program akan menampilkan:
- posisi enemy;
- posisi player;
- jarak enemy dan player;
- status apakah player terdeteksi;
- jalur yang ditemukan A*;
- langkah pergerakan enemy.

## Struktur Repository

```text
tugas-algoritma-enemy-dungeon/
├── README.md
├── JAWABAN_TUGAS.md
├── flowchart.md
└── main.py
```
