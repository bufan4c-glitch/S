import pygame
import sys
import random
import json
import os

# Ініціалізація
pygame.init()

# Адаптація під екран
try:
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
except:
    WIDTH, HEIGHT = 360, 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Кольори
BLACK, WHITE, GOLD = (10, 10, 10), (240, 240, 240), (255, 200, 0)
GREEN, RED, GRAY = (0, 255, 100), (255, 50, 50), (35, 35, 35)
PURPLE, BLUE = (120, 0, 200), (0, 120, 255)

def get_font(size):
    scaled = int(size * (WIDTH / 360))
    try: return pygame.font.SysFont("sans-serif", scaled, bold=True)
    except: return pygame.font.Font(None, scaled)

font_main, font_small, font_tiny = get_font(20), get_font(16), get_font(13)

# Збереження
SAVE_FILE = "save.json"
game_data = {"btc": 0.0, "usd": 0.0, "taps": 0, "task_done": False, "click_lvl": 1, "miners": 0}

if os.path.exists(SAVE_FILE):
    try:
        with open(SAVE_FILE, "r") as f: game_data.update(json.load(f))
    except: pass

mode, btc_price = "TAPPER", 62000.0
price_history = [62000.0] * 20
last_update = last_passive = pygame.time.get_ticks()
tap_effects = []
clock = pygame.time.Clock()

def draw_text(text, font, color, x, y, center=False):
    img = font.render(str(text), True, color)
    rect = img.get_rect()
    if center: rect.center = (x, y)
    else: rect.topleft = (x, y)
    screen.blit(img, rect)

while True:
    screen.fill(BLACK)
    now = pygame.time.get_ticks()
    
    # Пасивний дохід
    if now - last_passive > 1000:
        game_data["usd"] += game_data["miners"] * 0.5
        last_passive = now

    # Оновлення курсу (Шанс 60% ріст / 40% падіння)
    if now - last_update > 20000:
        change = random.uniform(0.01, 0.08) if random.random() < 0.60 else random.uniform(-0.06, -0.01)
        btc_price += btc_price * change
        price_history.append(btc_price)
        if len(price_history) > 20: price_history.pop(0)
        last_update = now

    # Рендер інтерфейсу (спрощено для стабільності)
    pygame.draw.rect(screen, (25, 25, 25), (0, 0, WIDTH, 95))
    draw_text(f"USD: ${round(game_data['usd'], 2)}", font_main, GREEN, 15, 15)
    draw_text(f"BTC: {round(game_data['btc'], 4)}", font_small, GOLD, 15, 45)

    m_w = WIDTH // 3
    for i, (txt, clr, m) in enumerate([("ТАП", PURPLE, "TAPPER"), ("БІРЖА", BLUE, "MARKET"), ("МАГАЗ", GREEN, "SHOP")]):
        rect = pygame.Rect(i*m_w, HEIGHT-70, m_w, 70)
        pygame.draw.rect(screen, clr if mode == m else GRAY, rect)
        draw_text(txt, font_tiny, WHITE, i*m_w + m_w//2, HEIGHT-35, True)

    tap_rect = up_btn = buy_btn = sell_btn = pygame.Rect(0,0,0,0)
    if mode == "TAPPER":
        tap_rect = pygame.draw.circle(screen, GOLD, (WIDTH//2, HEIGHT//2), 70)
        draw_text("₿", get_font(30), BLACK, WIDTH//2, HEIGHT//2, True)
    elif mode == "MARKET":
        draw_text(f"ЦІНА: ${round(btc_price, 1)}", font_main, GOLD, WIDTH//2, 130, True)
        buy_btn = pygame.draw.rect(screen, GREEN, (20, 200, WIDTH//2-30, 50), border_radius=10)
        sell_btn = pygame.draw.rect(screen, RED, (WIDTH//2+10, 200, WIDTH//2-30, 50), border_radius=10)
    elif mode == "SHOP":
        up_btn = pygame.draw.rect(screen, PURPLE, (20, 150, WIDTH-40, 60), border_radius=10)
        draw_text(f"UPGRADE CLICK: ${game_data['click_lvl']*20}", font_tiny, WHITE, WIDTH//2, 180, True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            p = event.pos
            if p[1] > HEIGHT-70:
                if p[0] < m_w: mode = "TAPPER"
                elif p[0] < m_w*2: mode = "MARKET"
                else: mode = "SHOP"
            if mode == "TAPPER" and tap_rect.collidepoint(p):
                game_data['usd'] += 0.01 * game_data['click_lvl']
            if mode == "MARKET":
                if buy_btn.collidepoint(p) and game_data['usd'] >= btc_price*0.1:
                    game_data['usd'] -= btc_price*0.1; game_data['btc'] += 0.1
                if sell_btn.collidepoint(p) and game_data['btc'] >= 0.1:
                    game_data['usd'] += btc_price*0.1; game_data['btc'] -= 0.1
            if mode == "SHOP" and up_btn.collidepoint(p) and game_data['usd'] >= game_data['click_lvl']*20:
                game_data['usd'] -= game_data['click_lvl']*20; game_data['click_lvl'] += 1

    pygame.display.flip()
    clock.tick(30)
              
