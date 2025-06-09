import QtQuick 2.15 // Adjust your QtQuick version if different
import QtQuick.Controls 2.15
import QtQuick.Layouts
import PhySim_Rebirth // Important: Ensure your module is imported

// This is the QML component that will display the Pygame simulation
Rectangle {
    id: pygameView
    // Default width and height, can be overridden by parent
    width: 800
    height: 600
    color: "lightgray" // Background color for this component, can be changed to "transparent" if Pygame image has alpha

    // Counter property to force the Image element to reload
    property int imageUpdateCounter: 0

    // Reference to the Python PygameSimulationManager object
    // This object is exposed as 'pygameManager' from main.py
    property var manager: pygameManager // Connects to the Python manager object

    // Image element to display the Pygame surface
    Image {
        id: pygameDisplayImage
        anchors.fill: parent // Fill the entire parent area
        fillMode: Image.PreserveAspectFit // Maintain aspect ratio when scaling
        smooth: true // For smoother image scaling

        // Use the counter as part of the URL to force a reload
        source: "image://pygameprovider/sim_id?" + pygameView.imageUpdateCounter
        // Debugging: Coba tambahkan placeholder jika gagal
        // onStatusChanged: {
        //     if (status === Image.Error) {
        //         console.log("Image failed to load: " + errorString);
        //     }
        // }
    }

    // Connections to react to signals from the Python manager
    Connections {
        target: manager
        function onSimulationFrameReady() {
            // When a new frame is ready, increment the counter to force the Image element to reload
            pygameView.imageUpdateCounter++;
            // Debugging:
            // console.log("Simulation frame ready. Counter: " + pygameView.imageUpdateCounter);
        }
    }

    // Example button to interact with the simulation (e.g., reset)
    Button {
        id: resetButton
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Reset Simulation"
        width: 150
        height: 40
        y: -20 // Margin from bottom
        onClicked: {
            manager.resetSimulation() // Call Python slot on the manager
        }
    }

    // Optional: MouseArea to pass events to Pygame (if simulation is interactive)
    MouseArea {
        anchors.fill: parent
        onClicked: (mouse) => {
            // Pass mouse click coordinates to the Python manager
            // You might need to adjust coordinates based on fillMode and Image scaling
            manager.handleMouseClick(mouse.x, mouse.y)
        }
    }

    // Ensure the component has active focus for event processing (if you have specific keyboard/mouse input)
    Component.onCompleted: {
        pygameView.forceActiveFocus();
    }
}
