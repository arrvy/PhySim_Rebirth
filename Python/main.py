import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
# Tambahkan QUrl untuk pemuatan file yang lebih robust
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import QUrl

# Impor kelas jembatan kita. Pastikan file ini berada di folder yang sama.
from SimulationItem import SimulationItem
from autogen.settings import url, import_paths

if __name__ == '__main__':
    os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Basic'
    os.environ['QT_LOGGING_RULES'] = 'qml.*=true'

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # DAFTARKAN KOMPONEN PYTHON SEBELUM MELAKUKAN APAPUN
    qmlRegisterType(SimulationItem, "PhySim", 1, 0, "SimulationCanvas")

    # Ambil path direktori utama proyek
    app_dir = Path(__file__).parent.parent

    # Tambahkan path-path yang diperlukan oleh QML engine
    engine.addImportPath(os.fspath(app_dir))
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    # --- PERUBAHAN UTAMA DI SINI ---
    # Muat file QML utama menggunakan QUrl. Ini lebih andal dalam
    # menangani path relatif antar file QML (seperti App.qml ke App_State.qml)
    main_qml_file = app_dir / url
    engine.load(QUrl.fromLocalFile(os.fspath(main_qml_file)))

    # Periksa apakah pemuatan berhasil
    if not engine.rootObjects():
        print("FATAL: Gagal memuat QML. Periksa output di atas untuk error spesifik.")
        sys.exit(-1)

    sys.exit(app.exec())
