import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Item {
    width: 1920
    height: 1080

    // Latar belakang untuk halaman ini
    Rectangle {
        anchors.fill: parent
        color: "#2c3e50" // Warna gelap agar fokus ke simulasi
    }

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            text: "Area Simulasi Pygame"
            color: "white"
            font.pixelSize: 32
            Layout.alignment: Qt.AlignHCenter
        }

        // Ini adalah area placeholder tempat jendela Pygame akan muncul.
        // Untuk saat ini, kita hanya beri bingkai.
        Rectangle {
            id: pygamePlaceholder
            width: 800
            height: 600
            color: "#000000" // Latar belakang hitam untuk area game
            border.color: "white"
            Layout.alignment: Qt.AlignHCenter
        }

        Button {
            text: "Mulai Simulasi GLBB"
            Layout.alignment: Qt.AlignHCenter

            // Saat tombol ini diklik, ia akan memanggil FUNGSI di PYTHON.
            // 'pygameBridge' adalah objek Python yang akan kita buat nanti.

        }
    }
}
