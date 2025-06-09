import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import QUrl

# Impor kelas jembatan kita
from SimulationItem import SimulationItem

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Daftarkan komponen Python kita SEBELUM QML engine dimuat.
    # Ini membuat "PhySim.SimulationCanvas" tersedia di QML.
    qmlRegisterType(SimulationItem, "PhySim", 1, 0, "SimulationCanvas")

    # Tentukan path absolut ke folder konten QML Anda.
    content_dir = Path(__file__).parent.parent / "PhySim_RebirthContent"

    # Setel basis URL untuk QML engine. Ini akan memperbaiki error 'Type unavailable'.
    engine.setBaseUrl(QUrl.fromLocalFile(os.fspath(content_dir)))

    # Sekarang, muat file App.qml.
    main_qml_file = content_dir / "App.qml"
    engine.load(os.fspath(main_qml_file))

    if not engine.rootObjects():
        print("\nFATAL: Gagal memuat QML. Periksa output di atas untuk error spesifik.")
        sys.exit(-1)

    sys.exit(app.exec())
