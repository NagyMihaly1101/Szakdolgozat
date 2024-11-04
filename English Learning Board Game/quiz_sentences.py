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
    ["The cat is ___ the tree.", ["under", "opposite", "flying", "reading"]],
    ["I like to eat ___ for breakfast.", ["eggs", "shoes", "books", "pencils"]],
    ["My father drives a ___.", ["car", "boat", "train", "bicycle"]],
    ["The sky is ___.", ["blue", "green", "red", "black"]],
    ["She is ___ a book.", ["reading", "cooking", "playing", "running"]],
    ["The dog is ___ the house.", ["inside", "outside", "over", "under"]],
    ["He ___ soccer after school.", ["plays", "cooks", "reads", "draws"]],
    ["I am wearing a ___ today.", ["jacket", "banana", "cup", "pencil"]],
    ["The baby is ___.", ["crying", "driving", "reading", "running"]],
    ["We saw a ___ at the zoo.", ["lion", "car", "pencil", "cup"]],
    ["My favorite fruit is ___.", ["apple", "bread", "chicken", "water"]],
    ["The chair is made of ___.", ["wood", "paper", "water", "stone"]],
    ["She has ___ hair.", ["long", "blue", "round", "plastic"]],
    ["We swim in the ___.", ["pool", "car", "tree", "grass"]],
    ["I need a ___ to write.", ["pen", "shoe", "bottle", "book"]],
    ["We wear ___ on our feet.", ["shoes", "hats", "gloves", "belts"]],
    ["He is ___ to music.", ["listening", "looking", "watching", "touching"]],
    ["I brush my ___ every morning.", ["teeth", "hair", "shoes", "clothes"]],
    ["The sun sets in the ___.", ["evening", "morning", "night", "midnight"]],
    ["We drive on the ___.", ["road", "water", "grass", "air"]],
    ["The birds are ___ in the sky.", ["flying", "walking", "jumping", "running"]],
    ["We eat lunch at ___.", ["noon", "midnight", "dawn", "sunset"]],
    ["She wears a ___ when it is cold.", ["coat", "hat", "t-shirt", "shorts"]],
    ["You need to ___ your homework.", ["finish", "cook", "paint", "play"]],
    ["The dog is ___ its tail.", ["chasing", "eating", "cooking", "writing"]],
    ["We sit on a ___.", ["chair", "table", "door", "wall"]],
    ["The bus will ___ soon.", ["arrive", "fly", "swim", "drive"]],
    ["He is wearing a red ___.", ["shirt", "banana", "car", "book"]],
    ["We ___ when we are happy.", ["smile", "cry", "sleep", "sit"]],
    ["A fish lives in the ___.", ["water", "sky", "forest", "house"]],
    ["You can write with a ___.", ["pencil", "fork", "shoe", "button"]],
    ["We eat with a ___.", ["fork", "shoe", "book", "hat"]],
    ["It is ___ in the winter.", ["cold", "hot", "rainy", "cloudy"]],
    ["She plays the ___.", ["piano", "ball", "card", "book"]],
    ["We go to bed at ___.", ["night", "morning", "evening", "dawn"]],
    ["I ___ my hands before eating.", ["wash", "dry", "paint", "fold"]],
    ["She is ___ a picture.", ["drawing", "cooking", "cleaning", "towing"]],
    ["We read books in the ___.", ["library", "kitchen", "garden", "garage"]],
    ["The clock shows ___.", ["time", "height", "speed", "weight"]],
    ["He is eating ___.", ["lunch", "hat", "shoes", "music"]],
    ["I use a ___ to call my friend.", ["phone", "book", "pen", "hat"]],
    ["The sun is very ___.", ["bright", "dark", "cold", "slow"]],
    ["I ___ my bike to school.", ["ride", "drive", "fly", "sail"]],
    ["The teacher is ___ the lesson.", ["teaching", "writing", "cooking", "playing"]],
    ["A bird has ___.", ["wings", "hair", "fins", "teeth"]],
    ["We drink water when we are ___.", ["thirsty", "sleepy", "tired", "cold"]],
    ["The flowers are ___.", ["beautiful", "heavy", "loud", "tall"]],
    ["She is ___ the window.", ["cleaning", "eating", "jumping", "drawing"]],
    ["The bus is ___ at the station.", ["arriving", "flying", "cooking", "writing"]],
    ["The apple on the table is ___.", ["red", "purple", "blue", "pink"]],
    ["I like to read ___ before bed.", ["books", "forks", "pencils", "cars"]],
    ["The dog is ___ in the garden.", ["running", "flying", "gaming", "painting"]],
    ["She ___ her hands after dinner.", ["washes", "drinks", "writes", "draws"]],
    ["The boy is ___ with his toys.", ["playing", "eating", "sleeping", "reading"]],
    ["We eat ___ with a fork.", ["food", "shoes", "pencils", "glasses"]],
    ["The teacher is ___ on the board.", ["writing", "cooking", "sleeping", "painting"]],
    ["We eat dinner in the ___.", ["kitchen", "garage", "bedroom", "garden"]],
    ["He is ___ a letter to his friend.", ["writing", "eating", "painting", "driving"]],
    ["The lamp is ___ on the table.", ["shining", "cooking", "jumping", "playing"]],
    ["She is ___ her shoes.", ["wearing", "drinking", "driving", "writing"]],
    ["The cat is ___ on the sofa.", ["sleeping", "flying", "driving", "eating"]],
    ["We go to school in the ___.", ["morning", "evening", "night", "noon"]],
    ["The flowers are ___ in the garden.", ["blooming", "jumping", "swimming", "drawing"]],
    ["The plane is ___ in the sky.", ["flying", "running", "eating", "jumping"]],
    ["She uses a ___ to cut vegetables.", ["knife", "pencil", "phone", "fork"]],
    ["We ___ songs during the concert.", ["sing", "cook", "write", "run"]],
    ["The clock ___ the time.", ["shows", "reads", "eats", "sings"]],
    ["He is ___ a movie on the TV.", ["watching", "writing", "painting", "cooking"]],
    ["She is ___ a picture with crayons.", ["drawing", "driving", "running", "cooking"]],
    ["We walk to the ___ every day.", ["park", "car", "phone", "book"]],
    ["The baby is ___ a bottle of milk.", ["drinking", "reading", "writing", "painting"]],
    ["The tree has ___ leaves in the fall.", ["yellow", "blue", "pink", "red"]],
    ["We ___ outside on a sunny day.", ["play", "sleep", "read", "write"]],
    ["The bird is ___ in the nest.", ["sleeping", "flying", "driving", "writing"]],
    ["We ___ to music on the radio.", ["listen", "eat", "paint", "run"]],
    ["She is ___ the door for her friend.", ["opening", "writing", "drawing", "painting"]],
    ["I need to ___ my shoes.", ["tie", "read", "eat", "paint"]],
    ["He is ___ a bike in the park.", ["riding", "eating", "flying", "singing"]],
    ["We ___ for the bus at the stop.", ["wait", "write", "cook", "fly"]]
]

answered_questions = []

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
        pygame.draw.rect(screen, self.bg, (self.rect.left - 50, self.rect.top, 500, self.rect.height))
        pygame.gfxdraw.rectangle(screen, (self.rect.left - 50, self.rect.top, 500, self.rect.height), self.borderc)

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
sentences_points = 0
run = 0

#Visszajelzés címke és időzítés
feedback_label = Label(screen, "", 420, 600, size=40, color="black")
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
        if button.text != questions[qnum-1][1][0]:  #Csak a helyes válasz maradjon
            button.kill()

def remove_answered_questions(questions, answered_questions):
    return [q for q in questions if q not in answered_questions]

#Kérdés és válaszok megjelenítése
def show_question(qnum):
    kill()  #Előző kérdés gombjainak eltávolítása
    feedback_label.change_text("")  #Visszajelzés törlése
    pos = [200, 300, 400, 500]  #Válasz gombok helyzetei
    random.shuffle(pos)  #Helyzetek véletlenszerű keverése

    for i, ans in enumerate(questions[qnum-1][1]):
        command = on_right if i == 0 else on_false  #Helyes válaszra az on_right, hibásra az on_false
        Button((450, pos[i]), ans, 72, "black on orange", hover_colors="black on yellow", style="button1", borderc=(255, 255, 255), command=command)

#Minden gomb eltávolítása
def kill():
    for button in buttons:
        button.kill()

#Kérdés címkéjének létrehozása
question_font_size = 50

def create_title_label():
    title_text = f"{qnum}. {questions[qnum-1][0]}"  #Kérdés szövege és száma
    title_size = fontsize(question_font_size)
    title_surface = title_size.render(title_text, True, "black")
    title_width = title_surface.get_width()
    title_x = (screen.get_width() - title_width) // 2  #Középre igazítás
    return Label(screen, title_text, title_x, 70, size=question_font_size, color="black")

title = create_title_label()  #Címke létrehozása

#Fő program
def quiz_sentences():
    global qnum, waiting_for_feedback, feedback_start_time, game_finished, answered_questions, questions, points, sentences_points, run
    time.sleep(0.25)
    waiting_for_feedback = False
    feedback_start_time = None
    game_finished = False
    qnum = 1

    if run > 0:
        title.change_text(f"{qnum}. {questions[qnum - 1][0]}", color="black")
        title.change_position((screen.get_width() - title.image.get_width()) // 2, 70)  # Középre igazítás
        show_question(qnum)
    else:
        show_question(qnum)

    while True:
        screen.blit(background_image, (0, 0))  #Háttér megjelenítése
        title.draw()

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
                    sentences_points += points
                    kill()
                    feedback_label.change_text("")
                    title.change_text(f"{points} pontot értél el.", color="black")
                    title.change_position(350, 325)
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
    quiz_sentences()