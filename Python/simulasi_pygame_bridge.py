import sys
import pygame
from PySide6.QtCore import QObject, Signal, Slot, Property, QTimer
from PySide6.QtGui import QImage, QPixmap

# Penting: Karena direktori 'Python' ditambahkan ke sys.path di main.py,
# kita bisa menggunakan impor absolut untuk modul di dalamnya.
# Pastikan file ini bernama 'glbb_simulation.py' di folder yang sama.
from glbb_simulation import GLBBSimulation

class PygameQmlBridge(QObject):
    """
    Kelas ini bertindak sebagai jembatan antara simulasi Pygame dan UI QML.
    Ini mengelola siklus Pygame, merender frame, dan mengonversinya menjadi QImage
    yang dapat ditampilkan di QML.
    """
    # Signal yang akan dipancarkan setiap kali frame Pygame baru siap
    pygameImageChanged = Signal()

    def __init__(self, width=800, height=600, parent=None):
        """
        Inisialisasi bridge Pygame.

        Args:
            width (int): Lebar yang diinginkan untuk permukaan Pygame.
            height (int): Tinggi yang diinginkan untuk permukaan Pygame.
            parent (QObject, optional): Objek induk untuk QObject ini.
        """
        super().__init__(parent)
        self._width = width
        self._height = height
        self._pygame_image = QImage()  # Ini akan menampung frame Pygame yang dikonversi

        # Inisialisasi Pygame dalam mode headless (tanpa membuat jendela display)
        pygame.init()
        pygame.font.init() # Pastikan modul font diinisialisasi untuk rendering teks

        # Buat permukaan Pygame untuk menggambar.
        # Menggunakan SRCALPHA memungkinkan transparansi.
        self.pygame_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        # Inisialisasi simulasi GLBB dengan dimensi yang diberikan
        self.simulation = GLBBSimulation(width, height)

        # QTimer untuk memicu pembaruan Pygame dan rendering ke QImage secara berkala
        self.timer = QTimer(self)
        self.timer.setInterval(16)  # Sekitar 60 FPS (1000 ms / 60 = 16.67 ms)
        self.timer.timeout.connect(self._update_pygame_frame)
        self.timer.start() # Mulai timer secara otomatis saat objek dibuat

    @Property(QImage, notify=pygameImageChanged)
    def pygameImage(self):
        """
        Properti QML yang mengekspos QImage dari frame Pygame.
        """
        return self._pygame_image

    @Slot()
    def resetSimulation(self):
        """
        Slot QML yang dapat dipanggil dari QML untuk mereset simulasi Pygame.
        """
        self.simulation.reset_simulation()
        print("Simulasi Pygame direset!")

    @Slot(float, float)
    def handleMouseClick(self, x, y):
        """
        Slot QML untuk menangani klik mouse dari QML dan meneruskannya ke simulasi Pygame
        (jika simulasi Anda memerlukan interaksi mouse).
        Untuk simulasi GLBB sederhana ini, ini hanyalah contoh.
        """
        # Anda dapat mengubah koordinat (x, y) ini menjadi event Pygame jika diperlukan
        # Misalnya: pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (int(x), int(y))}))
        print(f"Klik mouse di bridge Pygame: ({x}, {y})")
        # Di sini Anda bisa menambahkan logika untuk berinteraksi dengan simulasi Pygame
        # berdasarkan posisi klik.

    def _update_pygame_frame(self):
        """
        Metode internal yang dipanggil oleh QTimer untuk memperbarui simulasi Pygame,
        merendernya, dan mengonversi permukaan menjadi QImage.
        """
        # Perbarui keadaan simulasi
        self.simulation.update_simulation()

        # Render simulasi ke permukaan Pygame
        self.simulation.render(self.pygame_surface)

        # Konversi permukaan Pygame ke QImage
        # Pygame biasanya menggunakan format BGRA secara internal, jadi kita gunakan ARGB32
        # get_pitch() memberikan jumlah byte per baris, yang penting untuk konversi yang benar
        raw_data = self.pygame_surface.get_view('1') # Dapatkan tampilan byte dari permukaan
        self._pygame_image = QImage(raw_data, self._width, self._height,
                                    self.pygame_surface.get_pitch(),  # Byte per baris (pitch)
                                    QImage.Format_ARGB32).copy()  # Pastikan salinan dibuat

        self.pygameImageChanged.emit() # Pancarkan sinyal untuk memberi tahu QML bahwa gambar telah berubah

    def __del__(self):
        """
        Destruktor untuk membersihkan sumber daya Pygame saat objek bridge dihancurkan.
        """
        # Cek jika timer masih merupakan instance QObject dan belum dihancurkan.
        # Ini untuk menghindari RuntimeError: Internal C++ object already deleted.
        if self.timer and not self.timer.parent() is None: # Cek keberadaan objek dan parent (indikator objek C++ masih hidup)
            try:
                self.timer.stop() # Hentikan timer
            except RuntimeError as e:
                # Tangani kasus di mana objek C++ sudah dihapus oleh Qt
                print(f"Peringatan: Tidak dapat menghentikan QTimer di __del__: {e}")
        pygame.quit() # Hentikan Pygame
        print("Pygame Bridge dihancurkan.")

