# 🔗 Blockchain Final Project

## 📖 Deskripsi Project

Project ini merupakan simulasi sederhana teknologi Blockchain menggunakan bahasa pemrograman Python.

Program mengimplementasikan beberapa konsep utama blockchain, yaitu:

- SHA-256 Hash Function
- Merkle Tree
- RSA Digital Signature
- Peer-to-Peer Network (P2P)
- Proof of Work (Mining)
- Blockchain Validation
- Multi Block Chain

Tujuan project ini adalah memahami arsitektur matematika yang digunakan pada teknologi blockchain modern seperti Bitcoin dan Ethereum.

---

## ⚙️ Teknologi yang Digunakan

- Python 3
- Hashlib
- Random
- Time

---

## 📂 Struktur Project

```text
Blockchain_Final_Project/
│
├── blockchain_final_project.py
├── add_test_blockchain.py
├── blockchain_class.py
├── merkle_tree.py
├── rsa_signature.py
├── proof_of_work.py
├── blockchain_validator.py
└── README.md
```

---

## 🔐 SHA-256 Hash Function

SHA-256 digunakan untuk menghasilkan hash unik dari setiap transaksi.

Contoh:

```python
import hashlib

hashlib.sha256(
    "Rima -> Salwa".encode()
).hexdigest()
```

Output:

```text
5f6b1e0c....
```

---

## 🌳 Merkle Tree

Merkle Tree digunakan untuk menggabungkan seluruh hash transaksi menjadi satu hash utama yang disebut Merkle Root.

Contoh transaksi:

1. Rima → Salwa
2. Salwa → Nazwa
3. Nazwa → Andi
4. Andi → Budi

Hasil akhirnya menghasilkan satu Merkle Root yang mewakili seluruh transaksi.

---

## 🔑 RSA Digital Signature

RSA digunakan untuk:

- Enkripsi data
- Dekripsi data
- Tanda tangan digital

Tahapan:

1. Membuat kunci publik
2. Membuat kunci privat
3. Menandatangani pesan
4. Verifikasi tanda tangan

---

## 🌐 Peer to Peer Network

Program mensimulasikan beberapa node blockchain:

- Node A
- Node B
- Node C
- Node D

Setiap node menerima block dengan waktu yang berbeda.

Contoh output:

```text
Node A menerima block dalam 0.25 detik
Node B menerima block dalam 0.42 detik
Node C menerima block dalam 0.68 detik
Node D menerima block dalam 0.17 detik
```

---

## ⛏️ Proof of Work

Proof of Work digunakan untuk mencari nonce yang menghasilkan hash dengan awalan tertentu.

Contoh target:

```text
0000xxxxxxxxxxxxxxxxxxxx
```

Program akan melakukan proses mining hingga target ditemukan.

---

## ⛓️ Blockchain Validation

Setelah block dibuat, program melakukan validasi blockchain.

Pengecekan:

- Previous Hash
- Current Hash
- Integritas Data

Output:

```text
Blockchain VALID
```

---

## ▶️ Cara Menjalankan Program

Clone repository:

```bash
git clone https://github.com/hendriksuenda-prog/Blockchain_Final_Project.git
```

Masuk ke folder project:

```bash
cd Blockchain_Final_Project
```

Jalankan program:

```bash
python blockchain_final_project.py
```

---

## 📊 Hasil Program

Program menampilkan:

- Daftar transaksi
- Hash transaksi
- Merkle Root
- RSA Encryption
- RSA Decryption
- Digital Signature
- Peer-to-Peer Network
- Proof of Work
- Blockchain Validation
- Waktu Eksekusi

---

## 🎯 Kesimpulan

Blockchain merupakan teknologi penyimpanan data terdistribusi yang mengandalkan fungsi hash, struktur Merkle Tree, tanda tangan digital RSA, jaringan Peer-to-Peer, dan mekanisme Proof of Work untuk menjaga keamanan dan integritas data.

Melalui project ini diperoleh pemahaman mengenai konsep dasar matematika dan keamanan yang menjadi fondasi teknologi blockchain modern.

---

## 👩‍💻 Author

Rimawati  
NIM : 240511184  
Program Studi S1 Teknik Informatika
