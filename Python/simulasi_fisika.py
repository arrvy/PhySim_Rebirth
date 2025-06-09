# PhySim_Rebirth/Python/simulasi_fisika.py
# Berisi semua logika dan gambar simulasi fisika menggunakan Pygame.

import pygame

class SimulasiFisika:
    """
    Kelas ini mengelola state dan rendering dari simulasi Pygame.
    PENTING: Kelas ini tidak membuat window Pygame sendiri.
    Ia hanya menggambar pada sebuah 'pygame.Surface' internal.
    """
    def __init__(self, width, height):
        # Inisialisasi Pygame tanpa membuat window
        pygame.init()
        self.width = width
        self.height = height
        
        # Ini adalah 'kanvas' virtual kita. Semua akan digambar di sini.
        self.surface = pygame.Surface((width, height))
        
        # State simulasi (contoh: bola memantul)
        self.ball_pos = [width // 2, height // 2]
        self.ball_vel = [4, 3] # Kecepatan dalam piksel per frame
        self.ball_radius = 25
        self.background_color = (10, 20, 30) # Biru sangat gelap
        self.ball_color = (100, 200, 255) # Biru muda
        
        # Clock untuk mengontrol framerate
        self.clock = pygame.time.Clock()

    def update(self):
        """Membaharui state simulasi untuk satu frame."""
        # Pindahkan bola
        self.ball_pos[0] += self.ball_vel[0]
        self.ball_pos[1] += self.ball_vel[1]

        # Logika pantulan sederhana
        if self.ball_pos[0] <= self.ball_radius or self.ball_pos[0] >= self.width - self.ball_radius:
            self.ball_vel[0] *= -1
        if self.ball_pos[1] <= self.ball_radius or self.ball_pos[1] >= self.height - self.ball_radius:
            self.ball_vel[1] *= -1
            
        # Batasi FPS agar simulasi konsisten
        self.clock.tick(60)

    def draw(self) -> pygame.Surface:
        """Menggambar state saat ini ke surface dan mengembalikannya."""
        # Gambar latar belakang
        self.surface.fill(self.background_color)
        
        # Gambar bola
        pygame.draw.circle(self.surface, self.ball_color, self.ball_pos, self.ball_radius)
        
        return self.surface
