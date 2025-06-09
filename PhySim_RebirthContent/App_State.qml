import QtQuick
import PhySim_Rebirth
import "DataLevel.js" as DB

Rectangle {
    id: appRoot

    width: Constants.width
    height: Constants.height

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

       // Connections {
        //target: mainMenuPage

        Connections {
                target: mainMenuPage

                function onGoToselectSimulation(namaMateri) {
                    // Logika for-loop Anda sama persis
                    for (var i = 0; i < DB.materi.length; i++) {
                        if (DB.materi[i].namaMateri === namaMateri) {
                            var levels = DB.materi[i].levels;

                            // ✅ PERBAIKAN SINTAKS: Hapus '.item'. Akses id anak langsung.
                            // Pastikan di dalam Simul_Menu.ui.qml, ada komponen Simul_level dengan id: simul_level
                            simul_Menu.simul_level.daftarLevel = levels;

                            appRoot.state = "simul_MenuState";
                            return
                        }
                    }
                }
            }


    }

    Simul_Menu {
        id: simul_Menu
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

            PropertyChanges {
                target: simul_Menu
                visible: false
            }
        },
        State {
            name: "mainMenuState"
            PropertyChanges {
                target: loginPage
                visible: false
            }

            PropertyChanges {
                target: simul_Menu
                visible: false
            }
        },
        State {
            name: "simul_MenuState"

            PropertyChanges {
                target: mainMenuPage
                visible: false
            }

            PropertyChanges {
                target: loginPage
                visible: false
            }

            PropertyChanges {
                target: simul_Menu
                visible: true }
        }
    ]
}
