// File: DataLevels.js

// Baris ini penting, membuat file bisa diakses dari QML
.pragma library

// Kita buat "kamus" besar berisi semua data
var materi = [
    {
        "namaMateri": "Kinematika",
        "deskripsi": "Mempelajari gerak benda",
        "levels": [
            { "namaLevel": "Gerak Lurus", "terkunci": false },
            { "namaLevel": "Gerak Parabola", "terkunci": true },
            { "namaLevel": "Gerak Melingkar", "terkunci": true }
        ]
    },
    {
        "namaMateri": "Dinamika",
        "deskripsi": "Mempelajari penyebab gerak",
        "levels": [
            { "namaLevel": "Hukum Newton", "terkunci": false },
            { "namaLevel": "Gaya Gesek", "terkunci": false }
        ]
    },
    {
        "namaMateri": "Optik",
        "deskripsi": "Mempelajari tentang cahaya",
        "levels": [
            { "namaLevel": "Cermin Datar", "terkunci": true }
        ]
    }
];
