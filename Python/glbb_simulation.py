import pygame
import math

class GLBBSimulation:
    """
    Kelas ini mengelola logika simulasi Gerak Lurus Berubah Beraturan (GLBB).
    Simulasi dapat menggambar ke permukaan Pygame yang disediakan.
    """
    def __init__(self, width, height, initial_state=None):
        """
        Inisialisasi simulasi dengan dimensi tertentu.

        Args:
            width (int): Lebar area simulasi.
            height (int): Tinggi area simulasi.
            initial_state (dict, optional): Keadaan awal untuk mengatur ulang simulasi.
                                            Defaultnya adalah None, yang akan menggunakan keadaan awal default.
        """
        self.width = width
        self.height = height
        self.gravity = 9.81  # Gravitasi dalam m/s^2
        self.time_step = 0.05  # Ukuran langkah waktu untuk setiap pembaruan
        self.sim_time = 0.0  # Waktu simulasi saat ini

        # Properti objek yang disimulasikan
        self.obj_radius = 10
        self.obj_color = (255, 0, 0)  # Merah
        self.pos_x = 50
        self.pos_y = height - 50 - self.obj_radius  # Posisikan di atas tanah
        self.vel_x = 50  # Kecepatan awal X
        self.vel_y = -100 # Kecepatan awal Y (negatif karena ke atas di Pygame y-axis)

        # Simpan keadaan awal untuk fungsi reset
        self.initial_state = {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'vel_x': self.vel_x,
            'vel_y': self.vel_y,
            'sim_time': self.sim_time
        }
        # Jika keadaan awal disediakan, gunakan itu
        if initial_state:
            self.set_state(initial_state)

        # Properti grafik (untuk menampilkan data di dalam simulasi)
        self.graph_x_min = 0
        self.graph_x_max = width
        self.graph_y_min = 0
        self.graph_y_max = 200 # Tinggi area grafik
        self.graph_data = [] # Data untuk grafik (waktu, posisi Y)

        # Definisi warna
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)

    def set_state(self, state):
        """
        Mengatur keadaan simulasi ke nilai yang diberikan.
        """
        self.pos_x = state['pos_x']
        self.pos_y = state['pos_y']
        self.vel_x = state['vel_x']
        self.vel_y = state['vel_y']
        self.sim_time = state['sim_time']
        self.graph_data = []  # Hapus data grafik saat reset

    def reset_simulation(self):
        """
        Mengatur ulang simulasi ke keadaan awalnya.
        """
        self.set_state(self.initial_state)

    def update_simulation(self):
        """
        Memperbarui keadaan simulasi berdasarkan langkah waktu.
        """
        # Perbarui kecepatan Y karena gravitasi
        self.vel_y += self.gravity * self.time_step
        # Perbarui posisi berdasarkan kecepatan
        self.pos_x += self.vel_x * self.time_step
        self.pos_y += self.vel_y * self.time_step

        # Penanganan tabrakan dengan tanah (bawah)
        if self.pos_y > self.height - self.obj_radius:
            self.pos_y = self.height - self.obj_radius
            self.vel_y *= -0.8  # Memantul dengan sebagian kehilangan energi

        # Penanganan tabrakan dengan dinding (kiri/kanan)
        if self.pos_x < self.obj_radius:
            self.pos_x = self.obj_radius
            self.vel_x *= -0.8
        elif self.pos_x > self.width - self.obj_radius:
            self.pos_x = self.width - self.obj_radius
            self.vel_x *= -0.8

        self.sim_time += self.time_step # Majukan waktu simulasi
        # Simpan data waktu dan posisi Y untuk grafik
        self.graph_data.append((self.sim_time, self.pos_y))

    def draw_object(self, surface):
        """
        Menggambar objek simulasi ke permukaan Pygame yang diberikan.
        """
        pygame.draw.circle(surface, self.obj_color, (int(self.pos_x), int(self.pos_y)), self.obj_radius)

    def draw_wall(self, surface):
        """
        Menggambar dinding (tanah) ke permukaan Pygame yang diberikan.
        """
        # Gambar garis tanah
        pygame.draw.line(surface, self.BLACK, (0, self.height - self.obj_radius), (self.width, self.height - self.obj_radius), 3)

    def draw_vector(self, surface, start_pos, vector, color, scale=1):
        """
        Menggambar vektor kecepatan ke permukaan Pygame yang diberikan.
        """
        end_pos_x = start_pos[0] + vector[0] * scale
        end_pos_y = start_pos[1] + vector[1] * scale
        pygame.draw.line(surface, color, start_pos, (int(end_pos_x), int(end_pos_y)), 2)
        # Gambar kepala panah
        angle = math.atan2(vector[1], vector[0])
        arrow_length = 10
        pygame.draw.line(surface, color, (int(end_pos_x), int(end_pos_y)),
                         (int(end_pos_x - arrow_length * math.cos(angle - math.pi / 6)),
                          int(end_pos_y - arrow_length * math.sin(angle - math.pi / 6))), 2)
        pygame.draw.line(surface, color, (int(end_pos_x), int(end_pos_y)),
                         (int(end_pos_x - arrow_length * math.cos(angle + math.pi / 6)),
                          int(end_pos_y - arrow_length * math.sin(angle + math.pi / 6))), 2)

    def draw_graph(self, surface):
        """
        Menggambar grafik posisi Y terhadap waktu ke permukaan Pygame yang diberikan.
        """
        # Gambar latar belakang dan sumbu grafik
        pygame.draw.rect(surface, self.WHITE, (self.graph_x_min, self.graph_y_min, self.graph_x_max, self.graph_y_max))
        pygame.draw.line(surface, self.BLACK, (self.graph_x_min, self.graph_y_min + self.graph_y_max), (self.graph_x_max, self.graph_y_min + self.graph_y_max), 2) # Sumbu X
        pygame.draw.line(surface, self.BLACK, (self.graph_x_min, self.graph_y_min), (self.graph_x_min, self.graph_y_min + self.graph_y_max), 2) # Sumbu Y

        if len(self.graph_data) > 1:
            points = []
            for t, y_pos in self.graph_data:
                # Skala waktu ke sumbu x grafik
                # Asumsi 10 detik adalah lebar penuh grafik
                graph_x = self.graph_x_min + (t / 10.0) * self.graph_x_max
                # Skala posisi y ke sumbu y grafik (balik y untuk koordinat Pygame)
                graph_y = self.graph_y_min + self.graph_y_max - (y_pos / self.height) * self.graph_y_max
                points.append((int(graph_x), int(graph_y)))
            pygame.draw.lines(surface, self.BLUE, False, points, 2)

    def draw_info(self, surface, font):
        """
        Menggambar informasi simulasi (waktu, posisi, kecepatan) ke permukaan.
        """
        # Render teks informasi
        text_time = font.render(f"Waktu: {self.sim_time:.2f} s", True, self.BLACK)
        text_pos_x = font.render(f"Pos X: {self.pos_x:.2f} m", True, self.BLACK)
        text_pos_y = font.render(f"Pos Y: {self.height - self.pos_y:.2f} m", True, self.BLACK) # Balik Y untuk tampilan
        text_vel_x = font.render(f"Vel X: {self.vel_x:.2f} m/s", True, self.BLACK)
        text_vel_y = font.render(f"Vel Y: {-self.vel_y:.2f} m/s", True, self.BLACK) # Balik Vel Y untuk tampilan

        # Letakkan teks di permukaan
        surface.blit(text_time, (10, 10))
        surface.blit(text_pos_x, (10, 40))
        surface.blit(text_pos_y, (10, 70))
        surface.blit(text_vel_x, (10, 100))
        surface.blit(text_vel_y, (10, 130))

    def render(self, surface):
        """
        Metode utama untuk merender seluruh simulasi ke permukaan Pygame yang diberikan.
        """
        surface.fill(self.WHITE)  # Hapus permukaan dengan warna putih

        # Gambar elemen simulasi
        self.draw_wall(surface)
        self.draw_object(surface)

        # Gambar vektor kecepatan
        self.draw_vector(surface, (int(self.pos_x), int(self.pos_y)), (self.vel_x, 0), self.GREEN, scale=0.5)  # Vektor kecepatan X
        self.draw_vector(surface, (int(self.pos_x), int(self.pos_y)), (0, self.vel_y), self.YELLOW, scale=0.5) # Vektor kecepatan Y
        self.draw_vector(surface, (int(self.pos_x), int(self.pos_y)), (self.vel_x, self.vel_y), self.RED, scale=0.5) # Vektor kecepatan total

        # Gambar grafik
        self.draw_graph(surface)

        # Gambar informasi
        # Pastikan font diinisialisasi sebelum digunakan
        # Dalam konteks bridge, font akan diinisialisasi di bridge itu sendiri
        font = pygame.font.SysFont("Arial", 20)
        self.draw_info(surface, font)

