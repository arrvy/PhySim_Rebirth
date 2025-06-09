# PhySim_Rebirth/Python/simulasi_fisika.py
import pygame

# Kelas dasar untuk semua simulasi, agar struktur rapi
class BaseSimulasi:
    def __init__(self, width, height):
        if not pygame.get_init():
            pygame.init()
        self.width, self.height = width, height
        self.surface = pygame.Surface((width, height))
        self.clock = pygame.time.Clock()

    def update(self):
        raise NotImplementedError

    def draw(self) -> pygame.Surface:
        raise NotImplementedError

# Contoh Simulasi 1: Bola Memantul
class SimulasiBolaMemantul(BaseSimulasi):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ball_pos, self.ball_vel, self.ball_radius = [width//2, height//2], [4,3], 25
        self.background_color, self.ball_color = (10,20,30), (100,200,255)

    def update(self):
        self.ball_pos[0] += self.ball_vel[0]
        self.ball_pos[1] += self.ball_vel[1]
        if not self.ball_radius < self.ball_pos[0] < self.width - self.ball_radius:
            self.ball_vel[0] *= -1
        if not self.ball_radius < self.ball_pos[1] < self.height - self.ball_radius:
            self.ball_vel[1] *= -1
        self.clock.tick(60)

    def draw(self):
        self.surface.fill(self.background_color)
        pygame.draw.circle(self.surface, self.ball_color, self.ball_pos, self.ball_radius)
        return self.surface

# === CONTOH PENAMBAHAN SIMULASI BARU ===
# Contoh Simulasi 2: Gerak Jatuh Bebas (GJB)
class SimulasiGJB(BaseSimulasi):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.box_pos = [width // 2, 20]
        self.box_vel_y = 0
        self.gravity = 0.5  # Percepatan gravitasi
        self.background_color = (30, 10, 20)
        self.box_color = (255, 200, 100)

    def update(self):
        # Terapkan gravitasi ke kecepatan vertikal
        self.box_vel_y += self.gravity
        # Perbarui posisi Y
        self.box_pos[1] += self.box_vel_y

        # Berhenti jika menyentuh dasar layar
        if self.box_pos[1] >= self.height - 20:
            self.box_pos[1] = self.height - 20
            self.box_vel_y = 0

        self.clock.tick(60)

    def draw(self):
        self.surface.fill(self.background_color)
        # Gambar kotak sebagai objek yang jatuh
        pygame.draw.rect(self.surface, self.box_color, (self.box_pos[0] - 20, self.box_pos[1] - 20, 40, 40))
        return self.surface


# Pabrik (Factory) untuk memilih simulasi
# Daftarkan simulasi baru Anda di sini dengan ID unik
SIMULASI_TERSEDIA = {
    "bola_memantul": SimulasiBolaMemantul,
    "gjb_level_1": SimulasiGJB, # <- Tambahkan simulasi baru di sini
}

def get_simulasi(simulasi_id, width, height):
    """Membuat instance kelas simulasi berdasarkan ID."""
    cls = SIMULASI_TERSEDIA.get(simulasi_id)
    if cls:
        return cls(width, height)
    print(f"Peringatan: Simulasi ID '{simulasi_id}' tidak ditemukan.")
    return None
