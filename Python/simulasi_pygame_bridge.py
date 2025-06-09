import sys
import pygame
from PySide6.QtCore import QObject, Signal, Slot, QTimer, QSize
from PySide6.QtGui import QImage, QPixmap, qRgb
from PySide6.QtQuick import QQuickImageProvider

# Import the GLBB simulation class
from glbb_simulation import GLBBSimulation

# Class to manage the Pygame simulation and produce QImages
class PygameSimulationManager(QObject):
    """
    Manages the Pygame simulation lifecycle, updates frames, and provides them as a QImage.
    This is the "backend" that produces the images to be picked up by the ImageProvider.
    """
    simulationFrameReady = Signal()

    def __init__(self, width=800, height=600, parent=None):
        super().__init__(parent)
        self._width = width
        self._height = height
        
        pygame.init()
        pygame.font.init()

        # Important: Ensure the Pygame surface format is compatible with QImage.
        # ARGB (Alpha, Red, Green, Blue) is a common and suitable format for SRCALPHA.
        # QImage.Format_ARGB32 is (A,R,G,B) 32-bit.
        self.pygame_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.simulation = GLBBSimulation(width, height)

        # Initialize _current_image with an empty QImage. It will be populated in _update_pygame_frame
        self._current_image = QImage() 
        print(f"DEBUG Manager: Initialized. Pygame surface size: {self._width}x{self._height}")

        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self._update_pygame_frame)
        self.timer.start()

        # Perform an initial update so the first image is available immediately
        self._update_pygame_frame()

    @Slot()
    def resetSimulation(self):
        self.simulation.reset_simulation()
        print("DEBUG Manager: Pygame simulation reset!")

    @Slot(float, float)
    def handleMouseClick(self, x, y):
        print(f"DEBUG Manager: Mouse click in simulation: ({x}, {y})")

    def _update_pygame_frame(self):
        self.simulation.update_simulation()
        self.simulation.render(self.pygame_surface)

        # DEBUGGING: Check if pygame_surface is valid before conversion
        if self.pygame_surface.get_size() != (self._width, self._height):
            print(f"ERROR Manager: Pygame surface size mismatch! Expected ({self._width}, {self._height}), got {self.pygame_surface.get_size()}")
            return # Do not proceed if surface is invalid

        # --- Critical part: Convert Pygame Surface to QImage ---
        # Get raw pixel data from the Pygame surface
        # '1' refers to a memoryview over the buffer
        byte_data = self.pygame_surface.get_view('1')
        
        # Check the pitch (bytes per line) of the Pygame surface
        pygame_pitch = self.pygame_surface.get_pitch()
        
        # Create QImage from pixel data.
        # Important: Ensure QImage format matches Pygame surface pixel format.
        # Pygame surface with SRCALPHA usually has an ARGB format.
        # QImage.Format_ARGB32 is the corresponding format (Byte Order: A,R,G,B).
        # Calling .copy() is crucial to ensure QImage owns its pixel data,
        # preventing memory lifecycle issues.
        try:
            self._current_image = QImage(byte_data, self._width, self._height,
                                          pygame_pitch, # Use pitch from Pygame surface
                                          QImage.Format_ARGB32).copy()
        except Exception as e:
            print(f"CRITICAL ERROR Manager: Failed to create QImage from Pygame surface: {e}")
            self._current_image = QImage() # Set to null image on failure
            self.simulationFrameReady.emit() # Still emit signal to avoid hang
            return


        if self._current_image.isNull():
            print("ERROR Manager: _current_image is NULL after Pygame surface conversion! This is critical.")
        elif self._current_image.width() == 0 or self._current_image.height() == 0:
            print(f"ERROR Manager: _current_image has zero dimensions after conversion! {self._current_image.width()}x{self._current_image.height()}")
        # else:
        #     print(f"DEBUG Manager: _current_image successfully updated. Size: {self._current_image.width()}x{self._current_image.height()}")

        self.simulationFrameReady.emit()

    def get_current_qimage(self):
        # print(f"DEBUG Manager: get_current_qimage called. QImage is null: {self._current_image.isNull()}")
        return self._current_image

    def __del__(self):
        if hasattr(self, 'timer') and self.timer is not None:
            try:
                if self.timer.isActive():
                    self.timer.stop()
            except RuntimeError as e:
                print(f"Warning Manager: Could not stop QTimer in __del__: {e}")
        
        if pygame.get_init():
            pygame.quit()
        print("DEBUG Manager: Pygame Simulation Manager destroyed.")


class PygameImageProvider(QQuickImageProvider):
    """
    Provides the latest QImage from PygameSimulationManager to the QML Image element.
    """
    def __init__(self, manager: PygameSimulationManager):
        super().__init__(QQuickImageProvider.ImageType.Image)
        self._manager = manager
        print("DEBUG Provider: PygameImageProvider initialized.")

    def requestImage(self, id: str, requestedSize: QSize, imageType: int) -> (QImage, QSize):
        current_image = self._manager.get_current_qimage()
        if not current_image.isNull() and current_image.width() > 0 and current_image.height() > 0:
            # print(f"DEBUG Provider: Requested '{id}'. Returning valid QImage. Size: {current_image.size()}")
            return current_image, current_image.size()
        else:
            print("ERROR Provider: QQuickImageProvider requested image, but QImage from manager is empty or invalid. Returning default red image.")
            # Ensure requestedSize is valid before creating QImage. If not, create a 1x1 QImage.
            effective_size = requestedSize if requestedSize.isValid() and requestedSize.width() > 0 and requestedSize.height() > 0 else QSize(1,1)
            empty_image = QImage(effective_size, QImage.Format_ARGB32)
            empty_image.fill(qRgb(255, 0, 0)) # Red color for error indication
            return empty_image, effective_size

