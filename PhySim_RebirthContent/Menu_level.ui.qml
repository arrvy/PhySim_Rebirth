import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import PhySim_Rebirth 1.0
import "DataLevel.js" as DB

Pane {

    id: pane
    width: 960
    height: 1080

    signal selectSimulation(int levelIndex)

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
                x: 178
                y: 85
                width: 683
                height: 75
                text: qsTr("Select a Simulation")
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
                spacing: 40


                /*Level_button {
                    id: level_button
                    width: Level_button.width
                    height: Level_button.height
                    text: "My Button"

                    Connections {
                        target: level_button
                        function onClicked() { selectSimulation() }
                    }
                }*/
                Repeater {
                    id: repeater
                    model: DB.materi

                    //spacing: 40
                    delegate: Level_button {
                        id: delegateButton
                        width: Level_button.width
                        height: Level_button.height
                        text:modelData.namaMateri
                        //buttonText: modelData.namaMateri
                        Layout.alignment: Qt.AlignHCenter

                        property string namaMateriDelegate: modelData.namaMateri

                        Connections {
                            target: delegateButton
                            function onClicked() {
                                pane.selectSimulation(index)
                            }
                        }
                    }
                }
            }
        }
    }
}
