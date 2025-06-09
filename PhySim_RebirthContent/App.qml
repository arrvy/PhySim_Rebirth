import QtQuick
import QtQuick.Controls
import PhySim_Rebirth // Ganti ini jika nama modul Anda berbeda
import "DataLevel.js" as DB
// Cangkang dari file asli Studio: Gunakan Window sebagai elemen teratas.
Window {
    id: window

    // Ambil ukuran dari Constants.qml, ini sudah benar.
    width: Constants.width
    height: Constants.height

    // Ini adalah ".show()" yang hilang! Perintah untuk menampilkan jendela.
    visible: true
    title: "PhySim Rebirth"

    // Di dalam Window, kita tempatkan Rectangle Anda sebagai panggung utama.
    // Ini adalah 'mesin' state management Anda yang sudah benar.

    App_State{

        anchors.fill : parent
    }


    /*Rectangle {
        id: appRoot

        // Buat Rectangle ini mengisi seluruh area Window.
        anchors.fill: parent
        color: "#2c3e50"

        // State awal, ini sudah benar.
        state: "loginState"

        // Panggil Aktor #1: Halaman Login
        Login01 {
            id: loginPage
            anchors.fill: parent

            // Logika sinyal Anda sudah benar.
            onLoginBerhasil: {
                appRoot.state = "mainMenuState"
            }
        }

        // Panggil Aktor #2: Halaman Main Menu
        Main_Menu {
            id: mainMenuPage
            anchors.fill: parent
        }

        // Definisi state Anda sudah benar.
        states: [
            State {
                name: "loginState"
                PropertyChanges {
                    target: mainMenuPage
                    visible: false
                }
            },
            State {
                name: "mainMenuState"
                PropertyChanges {
                    target: loginPage
                    visible: false
                }
            }
        ]
    }*/
}
