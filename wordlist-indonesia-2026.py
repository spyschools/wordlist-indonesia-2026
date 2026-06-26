import random

# ====================================================
# wordlist-indonesia-2026.py
# Generator wordlist untuk keperluan pentest/audit
# password yang SAH (dengan otorisasi) dan riset
# akademis pola password di Indonesia.
#
# PENTING: Gunakan hanya pada sistem yang Anda miliki
# izin resmi untuk diuji (pentest engagement, audit
# internal organisasi sendiri, atau riset akademis
# dengan data yang sudah dianonimkan/disetujui).
# ====================================================

# ---------------------------
# Nama depan populer (deduplikasi)
# ---------------------------
nama_depan = [
    "andi","budi","agus","siti","putri","ani","joko","fariz","eka",
    "rudi","dwi","tono","yudi","adi","rizki","nanda","lina","ratna","dian",
    "wahyu","rio","bagus","sri","wulan","fitri","yusuf","nina","fajar",
    "dimas","arya","bayu","faisal","hendra","ilham","kevin","reza","satria",
    "zaki","aulia","raisa","kayla","naila","keisha","gibran","kaesang"
]

# ---------------------------
# Nama belakang populer
# ---------------------------
nama_belakang = [
    "pratama","saputra","maulana","fauzi","hidayat","permana","setiawan",
    "rahman","wijaya","kurniawan","siregar","hutapea","silalahi","manurung",
    "nababan","sitompul","simanjuntak","syahputra","putra","putri",
    "nugraha","gunawan","santoso","wibowo","susanto","firmansyah"
]

# ---------------------------
# Kota/daerah populer
# ---------------------------
daerah = [
    "jakarta","bandung","surabaya","medan","makassar","bekasi","tangerang",
    "depok","bogor","palembang","semarang","yogyakarta","denpasar","malang",
    "padang","pekanbaru","banjarmasin","pontianak","ambon","jayapura",
    "balikpapan","manado","solo","cirebon","tasikmalaya","cikarang"
]

# ---------------------------
# Kata umum bahasa Indonesia + tren 2025/2026
# ---------------------------
kata_umum = [
    "sayang","cinta","rahasia","indonesia","merdeka","anjing","kucing","bismillah",
    "alhamdulillah","123456","admin","root","ganteng","cantik","gratis","password",
    "sandi","sandiwara","doraemon","naruto","mobilelegends","ff","pubg","tiktok",
    "garuda","nusantara","ikn","pancasila","bhinneka","santuy","mantul","cuan",
    "rebahan","gabut","baper","kepo","jomblo","gacor","bestie","sigma","skibidi",
    "valorant","genshin","minecraft","roblox","spotify","netflix","gopay","dana",
    "ovo","shopee","tokopedia","bca","mandiri","bri","bni"
]

# ---------------------------
# Angka dan tahun (extend hingga 2026, plus pola umum)
# ---------------------------
angka = ["123","1234","12345","123456","007","999","212","08","2025","2026"] \
    + [str(x) for x in range(1985, 2027)]

# ---------------------------
# Suffix simbol umum yang sering dipakai untuk
# memenuhi syarat "harus ada karakter spesial"
# ---------------------------
simbol = ["!", "@", "#", "."]

# ---------------------------
# Peta leetspeak sederhana — pola umum di password Indonesia
# ---------------------------
leet_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}

def to_leet(word):
    return "".join(leet_map.get(c, c) for c in word)

# Gabungan semua base words
base_words = nama_depan + nama_belakang + daerah + kata_umum

# ---------------------------
# Fungsi pembuat kombinasi
# ---------------------------
def generate_variants(words, numbers):
    variants = []
    for w in words:
        variants.append(w)
        variants.append(w.capitalize())
        leet_w = to_leet(w)
        if leet_w != w:
            variants.append(leet_w)
        for n in numbers:
            variants.append(w + str(n))
            variants.append(w + "_" + str(n))
            variants.append(w.capitalize() + str(n))
        for s in simbol:
            variants.append(w.capitalize() + s)
            variants.append(w + s)
    return variants

# Buat kombinasi dasar
wordlist = set(generate_variants(base_words, angka))

# Gabungan nama depan + belakang
for nd in nama_depan:
    for nb in nama_belakang:
        wordlist.add(nd + nb)
        wordlist.add(nd + "_" + nb)
        wordlist.add(nd.capitalize() + nb.capitalize())
        for n in angka:
            wordlist.add(nd + nb + str(n))
            wordlist.add(nd + "_" + nb + str(n))
        for s in simbol:
            wordlist.add(nd.capitalize() + nb.capitalize() + s)

# Gabungan nama + daerah
for nd in nama_depan:
    for d in daerah:
        wordlist.add(nd + d)
        for n in angka:
            wordlist.add(nd + d + str(n))

# Gabungan nama + tahun lahir umum (lebih realistis untuk pola Indonesia)
tahun_lahir = [str(x) for x in range(1985, 2010)]
for nd in nama_depan:
    for th in tahun_lahir:
        wordlist.add(nd + th)
        wordlist.add(nd.capitalize() + th)

# Konversi ke list dan acak
wordlist = list(wordlist)
random.shuffle(wordlist)

# ---------------------------
# Simpan ke file
# ---------------------------
output_file = "wordlist_full_indo_2026.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for w in wordlist:
        f.write(w + "\n")

size_mb = sum(len(w) + 1 for w in wordlist) / (1024 * 1024)

print(f"[+] Wordlist berhasil dibuat: {output_file}")
print(f"[+] Total entry: {len(wordlist):,}")
print(f"[+] Estimasi ukuran file: {size_mb:.2f} MB")
print("[+] Wordlist sudah diacak agar lebih natural.")
print("[!] Gunakan hanya untuk pentest/audit yang berotorisasi atau riset akademis.")
