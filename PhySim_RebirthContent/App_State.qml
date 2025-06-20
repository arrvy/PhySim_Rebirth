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

                function onGoToselectSimulation(levelIndex) {
                    appRoot.state = "simul_MenuState";
                    // Logika for-loop Anda sama persis
                    var levels = DB.materi[levelIndex].levels;
                    console.log(levels)
                    simul_Menu.dataUntukLevel = levels;


                }
        }
    }




    Simul_Menu {
        id: simul_Menu
        anchors.fill: parent

        Connections {
            target: simul_Menu
            function onGoTolevelSelected(indexLevel) {
                console.log("clicked")
                appRoot.state = "pygame_State"
                simulasiPygame.namaSimulasi = indexLevel



            }
        }



    }

    SimulasiPygame {
        id: simulasiPygame

        Connections {
            target: simulasiPygame
            function onSimulationBack() {
                console.log("clicked")
                appRoot.state = "simul_MenuState"

            }
        }

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

            PropertyChanges {
                target: simulasiPygame
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

            PropertyChanges {
                target: simulasiPygame
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

                PropertyChanges {
                    target: simulasiPygame
                    visible: false
                }
        },
        State {
            name: "pygame_State"

            PropertyChanges {
                target: simul_Menu
                visible: false
            }

            PropertyChanges {
                target: mainMenuPage
                visible: false
            }

            PropertyChanges {
                target: loginPage
                visible: false
            }
        }
    ]
}
