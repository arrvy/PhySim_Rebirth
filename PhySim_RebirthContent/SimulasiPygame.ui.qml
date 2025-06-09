import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import PhySim_Rebirth

// Import your custom module

// Assuming this is the basic structure of your SimulasiPygame.ui.qml.
// You might need to adapt this to the actual structure of your file.
Rectangle {
    id: simulasiPygameRoot
    width: 1024
    height: 768
    color: "#F0F0F0" // Example background color

    // Main column layout (or whatever layout you are using)
    ColumnLayout {
        anchors.fill: parent
        spacing: 20
        //padding: 20

        // Title or other UI elements
        Label {
            text: "Pygame Physics Simulation"
            font.pixelSize: 32
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
        }

        // This is the black Rectangle you mentioned for placing the simulation
        Rectangle {
            id: simulationContainer
            // Assuming dimensions suitable for the intended simulation area
            Layout.preferredWidth: parent.width * 0.8
            Layout.preferredHeight: parent.height * 0.6
            Layout.alignment: Qt.AlignCenter
            color: "black" // The black background color you mentioned
            radius: 10 // Rounded corners for aesthetics

            // Integrate PygameSimulationView inside this Rectangle
            PygameSimulationView {
                // Fill the entire area of simulationContainer
                anchors.fill: parent
                // Adjust width and height to match the container
                width: parent.width
                height: parent.height
            }
        }

        // Back button or other controls
        Button {
            text: "Back to Menu"
            Layout.alignment: Qt.AlignCenter
            width: 200
            height: 50
            font.pixelSize: 18
        }
    }
}
