import pygame
import math

class GLBBSimulation:
    """
    This class manages the physics simulation of Uniformly Accelerated Motion (GLBB).
    The simulation can draw onto a provided Pygame surface.
    """
    def __init__(self, width, height, initial_state=None):
        """
        Initializes the simulation with specific dimensions.

        Args:
            width (int): Width of the simulation area.
            height (int): Height of the simulation area.
            initial_state (dict, optional): Initial state to reset the simulation to.
                                            Defaults to None, which will use the default initial state.
        """
        self.width = width
        self.height = height
        self.gravity = 9.81  # Gravity in m/s^2
        self.time_step = 0.05  # Time step size for each update
        self.sim_time = 0.0  # Current simulation time

        # Simulated object properties
        self.obj_radius = 10
        self.obj_color = (255, 0, 0)  # Red
        self.pos_x = 50
        self.pos_y = height - 50 - self.obj_radius  # Position above ground
        self.vel_x = 50  # Initial X velocity
        self.vel_y = -100 # Initial Y velocity (negative because upward on Pygame y-axis)

        # Store initial state for reset function
        self.initial_state = {
            'pos_x': self.pos_x,
            'pos_y': self.pos_y,
            'vel_x': self.vel_x,
            'vel_y': self.vel_y,
            'sim_time': self.sim_time
        }
        # If initial state is provided, use it
        if initial_state:
            self.set_state(initial_state)

        # Graph properties (for displaying data within the simulation)
        self.graph_x_min = 0
        self.graph_x_max = width
        self.graph_y_min = 0
        self.graph_y_max = 200 # Height of the graph area
        self.graph_data = [] # Data for the graph (time, Y position)

        # Color definitions
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)

    def set_state(self, state):
        """
        Sets the simulation state to the given values.
        """
        self.pos_x = state['pos_x']
        self.pos_y = state['pos_y']
        self.vel_x = state['vel_x']
        self.vel_y = state['vel_y']
        self.sim_time = state['sim_time']
        self.graph_data = []  # Clear graph data on reset

    def reset_simulation(self):
        """
        Resets the simulation to its initial state.
        """
        self.set_state(self.initial_state)

    def update_simulation(self):
        """
        Updates the simulation state based on the time step.
        """
        # Update Y velocity due to gravity
        self.vel_y += self.gravity * self.time_step
        # Update position based on velocity
        self.pos_x += self.vel_x * self.time_step
        self.pos_y += self.vel_y * self.time_step

        # Collision handling with ground (bottom)
        if self.pos_y > self.height - self.obj_radius:
            self.pos_y = self.height - self.obj_radius
            self.vel_y *= -0.8  # Bounce with some energy loss

        # Collision handling with walls (left/right)
        if self.pos_x < self.obj_radius:
            self.pos_x = self.obj_radius
            self.vel_x *= -0.8
        elif self.pos_x > self.width - self.obj_radius:
            self.pos_x = self.width - self.obj_radius
            self.vel_x *= -0.8

        self.sim_time += self.time_step # Advance simulation time
        # Store time and Y position data for graph
        self.graph_data.append((self.sim_time, self.pos_y))

    def draw_object(self, surface):
        """
        Draws the simulated object onto the given Pygame surface.
        """
        pygame.draw.circle(surface, self.obj_color, (int(self.pos_x), int(self.pos_y)), self.obj_radius)

    def draw_wall(self, surface):
        """
        Draws the wall (ground) onto the given Pygame surface.
        """
        # Draw ground line
        pygame.draw.line(surface, self.BLACK, (0, self.height - self.obj_radius), (self.width, self.height - self.obj_radius), 3)

    def draw_vector(self, surface, start_pos, vector, color, scale=1):
        """
        Draws a velocity vector onto the given Pygame surface.
        """
        end_pos_x = start_pos[0] + vector[0] * scale
        end_pos_y = start_pos[1] + vector[1] * scale
        pygame.draw.line(surface, color, start_pos, (int(end_pos_x), int(end_pos_y)), 2)
        # Draw arrowhead
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
        Draws the Y position vs. time graph onto the given Pygame surface.
        """
        # Draw graph background and axes
        pygame.draw.rect(surface, self.WHITE, (self.graph_x_min, self.graph_y_min, self.graph_x_max, self.graph_y_max))
        pygame.draw.line(surface, self.BLACK, (self.graph_x_min, self.graph_y_min + self.graph_y_max), (self.graph_x_max, self.graph_y_min + self.graph_y_max), 2) # X-axis
        pygame.draw.line(surface, self.BLACK, (self.graph_x_min, self.graph_y_min), (self.graph_x_min, self.graph_y_min + self.graph_y_max), 2) # Y-axis

        if len(self.graph_data) > 1:
            points = []
            for t, y_pos in self.graph_data:
                # Scale time to graph x-axis
                # Assume 10 seconds is full graph width
                graph_x = self.graph_x_min + (t / 10.0) * self.graph_x_max
                # Scale y position to graph y-axis (invert y for Pygame coordinates)
                graph_y = self.graph_y_min + self.graph_y_max - (y_pos / self.height) * self.graph_y_max
                points.append((int(graph_x), int(graph_y)))
            pygame.draw.lines(surface, self.BLUE, False, points, 2)

    def draw_info(self, surface, font):
        """
        Draws simulation information (time, position, velocity) onto the surface.
        """
        # Render info text
        text_time = font.render(f"Time: {self.sim_time:.2f} s", True, self.BLACK)
        text_pos_x = font.render(f"Pos X: {self.pos_x:.2f} m", True, self.BLACK)
        text_pos_y = font.render(f"Pos Y: {self.height - self.pos_y:.2f} m", True, self.BLACK) # Invert Y for display
        text_vel_x = font.render(f"Vel X: {self.vel_x:.2f} m/s", True, self.BLACK)
        text_vel_y = font.render(f"Vel Y: {-self.vel_y:.2f} m/s", True, self.BLACK) # Invert Vel Y for display

        # Position the text on the surface
        surface.blit(text_time, (10, 10))
        surface.blit(text_pos_x, (10, 40))
        surface.blit(text_pos_y, (10, 70))
        surface.blit(text_vel_x, (10, 100))
        surface.blit(text_vel_y, (10, 130))

    def render(self, surface):
        """
        Main method to render the entire simulation to the given Pygame surface.
        """
        surface.fill(self.WHITE)  # Clear surface with white

        # Draw simulation elements
        self.draw_wall(surface)
        self.draw_object(surface)

        # Draw velocity vectors
        self.draw_vector(surface, (int(self.pos_x), int(self.pos_y)), (self.vel_x, 0), self.GREEN, scale=0.5)  # X velocity vector
        self.draw_vector(surface, (int(self.pos_x), int(self.pos_y)), (0, self.vel_y), self.YELLOW, scale=0.5) # Y velocity vector
        self.draw_vector(surface, (int(self.pos_x), int(self.pos_y)), (self.vel_x, self.vel_y), self.RED, scale=0.5) # Total velocity vector

        # Draw graph
        self.draw_graph(surface)

        # Draw information
        # Ensure font is initialized before use
        # In the bridge context, font will be initialized in the bridge itself
        font = pygame.font.SysFont("Arial", 20)
        self.draw_info(surface, font)

