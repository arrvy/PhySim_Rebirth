import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "DataLevel.js" as DB

Item {
    id: simulation
    width: 1920
    height: 1080
    signal simulationBack
    property string namaSimulasi: "Simulasi"
    property string simulationId: "bola_memantul"
    // Latar belakang untuk halaman ini
    Rectangle {
        anchors.fill: parent
        color: "#2c3e50" // Warna gelap agar fokus ke simulasi
    }

    ColumnLayout {
        width: 800
        height: 875
        anchors.centerIn: parent
        spacing: 20

        Text {
            height: 46
            text: "Area Simulasi Pygame : " + namaSimulasi
            color: "white"
            font.pixelSize: 32
            Layout.topMargin: 0
            Layout.bottomMargin: 0
            Layout.minimumHeight: 0
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

            // Integrasikan PygameSimulationView di dalam Rectangle ini
            PygameSimulationView {
                // Mengisi seluruh area simulationContainer
                anchors.fill: parent
                // Sesuaikan width dan height agar sesuai dengan container
                width: parent.width
                height: parent.height
            }
        }

        Button {
            id: button
            text: "Mulai Simulasi GLBB"
            Layout.alignment: Qt.AlignHCenter

            Connections {
                target: button
                function onClicked() {
                    console.log("test")
                    simulation.simulationBack()
                }
            }

            // Saat tombol ini diklik, ia akan memanggil FUNGSI di PYTHON.
            // 'pygameBridge' adalah objek Python yang akan kita buat nanti.
        }
    }
}
