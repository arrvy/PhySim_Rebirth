import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import PhySim_Rebirth
import "DataLevel.js" as DB

Pane {
    id: pane
    width: 960
    height: 1080

    property var daftarLevel: []
    signal levelSelected(string indexLevel)

    ScrollView {
        id: scrollView
        x: -12
        y: -12
        width: 960
        height: 1080
        contentHeight: 3240
        contentWidth: 960

        Rectangle {
            id: rectangle
            x: 0
            y: 0
            width: 960
            height: 3240
            color: "#ffffff"

            Text {
                id: text1
                x: 139
                y: 59
                width: 683
                height: 75
                text: qsTr("Select a Level")
                font.pixelSize: 51
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.bold: true
                font.family: "Alte Haas Grotesk"
            }

            ColumnLayout {
                id: column
                x: 0
                y: 300
                anchors.centerIn: parent
                width: parent.width * 0.8
                height: 2940
                //padding: 0
                spacing: 200


                /*Level_button {
                        id: level_button
                        x: (column.width - width)/2
                        width: Level_button.width
                        height: Level_button.height
                        text: modelData.namaLevel
                        enabled: !modelData.terkunci

                        Connections {
                            target: level_button
                            function onClicked() { console.log("clicked: ", modelData.namaLevel ) }
                        }    //"My Button"
                    }*/
                Repeater {
                    id: repeater
                    model: pane.daftarLevel

                    delegate: Level_button {
                        id: level_button
                        Layout.alignment: Qt.AlignHCenter
                        //x: (column.width - width)/2
                        width: Level_button.width
                        height: Level_button.height
                        text: modelData.namaLevel
                        //buttonText: modelData.namaLevel
                        Connections {
                            // Targetkan ID delegate yang baru dibuat.
                            target: level_button
                            function onClicked() {
                                console.log("Tombol sub-level diklik: " + text)
                                // Tambahkan logika untuk mulai simulasi di sini
                                pane.levelSelected(modelData.namaLevel)
                            }
                        }
                    }
                }
            }
        }
    }
}
