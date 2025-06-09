import QtQuick
import QtQuick.Controls
import QtQuick.Layouts // Tambahkan untuk Layouts

// Ini adalah komponen QML yang akan menampilkan simulasi Pygame
Rectangle {
    id: pygameView
    // Default width dan height, bisa diubah oleh parent
    width: 800
    height: 600
    color: "lightgray" // Warna latar belakang untuk komponen ini, bisa diubah ke "transparent" jika gambar Pygame memiliki alpha

    // Referensi ke objek Python PygameQmlBridge
    // Objek ini diekspos sebagai 'pygameBridge' dari main.py
    property var bridge: pygameBridge // Menghubungkan ke objek Python

    // Elemen Image untuk menampilkan permukaan Pygame
    Image {
        id: pygameDisplayImage
        anchors.fill: parent // Mengisi seluruh area parent
        fillMode: Image.PreserveAspectFit // Menjaga rasio aspek gambar saat penskalaan
                                       // Pilihan lain: Image.Stretch (mengisi seluruh area, bisa mendistorsi)
        smooth: true // Untuk penskalaan gambar yang lebih halus
        source: bridge.pygameImage // Mengikat ke properti QImage dari Python
        asynchronous: true // Memuat gambar secara asynchronous agar UI tidak terblokir
        visible: source.width > 0 && source.height > 0 // Hanya tampilkan jika gambar memiliki dimensi
    }

    // Contoh tombol untuk berinteraksi dengan simulasi (misalnya, reset)
    Button {
        id: resetButton
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Reset Simulasi"
        width: 150
        height: 40
        y: -20 // Margin dari bawah
        onClicked: {
            bridge.resetSimulation() // Memanggil slot Python
        }
    }

    // Opsional: Area mouse untuk meneruskan event ke Pygame (jika simulasi interaktif)
    MouseArea {
        anchors.fill: parent
        // Menggunakan property mouse.x dan mouse.y
        onClicked: (mouse) => {
            // Meneruskan koordinat klik mouse ke bridge Python
            // Anda mungkin perlu menyesuaikan koordinat berdasarkan fillMode dan penskalaan Image
            bridge.handleMouseClick(mouse.x, mouse.y)
        }
    }
}
