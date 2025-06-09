# PhySim_Rebirth/Python/SimulationItem.py
import pygame
from PySide6.QtCore import QTimer, Slot, Property, Signal
from PySide6.QtGui import QPainter, QImage
from PySide6.QtQuick import QQuickPaintedItem
from simulasi_fisika import get_simulasi

class SimulationItem(QQuickPaintedItem):
    simulationIdChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._simulation_instance = None
        self._simulation_id = ""
        self.timer = QTimer(self)
        self.timer.setInterval(16)  # ~60 FPS
        self.timer.timeout.connect(self.tick)
        self.timer.start()

    def _load_simulation(self):
        self._simulation_instance = None
        if self._simulation_id and self.width() > 0 and self.height() > 0:
            w, h = int(self.width()), int(self.height())
            self._simulation_instance = get_simulasi(self._simulation_id, w, h)

    @Property(str, notify=simulationIdChanged)
    def simulationId(self):
        return self._simulation_id

    @simulationId.setter
    def simulationId(self, new_id):
        if self._simulation_id != new_id:
            self._simulation_id = new_id
            self._load_simulation()
            self.simulationIdChanged.emit()

    @Slot()
    def tick(self):
        if not self.isVisible(): return
        if self._simulation_instance is None and self._simulation_id:
            self._load_simulation()
        if self._simulation_instance:
            self._simulation_instance.update()
            self.update() # Memicu pemanggilan paint()

    def paint(self, painter: QPainter):
        if self._simulation_instance:
            pygame_surface = self._simulation_instance.draw()
            w, h = pygame_surface.get_width(), pygame_surface.get_height()
            image = QImage(pygame_surface.get_buffer().raw, w, h, QImage.Format_RGB32)
            painter.drawImage(0, 0, image)
        else:
            painter.fillRect(self.boundingRect().toRect(), (25, 25, 25))
