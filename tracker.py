import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chiptune Tracker")

# Font for displaying notes
font = pygame.font.Font(None, 36)

# Mapping of keys to notes and colors for each platform
platforms = {
    "NES_FDS": {
        "modes": {
            "NES": {
                "keys": [pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n],
                "notes": ["C", "D", "E", "F", "G", "A"],
                "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
            },
            "FDS": {
                "keys": [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h],
                "notes": ["C", "D", "E", "F", "G", "A"],
                "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
            },
            "VRC7": {
                "keys": [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y],
                "notes": ["C", "D", "E", "F", "G", "A"],
                "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
            },
            "VRC6": {
                "keys": [pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET],
                "notes": ["C", "D", "E", "F", "G", "A"],
                "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
            },
            "MMC5": {
                "keys": [pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_QUOTE, pygame.K_COMMA],
                "notes": ["C", "D", "E", "F", "G", "A"],
                "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
            },
        },
    },
    "Amiga": {
        "keys": [pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET],
        "notes": ["C", "D", "E", "F", "G", "A"],
        "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
    },
    "Sega": {
        "keys": [pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_QUOTE, pygame.K_COMMA],
        "notes": ["C", "D", "E", "F", "G", "A"],
        "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
    },
    "GameBoy": {
        "keys": [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6],
        "notes": ["C", "D", "E", "F", "G", "A"],
        "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
    },
    "PC_Engine": {
        "keys": [pygame.K_v, pygame.K_b, pygame.K_n, pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD],
        "notes": ["C", "D", "E", "F", "G", "A"],
        "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
    },
    "AY-3-8930": {
        "keys": [pygame.K_f1, pygame.K_f2, pygame.K_f3, pygame.K_f4, pygame.K_f5, pygame.K_f6],
        "notes": ["C", "D", "E", "F", "G", "A"],
        "colors": [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE],
    },
}

# Pattern Editor
pattern = [
    ["C", "D", "E", "F", "G", "A"],
    ["D", "E", "F", "G", "A", "B"],
    ["E", "F", "G", "A", "B", "C"],
]

pattern_row = 0

# Instrument Editor
instruments = ["Instrument 1", "Instrument 2", "Instrument 3"]
current_instrument = 0

# Main loop
def main():
    running = True
    pressed_keys = set()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_key_down(event.key)
            elif event.type == pygame.KEYUP:
                handle_key_up(event.key)
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Draw design elements
        draw_design()
        
        # Draw the pattern editor
        draw_pattern_editor()
        
        # Draw the instrument editor
        draw_instrument_editor()
        
        # Draw the notes being played
        draw_notes(pressed_keys)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

# Function to handle key presses
def handle_key_down(key):
    global pattern_row, current_instrument
    if key == pygame.K_UP:
        pattern_row = max(0, pattern_row - 1)
    elif key == pygame.K_DOWN:
        pattern_row = min(len(pattern) - 1, pattern_row + 1)
    elif key == pygame.K_LEFT:
        current_instrument = max(0, current_instrument - 1)
    elif key == pygame.K_RIGHT:
        current_instrument = min(len(instruments) - 1, current_instrument + 1)

# Function to draw design elements
def draw_design():
    # Draw pattern editor box
    pygame.draw.rect(screen, LIGHT_GRAY, (10, 10, 380, 580))
    pygame.draw.rect(screen, GRAY, (10, 10, 380, 40))
    
    # Draw instrument editor box
    pygame.draw.rect(screen, LIGHT_GRAY, (400, 10, 380, 180))
    pygame.draw.rect(screen, GRAY, (400, 10, 380, 40))

# Function to draw the pattern editor
def draw_pattern_editor():
    y = 60
    for row, pattern_row_data in enumerate(pattern):
        text = " ".join(pattern_row_data)
        if row == pattern_row:
            text = f"[{text}]"
        rendered_text = font.render(text, True, BLACK)
        screen.blit(rendered_text, (20, y))
        y += 40

# Function to draw the instrument editor
def draw_instrument_editor():
    text = "Instruments: "
    for i, instrument in enumerate(instruments):
        if i == current_instrument:
            text += f"[{instrument}] "
        else:
            text += f"{instrument} "
    rendered_text = font.render(text, True, BLACK)
    screen.blit(rendered_text, (410, 20))

# Function to draw notes on the screen based on pressed keys
def draw_notes(keys_pressed):
    y = 250
    for platform, data in platforms.items():
        if platform == "NES_FDS":
            for mode, mode_data in data["modes"].items():
                notes = [mode_data["notes"][i] for i, k in enumerate(mode_data["keys"]) if k in keys_pressed]
                colors = [mode_data["colors"][i] for i, k in enumerate(mode_data["keys"]) if k in keys_pressed]
                text = f"{mode}: {' - '.join(notes)}"
                rendered_text = font.render(text, True, BLACK)
                screen.blit(rendered_text, (400, y))
                y += 40
                for color in colors:
                    pygame.draw.circle(screen, color, (750, y), 15)
                    y += 30
        else:
            notes = [data["notes"][i] for i, k in enumerate(data["keys"]) if k in keys_pressed]
            colors = [data["colors"][i] for i, k in enumerate(data["keys"]) if k in keys_pressed]
            text = f"{platform}: {' - '.join(notes)}"
            rendered_text = font.render(text, True, BLACK)
            screen.blit(rendered_text, (400, y))
            y += 40
            for color in colors:
                pygame.draw.circle(screen, color, (750, y), 15)
                y += 30

if __name__ == "__main__":
    main()