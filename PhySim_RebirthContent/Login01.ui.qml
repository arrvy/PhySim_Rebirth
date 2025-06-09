

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
import QtQuick.Studio.Components 1.0

Rectangle {

    signal loginBerhasil

    id: rectangle1
    width: Constants.width
    height: Constants.height
    //width:1920
    //height:1080
    border.color: "#1c3e69"
    gradient: Gradient {
        GradientStop {
            position: 0
            color: "#1e79d6"
        }

        GradientStop {
            position: 1
            color: "#54ade9"
        }
        orientation: Gradient.Horizontal
    }

    property alias text1Fontfamily: judul.font.family

    Image {
        id: screenshot20250608104826
        x: -248
        y: -955
        source: "images/Screenshot 2025-06-08 104826.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: screenshot20250608110910
        x: -126
        y: -1031
        source: "images/Screenshot 2025-06-08 110910.png"
        fillMode: Image.PreserveAspectFit
    }

    Rectangle {
        id: rectangle
        x: 311
        y: 239
        width: 482
        height: 584
        opacity: 0.9
        color: "#ffffff"
        radius: 16
        border.color: "#c6d8ee"

        DesignEffect {
            layerBlurRadius: 0
            backgroundBlurRadius: 0
            effects: [
                DesignDropShadow {
                    offsetX: 8
                    offsetY: 13
                }
            ]
        }

        Row {
            id: row
            x: 9
            y: 8
            width: 466
            height: 80
        }

        RoundButton {
            id: loginButton
            x: 131
            y: 315
            width: 221
            height: 40
            radius: 13
            text: "LOGIN"

            DesignEffect {
                effects: [
                    DesignDropShadow {}
                ]
            }

            Connections {
                target: loginButton


                /*function onClicked() {
                    myStackView.push("Main_Menu.ui.qml")
                }*/
            }

            Connections {
                target: loginButton
                function onClicked() {
                    loginBerhasil()
                }
            }
        }

        Text {
            id: judul
            x: 124
            y: 20
            width: 233
            height: 52
            text: qsTr("Physim Rebirth")
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.bold: true
            font.family: "Persona Aura"
            anchors.verticalCenterOffset: -244
            anchors.horizontalCenterOffset: 1
            font.pointSize: 17
            anchors.centerIn: parent
        }

        Button {
            id: forgotButton
            x: 194
            y: 361
            width: 94
            height: 17
            visible: true
            //text: qsTr("FORGOT PASSWORD?")
            flat: true
            icon.height: 14
            icon.width: 11

            DesignEffect {}

            Text {
                id: forgot_text
                x: 0
                y: 0
                width: 132
                height: 17
                visible: true
                color: "#1f359e"
                text: qsTr("Forgot Password?")
                font.pixelSize: 12
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
            }
        }
    }

    Rectangle {
        id: email_rect
        x: 343
        y: 399
        width: 418
        height: 43
        color: "#ffffff"
        radius: 4
        border.color: "#1d3a5d"
        border.width: 1

        TextField {
            id: email_input
            x: 8
            y: 2
            width: 402
            height: 40
            color: "#000000"
            layer.enabled: false
            baselineOffset: 19
            smooth: true
            enabled: true
            placeholderText: qsTr("Enter you Email")
            //background: null
        }

        DesignEffect {
            effects: [
                DesignDropShadow {}
            ]
        }
    }

    Rectangle {
        id: pw_rect
        x: 343
        y: 467
        width: 418
        height: 43
        color: "#ffffff"
        radius: 4
        border.color: "#1d3a5d"
        border.width: 1
        TextField {
            id: pw_input
            x: 8
            y: 2
            width: 402
            height: 40
            color: "#000000"
            echoMode: TextInput.Password
            smooth: true
            placeholderText: qsTr("Enter you Password")
            layer.enabled: false
            enabled: true
            baselineOffset: 19
            //background: null
        }

        DesignEffect {
            effects: [
                DesignDropShadow {}
            ]
        }
    }

    Text {
        id: text1
        x: 972
        y: 259
        width: 821
        height: 204
        color: "#ffffff"
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Alte Haas Grotesk'; font-size:50pt;\">Explore your </span></p>\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Alte Haas Grotesk'; font-size:50pt;\">Journey</span></p></body></html>"
        font.pixelSize: 50
        textFormat: Text.RichText
        font.family: "Stretch Pro"
    }

    GroupItem {
        id: motion_group
        x: 972
        y: 441

        Image {
            id: motion1
            x: 0
            y: 0
            width: 55
            height: 39
            source: "images/symbol/motion.png"
            smooth: true
            antialiasing: false
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: motion_text1
            x: 52
            y: 0
            width: 336
            height: 40
            color: "#ffffff"
            text: qsTr("Numerous Fundamental Theory")
            font.pixelSize: 17
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            font.family: "Alte Haas Grotesk"
        }
    }

    GroupItem {
        id: ideas_group
        x: 977
        y: 566

        Image {
            id: ideas
            x: 2
            y: 8
            width: 34
            height: 29
            source: "images/symbol/ideas.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: console_text2
            x: 47
            y: 0
            width: 336
            height: 40
            color: "#ffffff"
            text: qsTr("Quiz for Exercise")
            font.pixelSize: 17
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            font.family: "Alte Haas Grotesk"
        }
    }

    GroupItem {
        id: science_group
        x: 979
        y: 527

        Image {
            id: science
            x: 0
            y: 3
            width: 33
            height: 33
            source: "images/symbol/science.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: console_text1
            x: 45
            y: 0
            width: 336
            height: 40
            color: "#ffffff"
            text: qsTr("For All")
            font.pixelSize: 17
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            font.family: "Alte Haas Grotesk"
        }
    }

    GroupItem {
        id: console_group
        x: 979
        y: 484

        Image {
            id: console1
            x: 0
            y: 3
            width: 33
            height: 33
            source: "images/symbol/console.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: console_text
            x: 45
            y: 0
            width: 336
            height: 40
            color: "#ffffff"
            text: qsTr("Fun to simulate")
            font.pixelSize: 17
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            font.family: "Alte Haas Grotesk"
        }
    }
}
