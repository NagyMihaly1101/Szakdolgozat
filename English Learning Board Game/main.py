import pygame
import sys
from button import Button
import game

pygame.font.init()

#Fő ablak beállítások
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angol nyelvű oktatóprogram")

#Háttér kép betöltése és átméretezése
BG = pygame.transform.scale(pygame.image.load("../Assets/Background/BG.jpg"), (WIDTH, HEIGHT))

#Gombok betöltése
start_img = pygame.image.load('../Assets/Buttons/start_btn.png').convert_alpha()
exit_img = pygame.image.load('../Assets/Buttons/exit_btn.png').convert_alpha()

start_button = Button(530, 350, start_img, 0.7)
exit_button = Button(545, 465, exit_img, 0.7)

#Szöveg kirajzolása a megadott felületre
def draw_text(surface, text, font, color, x, y):
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, (x, y))

#Főmenü megjelenítése
def draw_main_menu():
    WIN.blit(BG, (0, 0))
    font = pygame.font.SysFont("Ravie", 60)
    draw_text(WIN, "Adventure Time", font, (0, 0, 0), 310, 200)

    if start_button.draw(WIN): #Ha a start gombot megnyomják Játék állapotba lép
        return 'game'
    if exit_button.draw(WIN): #Ha a kilépés gombot megnyomják Kilép a Pygame-ből
        pygame.quit()
        sys.exit()

    pygame.display.update()
    return 'menu'

def main():
    run = True
    state = 'menu'

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if state == 'menu':
            state = draw_main_menu()  #A főmenü megjelenítése
        elif state == 'game':
            game.main()  #A játék indítása

    pygame.quit()

if __name__ == "__main__":
    main()