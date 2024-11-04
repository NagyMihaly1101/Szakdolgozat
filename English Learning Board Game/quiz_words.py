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
    ["Mit jelent a 'cat' kifejezés?", ["Macska", "Kutya", "Madár", "Hal"]],
    ["Mit jelent a 'blue' kifejezés?", ["Kék", "Piros", "Sárga", "Fehér"]],
    ["Mit jelent a 'seven' kifejezés?", ["Hét", "Egy", "Négy", "Három"]],
    ["Mit jelent a 'carrot' kifejezés?", ["Répa", "Krumpli", "Hagyma", "Cékla"]],
    ["Mit jelent a 'pen' kifejezés?", ["Toll", "Ceruza", "Radír", "Papír"]],
    ["Mit jelent a 'friend' kifejezés?", ["Barát", "Ellenség", "Tárgy", "Család"]],
    ["Mit jelent a 'fox' kifejezés?", ["Róka", "Farkas", "Nyúl", "Oroszlán"]],
    ["Mit jelent a 'gray' kifejezés?", ["Szürke", "Fekete", "Fehér", "Zöld"]],
    ["Mit jelent a 'banana' kifejezés?", ["Banán", "Alma", "Narancs", "Eper"]],
    ["Mit jelent a 'family' kifejezés?", ["Család", "Barát", "Testvér", "Kolléga"]],
    ["Mit jelent a 'dog' kifejezés?", ["Kutya", "Macska", "Nyúl", "Kígyó"]],
    ["Mit jelent a 'red' kifejezés?", ["Piros", "Zöld", "Kék", "Fekete"]],
    ["Mit jelent a 'potato' kifejezés?", ["Krumpli", "Répa", "Paprika", "Cékla"]],
    ["Mit jelent a 'pencil' kifejezés?", ["Ceruza", "Toll", "Mappa", "Füzet"]],
    ["Mit jelent a 'wolf' kifejezés?", ["Farkas", "Tigris", "Zebra", "Nyúl"]],
    ["Mit jelent a 'green' kifejezés?", ["Zöld", "Piros", "Kék", "Sárga"]],
    ["Mit jelent a 'four' kifejezés?", ["Négy", "Egy", "Nyolc", "Három"]],
    ["Mit jelent a 'spinach' kifejezés?", ["Spenót", "Répa", "Borsó", "Paprika"]],
    ["Mit jelent a 'exam' kifejezés?", ["Vizsga", "Teszt", "Kérdés", "Feladat"]],
    ["Mit jelent a 'bird' kifejezés?", ["Madár", "Eger", "Tigris", "Elefánt"]],
    ["Mit jelent a 'black' kifejezés?", ["Fekete", "Fehér", "Piros", "Zöld"]],
    ["Mit jelent a 'broccoli' kifejezés?", ["Brokkoli", "Hagyma", "Krumpli", "Cékla"]],
    ["Mit jelent a 'ruler' kifejezés?", ["Vonalzó", "Radír", "Ceruza", "Papír"]],
    ["Mit jelent a 'music' kifejezés?", ["Zene", "Tánc", "Kép", "Film"]],
    ["Mit jelent a 'squirrel' kifejezés?", ["Mókus", "Kutya", "Madár", "Patkány"]],
    ["Mit jelent a 'white' kifejezés?", ["Fehér", "Fekete", "Kék", "Piros"]],
    ["Mit jelent a 'kiwi' kifejezés?", ["Kivi", "Alma", "Banán", "Eper"]],
    ["Mit jelent a 'sun' kifejezés?", ["Nap", "Hold", "Csillag", "Égbolt"]],
    ["Mit jelent a 'fish' kifejezés?", ["Hal", "Cápa", "Delfin", "Törpe"]],
    ["Mit jelent a 'yellow' kifejezés?", ["Sárga", "Zöld", "Kék", "Piros"]],
    ["Mit jelent a 'eight' kifejezés?", ["Nyolc", "Egy", "Hét", "Kilenc"]],
    ["Mit jelent a 'pineapple' kifejezés?", ["Ananász", "Málna", "Eper", "Narancs"]],
    ["Mit jelent a 'scarf' kifejezés?", ["Sál", "Sapka", "Kalap", "Pulóver"]],
    ["Mit jelent a 'rabbit' kifejezés?", ["Nyúl", "Patkány", "Kacsa", "Ló"]],
    ["Mit jelent a 'purple' kifejezés?", ["Lila", "Kék", "Zöld", "Sárga"]],
    ["Mit jelent a 'pepper' kifejezés?", ["Paprika", "Borsó", "Hagyma", "Cékla"]],
    ["Mit jelent a 'cow' kifejezés?", ["Tehén", "Ló", "Nyúl", "Bárány"]],
    ["Mit jelent a 'orange' kifejezés?", ["Narancs", "Piros", "Sárga", "Zöld"]],
    ["Mit jelent a 'lemon' kifejezés?", ["Citrom", "Narancs", "Banán", "Eper"]],
    ["Mit jelent a 'phone' kifejezés?", ["Telefon", "Tv", "Füzet", "Tablet"]],
    ["Mit jelent a 'goat' kifejezés?", ["Kecske", "Ló", "Tehén", "Nyúl"]],
    ["Mit jelent a 'brown' kifejezés?", ["Barna", "Fekete", "Szürke", "Piros"]],
    ["Mit jelent a 'five' kifejezés?", ["Öt", "Egy", "Hét", "Három"]],
    ["Mit jelent a 'pear' kifejezés?", ["Körte", "Alma", "Banán", "Dinnye"]],
    ["Mit jelent a 'school' kifejezés?", ["Iskola", "Otthon", "Hotel", "Park"]],
    ["Mit jelent a 'eagle' kifejezés?", ["Sas", "Galamb", "Bagoly", "Kígyó"]],
    ["Mit jelent a 'bread' kifejezés?", ["Kenyér", "Tej", "Sajt", "Hús"]],
    ["Mit jelent a 'brush' kifejezés?", ["Ecset", "Papír", "Ceruza", "Laptop"]],
    ["Mit jelent a 'eraser' kifejezés?", ["Radír", "Toll", "Papír", "Laptop"]],
    ["Mit jelent a 'elephant' kifejezés?", ["Elefánt", "Oroszlán", "Farkas", "Tigris"]],
    ["Mit jelent a 'rice' kifejezés?", ["Rizs", "Tészta", "Répa", "Krumpli"]],
    ["Mit jelent a 'jungle' kifejezés?", ["Dzsungel", "Sivatag", "Tenger", "Hegyek"]],
    ["Mit jelent a 'deer' kifejezés?", ["Szarvas", "Tehén", "Ló", "Bárány"]],
    ["Mit jelent a 'one' kifejezés?", ["Egy", "Öt", "Három", "Négy"]],
    ["Mit jelent a 'salad' kifejezés?", ["Saláta", "Pasta", "Rizs", "Leves"]],
    ["Mit jelent a 'basket' kifejezés?", ["Kosár", "Táska", "Bögré", "Edény"]],
    ["Mit jelent a 'star' kifejezés?", ["Csillag", "Bolygó", "Nap", "Hold"]],
    ["Mit jelent a 'giraffe' kifejezés?", ["Zsiráf", "Elefánt", "Oroszlán", "Nyúl"]],
    ["Mit jelent a 'eleven' kifejezés?", ["Tizenegy", "Kilenc", "Tíz", "Nyolc"]],
    ["Mit jelent a 'soup' kifejezés?", ["Leves", "Saláta", "Desszert", "Hús"]],
    ["Mit jelent a 'dream' kifejezés?", ["Álom", "Valóság", "Terv", "Kép"]],
    ["Mit jelent a 'duck' kifejezés?", ["Kacsa", "Liba", "Pulyka", "Csirke"]],
    ["Mit jelent a 'ice cream' kifejezés?", ["Fagylalt", "Torta", "Süti", "Keksz"]],
    ["Mit jelent a 'vase' kifejezés?", ["Váza", "Tálca", "Bögre", "Süti"]],
    ["Mit jelent a 'pigeon' kifejezés?", ["Galamb", "Róka", "Kígyó", "Kacsa"]],
    ["Mit jelent a 'six' kifejezés?", ["Hat", "Egy", "Kilenc", "Három"]],
    ["Mit jelent a 'cake' kifejezés?", ["Torta", "Fagylalt", "Süti", "Keksz"]],
    ["Mit jelent a 'mountain' kifejezés?", ["Hegy", "Domb", "Völgy", "Kanyon"]],
    ["Mit jelent a 'sheep' kifejezés?", ["Bárány", "Tehén", "Ló", "Kecske"]],
    ["Mit jelent a 'melon' kifejezés?", ["Dinnye", "Körte", "Eper", "Banán"]],
    ["Mit jelent a 'table' kifejezés?", ["Asztal", "Szék", "Füzet", "Laptop"]],
    ["Mit jelent a 'snake' kifejezés?", ["Kígyó", "Gyík", "Béka", "Hal"]],
    ["Mit jelent a 'onion' kifejezés?", ["Hagyma", "Krumpli", "Saláta", "Paprika"]],
    ["Mit jelent a 'happy' kifejezés?", ["Boldog", "Szomorú", "Fáradt", "Haragos"]],
    ["Mit jelent a 'chicken' kifejezés?", ["Csirke", "Pulyka", "Kacsa", "Liba"]],
    ["Mit jelent a 'three' kifejezés?", ["Három", "Nyolc", "Egy", "Négy"]],
    ["Mit jelent a 'corn' kifejezés?", ["Kukorica", "Borsó", "Spenót", "Paprika"]],
    ["Mit jelent a 'chair' kifejezés?", ["Szék", "Asztal", "Fotel", "Kanapé"]],
    ["Mit jelent a 'whale' kifejezés?", ["Bálna", "Cápa", "Delfin", "Hal"]],
    ["Mit jelent a 'cheese' kifejezés?", ["Sajt", "Tejföl", "Vaj", "Kenyér"]],
    ["Mit jelent a 'owl' kifejezés?", ["Bagoly", "Sas", "Galamb", "Róka"]],
    ["Mit jelent a 'cucumber' kifejezés?", ["Uborka", "Saláta", "Paprika", "Hagyma"]],
    ["Mit jelent a 'window' kifejezés?", ["Ablak", "Ajtó", "Fal", "Padló"]],
    ["Mit jelent a 'rich' kifejezés?", ["Gazdag", "Szegény", "Kicsi", "Nagy"]],
    ["Mit jelent a 'bat' kifejezés?", ["Denevér", "Madár", "Gólya", "Rigó"]],
    ["Mit jelent a 'nine' kifejezés?", ["Kilenc", "Hét", "Hat", "Nyolc"]],
    ["Mit jelent a 'egg' kifejezés?", ["Tojás", "Sajt", "Tej", "Joghurt"]],
    ["Mit jelent a 'monkey' kifejezés?", ["Majom", "Kígyó", "Elefánt", "Kutya"]],
    ["Mit jelent a 'butter' kifejezés?", ["Vaj", "Sajt", "Joghurt", "Tejföl"]],
    ["Mit jelent a 'door' kifejezés?", ["Ajtó", "Ablak", "Fal", "Asztal"]],
    ["Mit jelent a 'holiday' kifejezés?", ["Ünnep", "Munka", "Tanulás", "Sport"]],
    ["Mit jelent a 'horse' kifejezés?", ["Ló", "Tehén", "Bárány", "Kecske"]],
    ["Mit jelent a 'ten' kifejezés?", ["Tíz", "Hét", "Nyolc", "Hat"]],
    ["Mit jelent a 'milk' kifejezés?", ["Tej", "Joghurt", "Sajt", "Vaj"]],
    ["Mit jelent a 'light' kifejezés?", ["Fény", "Sötétség", "Nap", "Zaj"]],
    ["Mit jelent a 'old' kifejezés?", ["Régi", "Új", "Kicsi", "Nagy"]],
    ["Mit jelent a 'frog' kifejezés?", ["Béka", "Kígyó", "Nyúl", "Kutya"]],
    ["Mit jelent a 'honey' kifejezés?", ["Méz", "Vaj", "Tejföl", "Sajt"]],
    ["Mit jelent a 'clock' kifejezés?", ["Óra", "Naptár", "Papír", "Ceruza"]],
    ["Mit jelent a 'new' kifejezés?", ["Új", "Régi", "Kicsi", "Nagy"]]
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
        pygame.draw.rect(screen, self.bg, (self.rect.left - 50, self.rect.top, 500,
                                                                  self.rect.height))
        pygame.gfxdraw.rectangle(screen, (self.rect.left - 50, self.rect.top, 500,
                                                    self.rect.height), self.borderc)

    #Ellenőrzi, hogy az egér a gomb felett van-e
    def hover(self):
        self.colors = self.hover_colors if self.rect.collidepoint(pygame.mouse.get_pos()) \
            else self.original_colors

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
quiz_points = 0
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
        answered_questions.append(questions[qnum-1])
    else:
        feedback_label.change_text("Helytelen válasz!", color="red")
        remove_wrong_answers()
        answered_questions.append(questions[qnum-1])

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
        #Helyes válaszra az on_right, hibásra az on_false
        command = on_right if i == 0 else on_false
        Button((450, pos[i]), ans, 72,
                        "black on pink", hover_colors="black on yellow",
                        style="button1", borderc=(255, 255, 255), command=command)

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
def quiz_words():
    global qnum, waiting_for_feedback, feedback_start_time, game_finished, answered_questions, questions, points, quiz_points, run
    time.sleep(0.25)
    waiting_for_feedback = False
    feedback_start_time = None
    game_finished = False
    qnum = 1

    if run > 0:
        title.change_text(f"{qnum}. {questions[qnum - 1][0]}", color="black")
        title.change_position((screen.get_width() - title.image.get_width()) // 2, 70)  #Középre igazítás
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
                    quiz_points += points
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
    quiz_words()