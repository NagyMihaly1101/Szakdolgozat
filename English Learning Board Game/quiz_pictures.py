import pygame
import pygame.gfxdraw
import time
import random

#Inicializálja a pygame-et és a mixer modult (hangokat kezelő modul)
pygame.init()
pygame.mixer.init()
hit = pygame.mixer.Sound("../Assets/sounds/hit.wav")  #Hangeffekt betöltése

#Képernyő méretének és órának beállítása
screen = pygame.display.set_mode((1280, 720))  #Játékablak mérete
clock = pygame.time.Clock()  #Óra a frissítések időzítéséhez
pygame.display.set_caption("Angol nyelvű oktatóprogram")  #Ablak címe

#Háttérkép betöltése és méretezése
background_image = pygame.image.load("../Assets/Background/BG_Game.jpg")
background_image = pygame.transform.scale(background_image, (1280, 720))

#Kérdések és válaszok listája
questions = [
    ["Mi látható a képen?", "../Assets/Pics/Snake.jpg", ["Snake", "Mouse", "Tiger", "Elephant"]],
    ["Mi látható a képen?", "../Assets/Pics/Horse.jpg", ["Horse", "Dog", "Bird", "Fish"]],
    ["Mi látható a képen?", "../Assets/Pics/Apple.jpg", ["Apple", "Plum", "Banana", "Grape"]],
    ["Mi látható a képen?", "../Assets/Pics/Carrot.jpg", ["Carrot", "Tomato", "Salad", "Pepper"]],
    ["Mi látható a képen?", "../Assets/Pics/Dog.jpg", ["Dog", "Cat", "Rabbit", "Snake"]],
    ["Mi látható a képen?", "../Assets/Pics/Lion.jpg", ["Lion", "Bear", "Deer", "Elephant"]],
    ["Mi látható a képen?", "../Assets/Pics/Banana.jpg", ["Banana", "Melon", "Apple", "Peach"]],
    ["Mi látható a képen?", "../Assets/Pics/Tomato.jpg", ["Tomato", "Carrot", "Salad", "Radish"]],
    ["Mi látható a képen?", "../Assets/Pics/Bird.jpg", ["Bird", "Owl", "Eagle", "Peacock"]],
    ["Mi látható a képen?", "../Assets/Pics/Elephant.jpg", ["Elephant", "Giraffe", "Kangaroo", "Horse"]],
    ["Mi látható a képen?", "../Assets/Pics/Grape.jpg", ["Grape", "Lemon", "Orange", "Apple"]],
    ["Mi látható a képen?", "../Assets/Pics/Cucumber.jpg", ["Cucumber", "Pepper", "Beetroot", "Radish"]],
    ["Mi látható a képen?", "../Assets/Pics/Giraffe.jpg", ["Giraffe", "Zebra", "Dog", "Fox"]],
    ["Mi látható a képen?", "../Assets/Pics/Tiger.jpg", ["Tiger", "Lion", "Leopard", "Cheetah"]],
    ["Mi látható a képen?", "../Assets/Pics/Orange.jpg", ["Orange", "Lemon", "Grape", "Banana"]],
    ["Mi látható a képen?", "../Assets/Pics/Pepper.jpg", ["Pepper", "Tomato", "Basil", "Salad"]],
    ["Mi látható a képen?", "../Assets/Pics/Duck.jpg", ["Duck", "Cat", "Rabbit", "Snake"]],
    ["Mi látható a képen?", "../Assets/Pics/Fish.jpg", ["Fish", "Bird", "Snake", "Dog"]],
    ["Mi látható a képen?", "../Assets/Pics/Peach.jpg", ["Peach", "Apple", "Banana", "Plum"]],
    ["Mi látható a képen?", "../Assets/Pics/Lettuce.jpg", ["Lettuce", "Pepper", "Tomato", "Broccoli"]],
    ["Mi látható a képen?", "../Assets/Pics/Cat.jpg", ["Cat", "Dog", "Rabbit", "Horse"]],
    ["Mi látható a képen?", "../Assets/Pics/Monkey.jpg", ["Monkey", "Horse", "Tiger", "Fish"]],
    ["Mi látható a képen?", "../Assets/Pics/Hazelnut.jpg", ["Hazelnut", "Pear", "Apple", "Plum"]],
    ["Mi látható a képen?", "../Assets/Pics/Onion.jpg", ["Onion", "Garlic", "Pepper", "Radish"]],
    ["Mi látható a képen?", "../Assets/Pics/Parrot.jpg", ["Parrot", "Owl", "Eagle", "Peacock"]],
    ["Mi látható a képen?", "../Assets/Pics/Sheep.jpg", ["Sheep", "Cat", "Rabbit", "Snake"]],
    ["Mi látható a képen?", "../Assets/Pics/Plum.jpg", ["Plum", "Apple", "Pear", "Lemon"]],
    ["Mi látható a képen?", "../Assets/Pics/Radish.jpg", ["Radish", "Salad", "Basil", "Lettuce"]],
    ["Mi látható a képen?", "../Assets/Pics/Rabbit.jpg", ["Rabbit", "Squirrel", "Cat", "Dog"]],
    ["Mi látható a képen?", "../Assets/Pics/Octopus.jpg", ["Octopus", "Dolphin", "Whale", "Fish"]],
    ["Mi látható a képen?", "../Assets/Pics/Cherry.jpg", ["Cherry", "Grape", "Lime", "Orange"]],
    ["Mi látható a képen?", "../Assets/Pics/Pumpkin.jpg", ["Pumpkin", "Tomato", "Corn", "Salad"]],
    ["Mi látható a képen?", "../Assets/Pics/Zebra.jpg", ["Zebra", "Giraffe", "Horse", "Lion"]],
    ["Mi látható a képen?", "../Assets/Pics/Wolf.jpg", ["Wolf", "Dog", "Fox", "Tiger"]],
    ["Mi látható a képen?", "../Assets/Pics/Pineapple.jpg", ["Pineapple", "Mango", "Banana", "Orange"]],
    ["Mi látható a képen?", "../Assets/Pics/Garlic.jpg", ["Garlic", "Onion", "Beetroot", "Radish"]],
    ["Mi látható a képen?", "../Assets/Pics/Owl.jpg", ["Owl", "Parrot", "Eagle", "Hawk"]],
    ["Mi látható a képen?", "../Assets/Pics/Fox.jpg", ["Fox", "Wolf", "Deer", "Rabbit"]],
    ["Mi látható a képen?", "../Assets/Pics/Pear.jpg", ["Pear", "Apple", "Banana", "Plum"]],
    ["Mi látható a képen?", "../Assets/Pics/Peas.jpg", ["Peas", "Bean", "Lentil", "Corn"]],
    ["Mi látható a képen?", "../Assets/Pics/Bear.jpg", ["Bear", "Lion", "Tiger", "Elephant"]],
    ["Mi látható a képen?", "../Assets/Pics/Dolphin.jpg", ["Dolphin", "Shark", "Whale", "Fish"]],
    ["Mi látható a képen?", "../Assets/Pics/Walnut.jpg", ["Walnut", "Orange", "Lime", "Apple"]],
    ["Mi látható a képen?", "../Assets/Pics/Zucchini.jpg", ["Zucchini", "Tomato", "Eggplant", "Pepper"]],
    ["Mi látható a képen?", "../Assets/Pics/Eagle.jpg", ["Eagle", "Owl", "Hawk", "Parrot"]],
    ["Mi látható a képen?", "../Assets/Pics/Kangaroo.jpg", ["Kangaroo", "Elephant", "Giraffe", "Rabbit"]],
    ["Mi látható a képen?", "../Assets/Pics/Lime.jpg", ["Lime", "Orange", "Lemon", "Kiwi"]],
    ["Mi látható a képen?", "../Assets/Pics/Spinach.jpg", ["Spinach", "Salad", "Basil", "Lettuce"]],
    ["Mi látható a képen?", "../Assets/Pics/Penguin.jpg", ["Penguin", "Duck", "Goose", "Swan"]],
    ["Mi látható a képen?", "../Assets/Pics/Goose.jpg", ["Goose", "Dog", "Fox", "Tiger"]],
    ["Mi látható a képen?", "../Assets/Pics/Melon.jpg", ["Melon", "Apple", "Lemon", "Pear"]],
    ["Mi látható a képen?", "../Assets/Pics/Potato.jpg", ["Potato", "Tomato", "Corn", "Salad"]],
    ["Mi látható a képen?", "../Assets/Pics/Peacock.jpg", ["Peacock", "Parrot", "Owl", "Pigeon"]],
    ["Mi látható a képen?", "../Assets/Pics/Deer.jpg", ["Deer", "Moose", "Horse", "Fox"]],
    ["Mi látható a képen?", "../Assets/Pics/Avocado.jpg", ["Avocado", "Pear", "Apple", "Plum"]],
    ["Mi látható a képen?", "../Assets/Pics/Beetroot.jpg", ["Beetroot", "Carrot", "Radish", "Onion"]],
    ["Mi látható a képen?", "../Assets/Pics/Shark.jpg", ["Shark", "Dolphin", "Whale", "Fish"]],
    ["Mi látható a képen?", "../Assets/Pics/Bee.jpg", ["Bee", "Owl", "Hawk", "Parrot"]],
    ["Mi látható a képen?", "../Assets/Pics/Kiwi.jpg", ["Kiwi", "Pear", "Apple", "Plum"]],
    ["Mi látható a képen?", "../Assets/Pics/Kohlrabi.jpg", ["Kohlrabi", "Salad", "Basil", "Lettuce"]],
    ["Mi látható a képen?", "../Assets/Pics/Turtle.jpg", ["Turtle", "Crocodile", "Lizard", "Snake"]],
    ["Mi látható a képen?", "../Assets/Pics/Camel.jpg", ["Camel", "Horse", "Elephant", "Zebra"]],
    ["Mi látható a képen?", "../Assets/Pics/Mango.jpg", ["Mango", "Grape", "Orange", "Banana"]],
    ["Mi látható a képen?", "../Assets/Pics/Broccoli.jpg", ["Broccoli", "Tomato", "Corn", "Salad"]],
    ["Mi látható a képen?", "../Assets/Pics/Squirrel.jpg", ["Squirrel", "Rabbit", "Mouse", "Fox"]],
    ["Mi látható a képen?", "../Assets/Pics/Koala.jpg", ["Koala", "Panda", "Monkey", "Bear"]],
    ["Mi látható a képen?", "../Assets/Pics/Lemon.jpg", ["Lemon", "Orange", "Lime", "Apple"]],
    ["Mi látható a képen?", "../Assets/Pics/Turnip.jpg", ["Turnip", "Beetroot", "Radish", "Kohlrabi"]],
    ["Mi látható a képen?", "../Assets/Pics/Panda.jpg", ["Panda", "Bear", "Koala", "Tiger"]],
    ["Mi látható a képen?", "../Assets/Pics/Hedgehog.jpg", ["Hedgehog", "Rabbit", "Squirrel", "Mouse"]],
    ["Mi látható a képen?", "../Assets/Pics/Coconut.jpg", ["Coconut", "Mango", "Pear", "Banana"]],
    ["Mi látható a képen?", "../Assets/Pics/Chili.jpg", ["Chili", "Tomato", "Pepper", "Radish"]],
    ["Mi látható a képen?", "../Assets/Pics/Crocodile.jpg", ["Crocodile", "Fish", "Lizard", "Turtle"]],
    ["Mi látható a képen?", "../Assets/Pics/Leopard.jpg", ["Leopard", "Cat", "Tiger", "Lion"]],
    ["Mi látható a képen?", "../Assets/Pics/Fig.jpg", ["Fig", "Plum", "Apple", "Cherry"]],
    ["Mi látható a képen?", "../Assets/Pics/Eggplant.jpg", ["Eggplant", "Zucchini", "Pepper", "Pumpkin"]],
    ["Mi látható a képen?", "../Assets/Pics/Spider.jpg", ["Spider", "Moose", "Horse", "Fox"]],
    ["Mi látható a képen?", "../Assets/Pics/Raccoon.jpg", ["Raccoon", "Fox", "Squirrel", "Rabbit"]],
    ["Mi látható a képen?", "../Assets/Pics/Corn.jpg", ["Corn", "Peas", "Lentil", "Bean"]],
    ["Mi látható a képen?", "../Assets/Pics/Celery.jpg", ["Celery", "Spinach", "Cabbage", "Salad"]],
    ["Mi látható a képen?", "../Assets/Pics/Flamingo.jpg", ["Flamingo", "Swan", "Duck", "Peacock"]],
    ["Mi látható a képen?", "../Assets/Pics/Goat.jpg", ["Goat", "Sheep", "Cow", "Horse"]],
    ["Mi látható a képen?", "../Assets/Pics/Cow.jpg", ["Cow", "Goat", "Buffalo", "Sheep"]],
    ["Mi látható a képen?", "../Assets/Pics/Lizard.jpg", ["Lizard", "Snake", "Frog", "Crocodile"]],
    ["Mi látható a képen?", "../Assets/Pics/Frog.jpg", ["Frog", "Snake", "Lizard", "Turtle"]],
]

answered_questions =[]

#Gombok csoportja (sprite-ként kezeli őket)
buttons = pygame.sprite.Group()

#Gomb osztály, amely kezeli a gombok megjelenését és működését
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, colors, hover_colors, style, borderc, command):
        super().__init__()
        self.text = text
        self.command = command
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")  #Színek felosztása
        self.hover_colors = f"{self.bg} on {self.fg}" if hover_colors == "red on green" else hover_colors
        self.style = style
        self.borderc = borderc
        self.font = pygame.font.SysFont("Ravie", size)  #Gomb betűtípusának beállítása
        self.render(self.text)
        self.rect = pygame.Rect(*position, 500, self.text_render.get_rect().h)
        self.pressed = 1
        buttons.add(self)

    #Gomb szövegének renderelése
    def render(self, text):
        self.text_render = self.font.render(text, True, self.fg)
        self.image = self.text_render

    #Gomb állapotának frissítése (hover, kattintás)
    def update(self):
        if not waiting_for_feedback:
            self.fg, self.bg = self.colors.split(" on ")
            if self.style == "button1":
                self.draw_button1()  #Gomb megrajzolása
            self.hover()  #Hover ellenőrzése
            self.click()  #Kattintás ellenőrzése

    #Gomb megrajzolása
    def draw_button1(self):
        pygame.draw.rect(screen, self.bg, (self.rect.left - 50, self.rect.top, 500, self.rect.height))  #Gomb háttér színe
        pygame.gfxdraw.rectangle(screen, (self.rect.left - 50, self.rect.top, 500, self.rect.height), self.borderc)  #Gomb kerete

    #Ellenőrzi, hogy az egér a gomb felett van-e
    def hover(self):
        self.colors = self.hover_colors if self.rect.collidepoint(pygame.mouse.get_pos()) else self.original_colors

    #Ellenőrzi, hogy a gombot megnyomták-e
    def click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed:  #Bal egérgomb lenyomása
                self.command()  #Hozzárendelt funkció végrehajtása
                self.pressed = 0  #Megakadályozza, hogy újra nyomásba lépjen
            if not pygame.mouse.get_pressed()[0]:
                self.pressed = 1  #Újra engedélyezi a nyomást, ha az egérgombot felengedték

#Betűméret beállítása
def fontsize(size):
    return pygame.font.SysFont("Ravie", size)
font_default = fontsize(20)

#Címkék listája
labels = []

#Címke osztály, amely szöveget jelenít meg a képernyőn
class Label:
    def __init__(self, screen, text, x, y, size=20, color="white"):
        self.font = fontsize(size) if size != 20 else font_default
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect(topleft=(x, y))  #Címke pozíciójának meghatározása
        self.screen = screen
        self.text = text
        labels.append(self)

    #Szöveg módosítása
    def change_text(self, new_text, color="white"):
        self.image = self.font.render(new_text, True, color)

    #Betűtípus és méret módosítása
    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)

    #Címke pozíciójának módosítása
    def change_position(self, x, y):
        self.rect.topleft = (x, y)

    #Címke megjelenítése a képernyőn
    def draw(self):
        self.screen.blit(self.image, self.rect)

#Címkék megjelenítése a képernyőn
def show_labels():
    for label in labels:
        label.draw()

#Helyes válasz esetén végrehajtandó funkció
def on_right():
    check_score("right")

#Hibás válasz esetén végrehajtandó funkció
def on_false():
    check_score()

qnum = 1
points = 0
pic_points = 0
run = 0

#Visszajelzés címke és időzítés
feedback_label = Label(screen, "", 420, 610, size=40, color="black")
feedback_display_time = 2
feedback_start_time = None
waiting_for_feedback = False
game_finished = False

#Pontszám ellenőrzése a válasz alapján
def check_score(answered="wrong"):
    global qnum, points, waiting_for_feedback, feedback_start_time, game_finished
    hit.play()  #Hangeffekt lejátszása

    #Visszajelzés szövege és pontszám frissítése
    if answered == "right":
        feedback_label.change_text("Helyes válasz!", color="green")
        points += 1
        remove_wrong_answers()  #Hibás válaszok eltávolítása
        answered_questions.append(questions[qnum - 1])
    else:
        feedback_label.change_text("Helytelen válasz!", color="red")
        remove_wrong_answers()
        answered_questions.append(questions[qnum - 1])

    waiting_for_feedback = True
    feedback_start_time = time.time()

    #Ha az utolsó kérdés volt
    if qnum == 3:
        game_finished = True

#Hibás válaszokat tartalmazó gombok eltávolítása
def remove_wrong_answers():
    for button in buttons:
        if button.text != questions[qnum-1][2][0]:  #Csak a helyes válasz maradjon
            button.kill()

def remove_answered_questions(questions, answered_questions):
    return [q for q in questions if q not in answered_questions]

#Kérdés és válaszok megjelenítése
def show_question(qnum):
    global image
    kill()  #Előző kérdés gombjainak eltávolítása
    feedback_label.change_text("")  #Visszajelzés törlése
    pos = [200, 300, 400, 500]  #Válasz gombok helyzetei
    random.shuffle(pos)  #Helyzetek véletlenszerű keverése

    image_path = questions[qnum - 1][1]
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (400, 400))  #Kép méretének beállítása

    for i, ans in enumerate(questions[qnum-1][2]):
        command = on_right if i == 0 else on_false  #Helyes válaszra az on_right, hibásra az on_false
        Button((150, pos[i]), ans, 72, "black on lightblue", hover_colors="black on yellow", style="button1", borderc=(255, 255, 255), command=command)

#Minden gomb eltávolítása
def kill():
    for button in buttons:
        button.kill()

#Kérdés címkéjének létrehozása
question_font_size = 65

def create_title_label():
    title_text = f"{qnum}. {questions[qnum-1][0]}"  #Kérdés szövege és száma
    title_size = fontsize(question_font_size)
    title_surface = title_size.render(title_text, True, "black")
    title_width = title_surface.get_width()
    title_x = (screen.get_width() - title_width) // 2  #Középre igazítás
    return Label(screen, title_text, title_x, 70, size=question_font_size, color="black")

title = create_title_label()  #Címke létrehozása

#Fő program
def quiz_pictures():
    global qnum, waiting_for_feedback, feedback_start_time, game_finished, image, answered_questions, questions, points, pic_points, run
    time.sleep(0.25)
    waiting_for_feedback = False
    feedback_start_time = None
    game_finished = False
    image = None
    qnum = 1

    if run > 0:
        title.change_text(f"{qnum}. {questions[qnum - 1][0]}", color="black")
        title.change_position((screen.get_width() - title.image.get_width()) // 2, 70)
        show_question(qnum)
    else:
        show_question(qnum)

    while True:
        screen.blit(background_image, (0, 0))  #Háttér megjelenítése
        title.draw()

        if image is not None:
            screen.blit(image, (745, 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #Visszajelzés időzítése és új kérdés megjelenítése
        if waiting_for_feedback:
            if time.time() - feedback_start_time >= feedback_display_time:
                waiting_for_feedback = False

                if game_finished:
                    questions = remove_answered_questions(questions, answered_questions)
                    pic_points += points
                    kill()
                    image = None
                    feedback_label.change_text("")
                    title.change_text(f"{points} pontot értél el.", color="black")
                    title.change_position(275, 325)
                    screen.blit(background_image, (0, 0))
                    points = 0
                    run += 1
                    title.draw()
                    pygame.display.update()
                    time.sleep(2)
                    return
                else:
                    qnum += 1  #Következő kérdés
                    title.change_text(f"{qnum}. {questions[qnum - 1][0]}", color="black")
                    title.change_position((screen.get_width() - title.image.get_width()) // 2, 70)
                    show_question(qnum)  #Új kérdés megjelenítése

        buttons.update()  #Gombok frissítése
        buttons.draw(screen)  #Gombok megjelenítése
        show_labels()  #Címkék megjelenítése
        clock.tick(60)  #Képernyő frissítési sebessége
        pygame.display.update()  #Képernyő frissítése

if __name__ == '__main__':
    quiz_pictures()