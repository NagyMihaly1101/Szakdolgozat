import pygame as pg
import sys
import random

WIN_SIZE = 700
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)

class TicTacToe:
    def __init__(self, game):
        self.game = game
        #Betöltjük a játéktáblát és a játékosok jelképeit
        self.field_image = self.get_scaled_image(path='../Assets/TicTacToe/field.png',
                                                 res=[WIN_SIZE] * 2)
        self.O_image = self.get_scaled_image(path='../Assets/TicTacToe/o.png',
                                             res=[CELL_SIZE] * 2)
        self.X_image = self.get_scaled_image(path='../Assets/TicTacToe/x.png',
                                             res=[CELL_SIZE] * 2)
        #Játékmező inicializálása végtelen értékekkel (üres cellák)
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]

        if random.randint(0, 1) == 0:
            self.human_symbol = 'X'
            self.ai_symbol = 'O'
            self.player = 0  #A játékos kezd
        else:
            self.human_symbol = 'O'
            self.ai_symbol = 'X'
            self.player = 1  #A számítógép kezd
        #Sorok, amelyek a győzelmi feltételeket tartalmazzák
        self.line_indices_array = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]
        self.winner = None
        self.game_steps = 0
        self.first_move_delay = pg.time.get_ticks() + 500
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 4, True)

    #Számítógép lépései
    def ai_move(self):
        for line_indices in self.line_indices_array:
            line = [self.game_array[i][j] for i, j in line_indices]
            if line.count(1) == 2 and line.count(INF) == 1:
                #A számítógép nyerhet
                for i, j in line_indices:
                    if self.game_array[i][j] == INF:
                        self.game_array[i][j] = 1
                        return
            elif line.count(0) == 2 and line.count(INF) == 1:
                #A számítógép megakadályozhatja az ellenfelet
                for i, j in line_indices:
                    if self.game_array[i][j] == INF:
                        self.game_array[i][j] = 1
                        return

        #Ha nincs azonnali nyerés/megállítás, véletlenszerű lépés
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.game_array[i][j] == INF]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.game_array[i][j] = 1

    #Győztes ellenőrzése
    def check_winner(self):
        for line_indices in self.line_indices_array:
            sum_line = sum([self.game_array[i][j] for i, j in line_indices])
            if sum_line in {0, 3}:
                self.winner = self.human_symbol if sum_line == 0 else self.ai_symbol
                # Ha a játékos nyert növeljük a győzelmek számát
                if self.winner == self.human_symbol:
                    self.game.human_wins += 1
                self.winner_line = [vec2(line_indices[0][::-1]) * CELL_SIZE + CELL_CENTER,
                                    vec2(line_indices[2][::-1]) * CELL_SIZE + CELL_CENTER]

    def run_game_process(self):
        if self.winner:
            return

        current_time = pg.time.get_ticks()

        if self.player == 0 and current_time < self.first_move_delay:
            return

        if self.player == 0:  #A játékos lépése
            current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
            col, row = map(int, current_cell)
            left_click = pg.mouse.get_pressed()[0]

            if left_click and self.game_array[row][col] == INF:
                self.game_array[row][col] = self.player
                self.player = 1  #Átváltunk a számítógép lépésére
                self.game_steps += 1
                self.check_winner()     #Ellenőrízzük van-e győztes
        else:  #A számítógép lépése
            self.ai_move()
            self.player = 0  #Átváltunk a játékos lépésére
            self.game_steps += 1
            self.check_winner()

    #Játékobjektumok kirajzolása
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != INF:
                    symbol = self.human_symbol if obj == 0 else self.ai_symbol
                    image = self.X_image if symbol == 'X' else self.O_image
                    self.game.screen.blit(image, vec2(x, y) * CELL_SIZE)

    #Győztes kirajzolása
    def draw_winner(self):
        if self.winner:
            pg.draw.line(self.game.screen, 'red', *self.winner_line, CELL_SIZE // 8)    #Győztes vonal rajzolása
            label = self.font.render(f'Player "{self.winner}" wins!', True, 'white', 'black')
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 4))
        elif self.game_steps == 9 and not self.winner:  #Döntetlen ellenőrzése
            label = self.font.render('Tie Game!', True, 'white', 'black')
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 4))
            pg.display.update()
            pg.time.delay(1000)

    #Játék kirajzolása
    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner()

    #Kép betöltése és méretezése
    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)

    #Az ablak címsorának beállítása
    def print_caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')
        if self.winner:
            pg.display.set_caption(f'Player "{self.winner}" wins! Press Space to Restart')
        elif self.game_steps == 9:
            pg.display.set_caption(f'Game Over! Press Space to Restart')

    #A játék folyamata
    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.human_wins = 0  #Játékos győzelmek száma
        self.tic_tac_toe = TicTacToe(self)
        self.restart_count = 0  #Újraindítások száma
        self.max_restarts = 2  #Maximum újraindítások száma
    #Új játék indítása
    def new_game(self):
        if self.restart_count < self.max_restarts:
            self.tic_tac_toe = TicTacToe(self)
            self.restart_count += 1  #Újraindítások számának növelése
        else:
            self.show_restart_limit_message()

    #Üzenet megjelenítése, ha elértük a maximumot
    def show_restart_limit_message(self):
        label = pg.font.SysFont('Verdana', 32).render('Csak kétszer indíthatod újra!', True, 'white', 'black')
        self.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 2))
        pg.display.update()
        pg.time.delay(2000)

    #Események ellenőrzése
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE: #Ha lenyomjuk a SPACE-t újraindul a játék
                    self.new_game()
                elif event.key == pg.K_ESCAPE:  #Ha lenyomjuk az ESC-et kilép a játékból
                    return False

    def run(self):
        while True:
            self.tic_tac_toe.run()
            if self.check_events() is False:
                return
            pg.display.update()
            self.clock.tick(60)

def tic_tac_toe():
    game = Game()
    game.run()
    return game.human_wins

if __name__ == '__main__':
    tic_tac_toe()