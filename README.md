# Wordlist Generator Indonesia 2026

Generator wordlist berbasis pola nama, daerah, dan kata umum di Indonesia. Dibuat untuk mendukung **pentest/security assessment yang berotorisasi**, **audit kekuatan password internal**, dan **riset akademis** terkait pola password di Indonesia.

> ⚠️ **Disclaimer**
> Tool ini hanya untuk digunakan pada sistem yang Anda miliki izin sah untuk diuji (pentest engagement dengan kontrak/otorisasi tertulis, audit internal organisasi sendiri, atau riset akademis dengan data yang sudah disetujui/dianonimkan). Penggunaan terhadap sistem atau akun pihak lain tanpa izin adalah **pelanggaran hukum** (di Indonesia diatur antara lain dalam UU ITE). Pembuat tidak bertanggung jawab atas penyalahgunaan tool ini.

---

## Fitur

- Kombinasi nama depan + nama belakang + daerah populer di Indonesia
- Variasi tahun (1985–2026) dan pola angka umum (`123456`, `2025`, dll)
- Variasi leetspeak (`a→4`, `e→3`, `i→1`, `o→0`, `s→5`)
- Suffix simbol umum (`!`, `@`, `#`, `.`) untuk sistem yang mewajibkan karakter spesial
- Kata tren 2025/2026 (istilah gaming, e-wallet, slang lokal)
- Output otomatis diacak (shuffle) agar tidak berurutan secara prediktif
- Dedup otomatis menggunakan `set()`

## Persyaratan

- Python 3.8 atau lebih baru
- Tidak ada dependency eksternal (hanya modul standar `random`)

## Instalasi di Kali Linux

Kali Linux sudah menyertakan Python 3 secara default, jadi instalasinya singkat.

### 1. Cek versi Python

```bash
python3 --version
```

Jika belum ada atau versinya terlalu lama:

```bash
sudo apt update
sudo apt install python3 -y
```

### 2. Clone repository

```bash
git clone https://github.com/spyschools/wordlist-indonesia-2026.git
cd wordlist-indonesia-2026
```

Atau jika hanya mengunduh file tunggal:

```bash
wget https://raw.githubusercontent.com/spyschools/wordlist-indonesia-2026/main/wordlist-indonesia-2026.py
```

### 3. (Opsional) Buat virtual environment

Tidak wajib karena tidak ada dependency eksternal, tapi disarankan untuk kebersihan environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Jalankan script

```bash
python3 wordlist-indonesia-2026.py
```

Output akan tersimpan sebagai `wordlist_full_indo_2026.txt` di direktori yang sama.

### 5. (Opsional) Beri izin eksekusi langsung

```bash
chmod +x wordlist-indonesia-2026.py
./wordlist-indonesia-2026.py
```

> Tambahkan shebang `#!/usr/bin/env python3` di baris pertama file jika ingin menjalankannya langsung seperti di atas.

## Contoh Output

```
[+] Wordlist berhasil dibuat: wordlist_full_indo_2026.txt
[+] Total entry: 209,274
[+] Estimasi ukuran file: 3.25 MB
[+] Wordlist sudah diacak agar lebih natural.
[!] Gunakan hanya untuk pentest/audit yang berotorisasi atau riset akademis.
```

## Penggunaan dengan Tools Pentest

Wordlist ini paling efektif dipadukan dengan **rules engine** seperti yang tersedia di Hashcat atau John the Ripper, agar variasi kapitalisasi/angka/simbol yang belum ter-cover otomatis ditambahkan.

### Hashcat

```bash
hashcat -m <hash-mode> hash.txt wordlist_full_indo_2026.txt -r /usr/share/hashcat/rules/best64.rule
```

### John the Ripper

```bash
john --wordlist=wordlist_full_indo_2026.txt --rules hash.txt
```

### Hydra (uji login service, dengan otorisasi)

```bash
hydra -l admin -P wordlist_full_indo_2026.txt ssh://<target-ip-yang-diotorisasi>
```

## Kustomisasi

Buka `wordlist-indonesia-2026.py` dan sesuaikan list berikut sesuai kebutuhan target/riset Anda:

| Variabel | Isi |
|---|---|
| `nama_depan` | Nama depan populer |
| `nama_belakang` | Nama belakang/marga populer |
| `daerah` | Kota/daerah di Indonesia |
| `kata_umum` | Kata umum & istilah tren |
| `angka` | Pola angka/tahun |
| `simbol` | Karakter spesial suffix |

## Struktur Project

```
.
├── wordlist-indonesia-2026.py   # Script generator utama
├── README.md                    # Dokumentasi ini
└── wordlist_full_indo_2026.txt  # Output (dibuat otomatis setelah run)
```

## Lisensi

Gunakan dan modifikasi secara bebas untuk keperluan riset dan pengujian keamanan yang sah. Tidak ada garansi apa pun (disediakan "as-is").

## Kontribusi

Pull request untuk menambah pola, memperbaiki dataset nama/daerah, atau optimasi performa sangat diterima.
