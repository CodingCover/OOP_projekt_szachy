import pygame

pygame.init()

SZEROKOSC = 900
WYSOKOSC = 1000

screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption('Szachy')

font = pygame.font.SysFont("arial", 20)
big_font = pygame.font.SysFont("arial", 50)

timer = pygame.time.Clock()
fps = 60

#wczytanie bierek z pliku images
czarny_hetman = pygame.image.load('images/black queen.png')
#scalowanie
czarny_hetman = pygame.transform.scale(czarny_hetman, (80,80))
#scalowanie_zbitej wersji, off the board
czarny_hetman_maly = pygame.transform.scale(czarny_hetman, (45,45))

czarny_krol = pygame.image.load('images/black king.png')
czarny_krol = pygame.transform.scale(czarny_krol, (80,80))
czarny_krol_maly = pygame.transform.scale(czarny_krol, (45,45))

czarny_goniec = pygame.image.load('images/black bishop.png')
czarny_goniec = pygame.transform.scale(czarny_goniec, (80,80))
czarny_goniec_maly = pygame.transform.scale(czarny_goniec, (45,45))

czarny_skoczek = pygame.image.load('images/black knight.png')
czarny_skoczek = pygame.transform.scale(czarny_skoczek, (80,80))
czarny_skoczek_maly = pygame.transform.scale(czarny_skoczek, (45,45))

czarny_wieza = pygame.image.load('images/black rook.png')
czarny_wieza = pygame.transform.scale(czarny_wieza, (80,80))
czarny_wieza_maly = pygame.transform.scale(czarny_wieza, (45,45))

czarny_pion = pygame.image.load('images/black pawn.png')
czarny_pion = pygame.transform.scale(czarny_pion, (65,65))
czarny_pion_maly = pygame.transform.scale(czarny_pion, (45,45))

czarne_bierki = ['wieza','skoczek','goniec','krol','hetman','pion']

bialy_hetman = pygame.image.load('images/white queen.png')
bialy_hetman = pygame.transform.scale(bialy_hetman, (80,80))
bialy_hetman_maly = pygame.transform.scale(bialy_hetman, (45,45))

bialy_krol = pygame.image.load('images/white king.png')
bialy_krol = pygame.transform.scale(bialy_krol, (80,80))
bialy_krol_maly = pygame.transform.scale(bialy_krol, (45,45))

bialy_goniec = pygame.image.load('images/white bishop.png')
bialy_goniec = pygame.transform.scale(bialy_goniec, (80,80))
bialy_goniec_maly = pygame.transform.scale(bialy_goniec, (45,45))

bialy_skoczek = pygame.image.load('images/white knight.png')
bialy_skoczek = pygame.transform.scale(bialy_skoczek, (80,80))
bialy_skoczek_maly = pygame.transform.scale(bialy_skoczek, (45,45))

bialy_wieza = pygame.image.load('images/white rook.png')
bialy_wieza = pygame.transform.scale(bialy_wieza, (80,80))
bialy_wieza_maly = pygame.transform.scale(bialy_wieza, (45,45))

bialy_pion = pygame.image.load('images/white pawn.png')
bialy_pion = pygame.transform.scale(bialy_pion, (65,65))
bialy_pion_maly = pygame.transform.scale(bialy_pion, (45,45))

biale_bierki = ['wieza','skoczek','goniec','krol','hetman','pion']

class Bierka:
        def __init__(self, kolor, x, y):
            self.kolor = kolor
            self.x = x 
            self.y = y  
class Krol(Bierka):
    def __init__(self, kolor, x, y):
        super().__init__(kolor, x, y)
        self.nazwa = 'krol'
    def podajRuchy(self, tablica):
        ruchy = []

        mozliwe_pola = [
            (self.x,     self.y - 1),  # góra
            (self.x,     self.y + 1),  # dół
            (self.x - 1, self.y),      # lewo
            (self.x + 1, self.y),      # prawo
            (self.x - 1, self.y - 1),  # lewo-góra
            (self.x + 1, self.y - 1),  # prawo-góra
            (self.x - 1, self.y + 1),  # lewo-dół
            (self.x + 1, self.y + 1),  # prawo-dół
        ]

        for x, y in mozliwe_pola:
            if 0 <= x <= 7 and 0 <= y <= 7:
                if tablica[y][x] is None or tablica[y][x].kolor != self.kolor:
                    ruchy.append((x, y))

        return ruchy
class Hetman(Bierka):
    def __init__(self, kolor, x, y):
        super().__init__(kolor, x, y)
        self.nazwa = 'hetman'
    def podajRuchy(self, tablica):
        ruchy = []

        # góra
        for i in range(self.y - 1, -1, -1):
            if tablica[i][self.x] is None:
                ruchy.append((self.x, i))
            elif tablica[i][self.x].kolor != self.kolor:
                ruchy.append((self.x, i))
                break
            else:
                break

        # dół
        for i in range(self.y + 1, 8):
            if tablica[i][self.x] is None:
                ruchy.append((self.x, i))
            elif tablica[i][self.x].kolor != self.kolor:
                ruchy.append((self.x, i))
                break
            else:
                break

        # lewo
        for i in range(self.x - 1, -1, -1):
            if tablica[self.y][i] is None:
                ruchy.append((i, self.y))
            elif tablica[self.y][i].kolor != self.kolor:
                ruchy.append((i, self.y))
                break
            else:
                break

        # prawo
        for i in range(self.x + 1, 8):
            if tablica[self.y][i] is None:
                ruchy.append((i, self.y))
            elif tablica[self.y][i].kolor != self.kolor:
                ruchy.append((i, self.y))
                break
            else:
                break

        # skos prawo-dół
        x, y = self.x + 1, self.y + 1
        while x <= 7 and y <= 7:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x += 1
            y += 1

        # skos prawo-góra
        x, y = self.x + 1, self.y - 1
        while x <= 7 and y >= 0:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x += 1
            y -= 1

        # skos lewo-dół
        x, y = self.x - 1, self.y + 1
        while x >= 0 and y <= 7:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x -= 1
            y += 1

        # skos lewo-góra
        x, y = self.x - 1, self.y - 1
        while x >= 0 and y >= 0:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x -= 1
            y -= 1

        return ruchy
class Wieza(Bierka):
    def __init__(self, kolor, x, y):
        super().__init__(kolor, x, y)
        self.nazwa = 'wieza'
    def podajRuchy(self, tablica):
        ruchy = []

        # w górę
        for i in range(self.y - 1, -1, -1):
            if tablica[i][self.x] is None:
                ruchy.append((self.x, i))
            elif tablica[i][self.x].kolor != self.kolor:
                ruchy.append((self.x, i))
                break
            else:
                break

        # w dół
        for i in range(self.y + 1, 8):
            if tablica[i][self.x] is None:
                ruchy.append((self.x, i))
            elif tablica[i][self.x].kolor != self.kolor:
                ruchy.append((self.x, i))
                break
            else:
                break

        # w lewo
        for i in range(self.x - 1, -1, -1):
            if tablica[self.y][i] is None:
                ruchy.append((i, self.y))
            elif tablica[self.y][i].kolor != self.kolor:
                ruchy.append((i, self.y))
                break
            else:
                break

        # w prawo
        for i in range(self.x + 1, 8):
            if tablica[self.y][i] is None:
                ruchy.append((i, self.y))
            elif tablica[self.y][i].kolor != self.kolor:
                ruchy.append((i, self.y))
                break
            else:
                break

        return ruchy   
class Goniec(Bierka):
    def __init__(self, kolor, x, y):
        super().__init__(kolor, x, y)
        self.nazwa = 'goniec'
    def podajRuchy(self, tablica):
        ruchy = []

        # skos prawo-dół
        x, y = self.x + 1, self.y + 1
        while x <= 7 and y <= 7:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x += 1
            y += 1

        # skos prawo-góra
        x, y = self.x + 1, self.y - 1
        while x <= 7 and y >= 0:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x += 1
            y -= 1

        # skos lewo-dół
        x, y = self.x - 1, self.y + 1
        while x >= 0 and y <= 7:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x -= 1
            y += 1

        # skos lewo-góra
        x, y = self.x - 1, self.y - 1
        while x >= 0 and y >= 0:
            if tablica[y][x] is None:
                ruchy.append((x, y))
            elif tablica[y][x].kolor != self.kolor:
                ruchy.append((x, y))
                break
            else:
                break
            x -= 1
            y -= 1

        return ruchy
class Skoczek(Bierka):
    def __init__(self, kolor, x, y):
        super().__init__(kolor, x, y)
        self.nazwa = 'skoczek'
    def podajRuchy(self, tablica):
        ruchy = []

        mozliwe_pola = [
            (self.x + 2, self.y - 1),
            (self.x + 2, self.y + 1),
            (self.x - 2, self.y - 1),
            (self.x - 2, self.y + 1),
            (self.x + 1, self.y - 2),
            (self.x + 1, self.y + 2),
            (self.x - 1, self.y - 2),
            (self.x - 1, self.y + 2),
        ]

        for x, y in mozliwe_pola:
            if 0 <= x <= 7 and 0 <= y <= 7:
                if tablica[y][x] is None or tablica[y][x].kolor != self.kolor:
                    ruchy.append((x, y))

        return ruchy

class Pion(Bierka):
    def __init__(self, kolor, x, y):
        super().__init__(kolor, x, y)
        self.nazwa = 'pion'

    def podajRuchy(self,tablica):
        ruchy= []
        if self.kolor == 'bialy':
            start_y = 6
            kierunek = -1
        else:
            start_y = 1
            kierunek = 1

        nowy_y = self.y + kierunek
        if tablica[nowy_y][self.x] is None:
            ruchy.append((self.x,nowy_y))       
            if self.y == start_y:
                nowy_y2 = self.y + kierunek * 2
            if tablica[nowy_y2][self.x] is None:
                ruchy.append((self.x,nowy_y2))
        # bicie w lewo
        if self.x - 1 >= 0 and tablica[nowy_y][self.x - 1] is not None:
            if tablica[nowy_y][self.x - 1].kolor != self.kolor:
                ruchy.append((self.x - 1, nowy_y))

        # bicie w prawo
        if self.x + 1 <= 7 and tablica[nowy_y][self.x + 1] is not None:
            if tablica[nowy_y][self.x + 1].kolor != self.kolor:
                ruchy.append((self.x + 1, nowy_y))
        return ruchy

class Szachownica:
    def __init__(self):
        self.tablica = [[None]*8 for _ in range(8)]
        self.inicjalizujPlansze()
        
    def inicjalizujPlansze(self):
        # czarne
        self.tablica[0][0] = Wieza('czarny', 0, 0)
        self.tablica[0][1] = Skoczek('czarny', 1, 0)
        self.tablica[0][2] = Goniec('czarny', 2, 0)
        self.tablica[0][3] = Hetman('czarny', 3, 0)
        self.tablica[0][4] = Krol('czarny', 4, 0)
        self.tablica[0][5] = Goniec('czarny', 5, 0)
        self.tablica[0][6] = Skoczek('czarny', 6, 0)
        self.tablica[0][7] = Wieza('czarny', 7, 0)
        for x in range(8):
            self.tablica[1][x] = Pion('czarny', x, 1)
        # biale
        self.tablica[7][0] = Wieza('bialy', 0, 7)
        self.tablica[7][1] = Skoczek('bialy', 1, 7)
        self.tablica[7][2] = Goniec('bialy', 2, 7)
        self.tablica[7][3] = Hetman('bialy', 3, 7)
        self.tablica[7][4] = Krol('bialy', 4, 7)
        self.tablica[7][5] = Goniec('bialy', 5, 7)
        self.tablica[7][6] = Skoczek('bialy', 6, 7)
        self.tablica[7][7] = Wieza('bialy', 7, 7)
        for x in range(8):
            self.tablica[6][x] = Pion('bialy', x, 6)

class InterfejsGraficzny:

    def __init__(self, screen, gra):

        self.screen = screen
        self.gra = gra
        self.zaznaczone = None
        self.mozliwe_ruchy=[]


    def rysujPlansze(self):
        offset_x = 50
        offset_y = 100

        for y in range(8):
            for x in range(8):

                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.screen, 'light gray', (offset_x + x*100,offset_y + y*100 ,100,100))
                else:
                    pygame.draw.rect(self.screen, 'dark gray',(offset_x + x*100,offset_y + y*100 ,100,100))

        if self.zaznaczone:
            x, y = self.zaznaczone
            pygame.draw.rect(self.screen, 'yellow', (offset_x + x*100, offset_y + y*100, 100, 100), 4)
    def rysujBierki(self):
        offset_x = 50
        offset_y = 100
        for y in range(8):
            for x in range(8):
                bierka = self.gra.tablica[y][x]
                if bierka:
                    if bierka.kolor == 'bialy':
                        obrazki = {'krol': bialy_krol, 'hetman': bialy_hetman, 'wieza': bialy_wieza,
                                    'goniec': bialy_goniec, 'skoczek': bialy_skoczek, 'pion': bialy_pion}
                    else:
                        obrazki = {'krol': czarny_krol, 'hetman': czarny_hetman, 'wieza': czarny_wieza,
                                    'goniec': czarny_goniec, 'skoczek': czarny_skoczek, 'pion': czarny_pion}
                    self.screen.blit(obrazki[bierka.nazwa], (offset_x + x*100 + 10, offset_y + y*100 + 10))

    def przetworzKlikniecie(self,mouse_x,mouse_y):
        offset_x = 50
        offset_y = 100
        x = (mouse_x - offset_x) // 100
        y = (mouse_y - offset_y) // 100
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.zaznaczone = (x, y)
            bierka = self.gra.tablica[y][x]
            if bierka:
                self.mozliwe_ruchy = bierka.podajRuchy(self.gra.tablica)
            else:
                self.mozliwe_ruchy = []
    def rysujMozliweRuchy(self):
        offset_x = 50
        offset_y = 100
        for x, y in self.mozliwe_ruchy:
            kx = offset_x + x*100 + 50
            ky = offset_y + y*100 + 50
            pygame.draw.circle(self.screen, 'light blue', (kx, ky), 20)

szachownica = Szachownica()
interfejs = InterfejsGraficzny(screen,szachownica)

run = True
while run:
    timer.tick(fps)
    screen.fill((50, 50, 50))

    interfejs.rysujPlansze()
    interfejs.rysujMozliweRuchy()
    interfejs.rysujBierki()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            interfejs.przetworzKlikniecie(*pygame.mouse.get_pos())


    pygame.display.flip()

pygame.quit()