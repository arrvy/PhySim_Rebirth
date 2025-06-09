import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtQuickControls2 import QQuickStyle # Add this to set the style
from autogen.settings import url, import_paths # Import automatic settings from Qt Design Studio

# Important: Add the 'Python' directory to sys.path for absolute imports to work
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

# Now import PygameSimulationManager and PygameImageProvider from simulasi_pygame_bridge
from simulasi_pygame_bridge import PygameSimulationManager, PygameImageProvider

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    # SET APPLICATION STYLE TO ADDRESS QML CONTROL CUSTOMIZATION WARNINGS
    # Options: "Basic", "Fusion", "Material", "Universal", "Imagine" (if available), etc.
    #QQuickStyle.setStyle("Fusion") 

    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent # This is the project root (PhySim_Rebirth)

    # Add the project root directory as the main import path.
    # This will allow the QML engine to find qmldir in PhySim_Rebirth/qmldir
    # and other modules.
    engine.addImportPath(os.fspath(app_dir))

    # Add additional import paths from automatic settings (e.g., for QtQuick.Controls)
    # This is important for non-module components or other modules that might exist.
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    # --- Pygame Bridge Integration (Manager and Provider) ---
    # Initialize the Pygame simulation manager
    pygame_manager = PygameSimulationManager(width=800, height=600)
    # Expose the manager to the QML context, so it can be accessed in QML as 'pygameManager'
    # This is needed to call slots like resetSimulation or handleMouseClick.
    engine.rootContext().setContextProperty("pygameManager", pygame_manager)

    # Initialize the image provider and register it with the QML engine.
    # "pygameprovider" is the unique ID that will be used in QML (e.g., image://pygameprovider/sim_id).
    # Important: The provider object must stay alive as long as the engine is active.
    pygame_image_provider = PygameImageProvider(pygame_manager)
    engine.addImageProvider("pygameprovider", pygame_image_provider)

    # --- End Pygame Bridge Integration ---

    # Load your main QML file using the URL from automatic settings.
    # Assume 'url' in settings.py is a relative path from 'app_dir',
    # e.g., "PhySim_RebirthContent/App.qml".
    engine.load(os.fspath(app_dir / url))

    if not engine.rootObjects():
        print("\nFATAL: Failed to load QML. Check the output above for specific errors.")
        sys.exit(-1)

    sys.exit(app.exec())

