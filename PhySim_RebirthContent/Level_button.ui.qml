

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls

Button {
    id: control

    implicitWidth: Math.max(
                       buttonBackground ? buttonBackground.implicitWidth : 0,
                       textItem.implicitWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(
                        buttonBackground ? buttonBackground.implicitHeight : 0,
                        textItem.implicitHeight + topPadding + bottomPadding)
    leftPadding: 4
    rightPadding: 4
    rotation: buttonBackground.rotation

    //text: "My Button"
    //text: delegateButton.namaMateriDelegate
    background: buttonBackground
    Rectangle {
        id: buttonBackground
        x: 0
        y: 0
        width: 280
        height: 102
        implicitWidth: width
        implicitHeight: height
        opacity: enabled ? 1 : 0.3
        radius: 2
        border.color: "#047eff"
        rotation: 0
        gradient: Gradient {
            GradientStop {
                id: gradientStop
                position: 0
                color: "#1e79d6"
            }

            GradientStop {
                position: 1
                color: "#5ca4ed"
            }
            orientation: Gradient.Vertical
        }
    }

    contentItem: textItem
    Text {
        id: textItem

        opacity: enabled ? 1.0 : 0.3
        color: "#000000"
        text: control.text
        //text: "haha"
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    states: [
        State {
            name: "normal"
            when: !control.down && !control.hovered

            PropertyChanges {
                target: buttonBackground
                color: "#00000000"
                border.color: "#047eff"
            }

            PropertyChanges {
                target: textItem
                color: "#000000"
            }
        },
        State {
            name: "down"
            when: control.down
            PropertyChanges {
                target: textItem
                color: "#ffffff"
            }

            PropertyChanges {
                target: buttonBackground
                color: "#047eff"
                border.color: "#00000000"
            }
        },
        State {
            name: "hover"
            when: control.hovered && !control.down

            PropertyChanges {
                target: gradientStop
                color: "#8ebae7"
            }
        }
    ]
}
