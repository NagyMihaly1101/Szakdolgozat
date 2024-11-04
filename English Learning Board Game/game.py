import pygame
import os
import sys
import time
import random
from quiz_pictures import quiz_pictures
from quiz_words import quiz_words
from quiz_sentences import quiz_sentences
from tictactoe import tic_tac_toe

pygame.init()

BLACK = (0, 0, 0)

#Ablak beállítása
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angol nyelvű oktatóprogram")

#Játékmező beállítása
ROWS, COLS = 8, 11
TILE_WIDTH = WIDTH // COLS
TILE_HEIGHT = HEIGHT // ROWS

#Háttér betöltése
BG_GAME = pygame.transform.scale(pygame.image.load("../Assets/Background/BG_Game.jpg"), (WIDTH, HEIGHT)) if os.path.exists(
    "../Assets/Background/BG_Game.jpg") else pygame.Surface((WIDTH, HEIGHT))

#Képek betöltése
IMAGES_DIR = os.path.join('..', 'Assets/Squares')

def load_image(image_name):
    image_path = os.path.join(IMAGES_DIR, image_name)
    return pygame.image.load(image_path) if os.path.exists(image_path) else pygame.Surface((TILE_WIDTH, TILE_HEIGHT))

#Feladatok képeinek betöltése
IMAGES = {f"Task {i}": load_image(f'{i}.png') for i in range(1, 31)}
IMAGES.update({
    "Start": load_image('start_game.png'),
    "End": load_image('finish_game.png'),
    "Shortcut": load_image('Question Mark.png')
})

#Képek méretezése
for key in IMAGES:
    IMAGES[key] = pygame.transform.scale(IMAGES[key], (TILE_WIDTH, TILE_HEIGHT))

#Mezők
class Squares:
    def __init__(self, x, y, task):
        self.rect = pygame.Rect(x, y, TILE_WIDTH, TILE_HEIGHT)
        self.task = task
        self.image = IMAGES[task]

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft) #Mező képének megrajzolása
        pygame.draw.rect(surface, BLACK, self.rect, 3) #Mező keretének megrajzolása

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) #Ellenőrzi, hogy a mezőre kattintottak-e

#Feladatok elhelyezése a táblán
TASKS = {
    (7, 0): "Start", (7, 1): "Task 1", (6, 1): "Task 2", (5, 1): "Task 3", (5, 0): "Task 4",
    (4, 0): "Task 5", (3, 0): "Task 6", (2, 0): "Task 7", (1, 0): "Task 8", (1, 1): "Task 9",
    (1, 2): "Task 10", (2, 2): "Task 11", (2, 3): "Task 12", (2, 4): "Task 13", (2, 5): "Task 14",
    (3, 5): "Task 15", (4, 5): "Task 16", (5, 5): "Task 17", (6, 5): "Task 18", (6, 6): "Task 19",
    (6, 7): "Task 20", (6, 8): "Task 21", (5, 8): "Task 22", (4, 8): "Task 23", (4, 7): "Task 24",
    (3, 7): "Task 25", (2, 7): "Task 26", (2, 8): "Task 27", (2, 9): "Task 28", (2, 10): "Task 29",
    (1, 10): "Task 30", (0, 10): "End", (5, 2): "Shortcut", (5, 3): "Shortcut", (4, 3): "Shortcut",
    (3, 3): "Shortcut", (1, 5): "Shortcut", (0, 5): "Shortcut", (0, 6): "Shortcut", (0, 7): "Shortcut",
    (1, 7): "Shortcut", (5, 9): "Shortcut", (5, 10): "Shortcut", (4, 10): "Shortcut", (3, 10): "Shortcut"
}

buttons = [Squares(col * TILE_WIDTH, row * TILE_HEIGHT, task) for (row, col), task in TASKS.items()]

#Győzelem szöveg megjelenítése
def draw_text_centered(text, font, color, surface):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    surface.blit(text_surface, text_rect)

#A taskok elérhetőségét jelző szöveg megjelenítése
def draw_text_bottom_right(text, font, color, surface):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
    surface.blit(text_surface, text_rect)

#Játék befejezése és győzelem kiírása
def end_button():
    from quiz_pictures import pic_points
    from quiz_words import quiz_points
    from quiz_sentences import sentences_points
    font = pygame.font.SysFont("Ravie", 60)
    draw_text_centered("Congratulations, You Won!", font, BLACK, WIN)
    sum_points = quiz_points + sentences_points + pic_points    #Pontok összesítése
    points_text = f"Your Total Points: {sum_points}"
    points_surface = font.render(points_text, True, BLACK)
    points_rect = points_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))  # Kiírja a pontokat a szöveg alatt
    WIN.blit(points_surface, points_rect)
    pygame.display.update()
    time.sleep(10)
    pygame.quit()
    sys.exit()

def main():
    global WIN
    run = True
    game_started = False
    start_time = 0
    font = pygame.font.SysFont("Ravie", 30)
    unavailable_task_message = ""  #A nem elérhető feladat üzenete
    message_time = 0  #Az üzenet megjelenítésének időpontja
    question_mark_unlocked = False
    task_3_completed = False
    task_14_completed = False
    task_22_completed = False

    while run:
        WIN.blit(BG_GAME, (0, 0))   #Háttér kirajzolása

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(pos):
                        if button.task == "Start" and not game_started:
                            game_started = True
                            task_progress = 1   #Feladat előrehaladásának nyomon követése
                            start_time = time.time()
                        elif game_started:
                            task_number = button.task.split()[-1]
                            if button.task.startswith("Task"):
                                if task_number.isdigit() and int(task_number) == task_progress:
                                    #Véletlenszerűen választunk egy feladatot
                                    random_quiz = random.choice([quiz_pictures, quiz_words, quiz_sentences])
                                    random_quiz()  #A kiválasztott feladat meghívása
                                    task_progress += 1
                                    #Shortcutok elérhetővé tétele
                                    if task_progress == 4:
                                        task_3_completed = True
                                    if task_progress == 15:
                                        task_14_completed = True
                                    if task_progress == 23:
                                        task_22_completed = True
                                    if task_3_completed or task_14_completed or task_22_completed:
                                        question_mark_unlocked = True

                                elif task_number.isdigit() and int(task_number) < task_progress:
                                    unavailable_task_message = f"A {button.task} már nem használható."
                                    message_time = time.time()
                                else:
                                    unavailable_task_message = f"A {button.task} még nem használható."
                                    message_time = time.time()
                            elif button.task == "Shortcut" and question_mark_unlocked:
                                human_wins = tic_tac_toe()      #Győzelmek összegyűjtése
                                if human_wins >= 1:
                                    if task_progress == 4:
                                        task_progress = 12
                                    elif task_progress == 15:
                                        task_progress = 26
                                    elif task_progress == 22:
                                        task_progress = 29

                                WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                                pygame.display.set_caption("Angol nyelvű oktatóprogram")
                                question_mark_unlocked = False
                            elif button.task == "End" and task_progress > 30:
                                end_button()
        #Timer megjelenítése
        if game_started:
            elapsed_time = int(time.time() - start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            if minutes > 0:
                timer_text = f"Timer: {minutes}min {seconds}sec"
            else:
                timer_text = f"Timer: {seconds}sec"

            timer_surface = font.render(timer_text, True, BLACK)
            WIN.blit(timer_surface, (10, 10))
        #Mezők kirajzolása
        for button in buttons:
            button.draw(WIN)

        if unavailable_task_message and time.time() - message_time < 3:  #Üzenet megjelenítése 3 másodpercig
            draw_text_bottom_right(unavailable_task_message, font, BLACK, WIN)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()