/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import PhySim_Rebirth
import QtQuick.Studio.DesignEffects
import "DataLevel.js" as DB

Rectangle {

    signal goToselectSimulation (int levelIndex)

    id: root

    width: Constants.width
    height: Constants.height

    //width: 1920
    //height: 1080

    Text {
        id: text1
        x: 36
        y: 37
        width: 821
        height: 204
        color: "#29abe2"
        text: "PhySim"
        font.pixelSize: 83
        font.bold: true
        textFormat: Text.RichText
        font.family: "CF Fortusnova Demo"

        DesignEffect {
            effects: [
                DesignDropShadow {
                }
            ]
        }
    }

    Image {
        id: screenshot20250608104826
        x: 106
        y: -1064
        source: "images/Screenshot 2025-06-08 104826.png"
        fillMode: Image.PreserveAspectFit
    }

    Menu_level {
        id: menu_level
        x: 480
        y: 0

        //data: [
            Connections {
                target: menu_level
                function onSelectSimulation (levelIndex) { root.goToselectSimulation(levelIndex) }
            }
        //]

    }
}
