import sys
import pygame
from bullet import Bullet
from alien import Alien


def create_fleet(ai_settings, screen, aliens):
    """create a full fleet of alients"""
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to one alien width
    available_space_x = ai_settings.screen_width - (2 * ai_settings.alien_width)
    number_of_aliens_x = int(available_space_x / (2 * ai_settings.alien_width))

    # create the first row of aliens
    for alien_number in range(number_of_aliens_x):
        # create an alien and place it in a row
        alien = Alien(ai_settings, screen)
        alien.x = ai_settings.alien_width + 2 * ai_settings.alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
        
def check_events(ai_settings, screen, ship, bullets):
    """respond to mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached"""
    # create a new bullet and it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, aliens, bullets):

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # redraw all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)


    # make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """update position of bullets and get rid of old bullets"""
    # update bullet position
    bullets.update()

    # delete bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
