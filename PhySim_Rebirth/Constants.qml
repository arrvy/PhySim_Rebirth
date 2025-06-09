pragma Singleton
import QtQuick
import QtQuick.Studio.Application
import QtQuick.Window


QtObject {
    //readonly property int width: Screen.width
    //readonly property int height: Screen.height

    readonly property int width: 1920
    readonly property int height: 1080

    readonly property real scaleFactor: Screen.pixelDensity / 2.0

    property string relativeFontDirectory: "fonts"

    /* Edit this comment to add your custom font */
    readonly property font font: Qt.font({
                                             family: Qt.application.font.family,
                                             pixelSize: Qt.application.font.pixelSize * scaleFactor
                                         })
    readonly property font largeFont: Qt.font({
                                                  family: Qt.application.font.family,
                                                  pixelSize: Qt.application.font.pixelSize * 1.6
                                              })

    readonly property color backgroundColor: "#EAEAEA"


    property StudioApplication application: StudioApplication {
        fontPath: Qt.resolvedUrl("../PhySim_RebirthContent/" + relativeFontDirectory)
    }
}
