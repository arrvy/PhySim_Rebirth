import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from autogen.settings import url, import_paths # Mengimpor pengaturan otomatis dari Qt Design Studio

# Penting: Tambahkan direktori 'Python' ke sys.path agar impor absolut berfungsi
# Ini mengatasi "ImportError: attempted relative import with no known parent package"
# Pastikan main.py, simulasi_pygame_bridge.py, dan glbb_simulation.py berada di folder ini.
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

# Sekarang impor PygameQmlBridge sebagai impor absolut
# karena direktori 'Python' (current_dir) sudah ada di sys.path
from simulasi_pygame_bridge import PygameQmlBridge

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent # Ini adalah root proyek (PhySim_Rebirth)

    # Hanya tambahkan jalur impor yang spesifik dari settings.py.
    # Menghapus `engine.addImportPath(os.fspath(app_dir))` secara langsung
    # untuk mencegah ambiguitas karena modul 'PhySim_Rebirth' sudah didefinisikan
    # di dalam 'PhySim_RebirthContent' (tempat qmldir berada).
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    # --- Integrasi Pygame Bridge ---
    # Atur lebar dan tinggi sesuai keinginan Anda untuk simulasi Pygame
    # Ini harus cocok dengan ukuran Rectangle di QML tempat Anda menampilkan simulasi
    pygame_bridge = PygameQmlBridge(width=800, height=600)
    # Mengekspos objek bridge ke konteks QML, sehingga dapat diakses di QML sebagai 'pygameBridge'
    engine.rootContext().setContextProperty("pygameBridge", pygame_bridge)
    # --- Akhir Integrasi Pygame Bridge ---

    # Muat file QML utama Anda menggunakan URL dari pengaturan otomatis (misalnya "PhySim_RebirthContent/App.qml")
    engine.load(os.fspath(app_dir / url))

    if not engine.rootObjects():
        print("\nFATAL: Gagal memuat QML. Periksa output di atas untuk error spesifik.")
        sys.exit(-1)

    sys.exit(app.exec())

