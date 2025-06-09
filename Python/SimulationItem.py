# PhySim_Rebirth/Python/SimulationItem.py
# Kelas ini adalah jembatan antara Qt/QML dan Pygame.

import pygame
from PySide6.QtCore import QTimer, Slot, Property, QSize
from PySide6.QtGui import QPainter, QImage
from PySide6.QtQuick import QQuickPaintedItem

# Impor kelas simulasi kita
from simulasi_fisika import SimulasiFisika

class SimulationItem(QQuickPaintedItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._simulation_instance = None

        # Timer Qt akan menjalankan game loop kita agar tidak memblokir UI
        self.timer = QTimer(self)
        self.timer.setInterval(16)  # Target ~60 FPS (1000ms / 16ms)
        self.timer.timeout.connect(self.tick)
        self.timer.start()

    @Slot()
    def tick(self):
        """Fungsi yang dipanggil oleh QTimer secara berkala."""
        if not self.isVisible() or self.width() <= 0 or self.height() <= 0:
            return

        # Inisialisasi simulasi HANYA setelah item memiliki ukuran yang valid
        if self._simulation_instance is None:
            w, h = int(self.width()), int(self.height())
            if w > 0 and h > 0:
                self._simulation_instance = SimulasiFisika(w, h)

        if self._simulation_instance:
            # 1. Update logika game
            self._simulation_instance.update()
            # 2. Minta QML untuk menjadwalkan penggambaran ulang (memanggil paint())
            self.update()

    def paint(self, painter: QPainter):
        """Fungsi ini dipanggil oleh Qt ketika item perlu digambar."""
        if self._simulation_instance:
            # Dapatkan pygame surface yang sudah digambar
            pygame_surface = self._simulation_instance.draw()
            
            # Konversi pygame.Surface ke QImage yang bisa dibaca Qt
            w = pygame_surface.get_width()
            h = pygame_surface.get_height()
            
            # Format harus cocok. Pygame surface biasanya 32-bit.
            image = QImage(pygame_surface.get_buffer().raw, w, h, QImage.Format_RGB32)

            # Gambar QImage ke canvas QML menggunakan QPainter
            painter.drawImage(0, 0, image)
        else:
            # Tampilkan sesuatu jika simulasi belum siap
            painter.fillRect(self.boundingRect().toRect(), (25, 25, 25))
