import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens)
    pygame.display.set_caption("Alien Invasion")
    alien = Alien(ai_settings,screen)
    pygame.mixer.init()
    music = '1.ogg'
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=0, start=0.0)

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

if __name__ == '__main__':
    run_game()