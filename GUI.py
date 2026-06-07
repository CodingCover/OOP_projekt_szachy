import os
import json
import pygame
from bierki import *
from szachownica import Szachownica

#wczytanie bierek z pliku images_bierki
czarny_hetman = pygame.image.load('images_bierki/black queen.png')
#scalowanie
czarny_hetman = pygame.transform.scale(czarny_hetman, (80,80))
#scalowanie_zbitej wersji, off the board
czarny_hetman_maly = pygame.transform.scale(czarny_hetman, (45,45))

czarny_krol = pygame.image.load('images_bierki/black king.png')
czarny_krol = pygame.transform.scale(czarny_krol, (80,80))
czarny_krol_maly = pygame.transform.scale(czarny_krol, (45,45))

czarny_goniec = pygame.image.load('images_bierki/black bishop.png')
czarny_goniec = pygame.transform.scale(czarny_goniec, (80,80))
czarny_goniec_maly = pygame.transform.scale(czarny_goniec, (45,45))

czarny_skoczek = pygame.image.load('images_bierki/black knight.png')
czarny_skoczek = pygame.transform.scale(czarny_skoczek, (80,80))
czarny_skoczek_maly = pygame.transform.scale(czarny_skoczek, (45,45))

czarny_wieza = pygame.image.load('images_bierki/black rook.png')
czarny_wieza = pygame.transform.scale(czarny_wieza, (80,80))
czarny_wieza_maly = pygame.transform.scale(czarny_wieza, (45,45))

czarny_pion = pygame.image.load('images_bierki/black pawn.png')
czarny_pion = pygame.transform.scale(czarny_pion, (65,65))
czarny_pion_maly = pygame.transform.scale(czarny_pion, (45,45))

czarne_bierki = ['wieza','skoczek','goniec','krol','hetman','pion']

bialy_hetman = pygame.image.load('images_bierki/white queen.png')
bialy_hetman = pygame.transform.scale(bialy_hetman, (80,80))
bialy_hetman_maly = pygame.transform.scale(bialy_hetman, (45,45))

bialy_krol = pygame.image.load('images_bierki/white king.png')
bialy_krol = pygame.transform.scale(bialy_krol, (80,80))
bialy_krol_maly = pygame.transform.scale(bialy_krol, (45,45))

bialy_goniec = pygame.image.load('images_bierki/white bishop.png')
bialy_goniec = pygame.transform.scale(bialy_goniec, (80,80))
bialy_goniec_maly = pygame.transform.scale(bialy_goniec, (45,45))

bialy_skoczek = pygame.image.load('images_bierki/white knight.png')
bialy_skoczek = pygame.transform.scale(bialy_skoczek, (80,80))
bialy_skoczek_maly = pygame.transform.scale(bialy_skoczek, (45,45))

bialy_wieza = pygame.image.load('images_bierki/white rook.png')
bialy_wieza = pygame.transform.scale(bialy_wieza, (80,80))
bialy_wieza_maly = pygame.transform.scale(bialy_wieza, (45,45))

bialy_pion = pygame.image.load('images_bierki/white pawn.png')
bialy_pion = pygame.transform.scale(bialy_pion, (65,65))
bialy_pion_maly = pygame.transform.scale(bialy_pion, (45,45))

biale_bierki = ['wieza','skoczek','goniec','krol','hetman','pion']




class InterfejsGraficzny:

    def __init__(self, screen, gra):

        self.screen = screen
        self.gra = gra
        self.zaznaczone = None
        self.mozliwe_ruchy = []
        self.game_over = False
        self.zwyciezca = None
        self.reset_rect = pygame.Rect(650, 20, 200, 50)
        self.undo_rect = pygame.Rect(400, 20, 200, 50)
        self.auto_save_file = 'szachownica_zapis.json'
        self.wynik = {'bialy': 0, 'czarny': 0}
        self.piece_values = {'pion': 1, 'skoczek': 3, 'goniec': 3, 'wieza': 5, 'hetman': 9, 'krol': 0}
        self.state_history = [{'board': self.gra.generuj_stan(), 'player': 'bialy', 'score': self.wynik.copy()}]
        self.has_check_background = True


    def rysujPlansze(self):
        offset_x = 50
        offset_y = 100

        for y in range(8):
            for x in range(8):

                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.screen, 'light gray', (offset_x + x*100,offset_y + y*100 ,100,100))
                else:
                    pygame.draw.rect(self.screen, 'dark gray',(offset_x + x*100,offset_y + y*100 ,100,100))

        for kolor in ['bialy', 'czarny']:
            if self.czySzach(kolor):
                pozycja = self.pozycjaKrola(kolor)
                if pozycja is not None:
                    x, y = pozycja
                    pygame.draw.rect(self.screen, 'red', (offset_x + x*100, offset_y + y*100, 100, 100))

        if self.zaznaczone:
            x, y = self.zaznaczone
            pygame.draw.rect(self.screen, 'yellow', (offset_x + x*100, offset_y + y*100, 100, 100), 4)
        self.rysujResetButton()
        self.rysujUndoButton()
        self.rysujPunkty()

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

    def przetworzKlikniecie(self,mouse_x,mouse_y, kolor=None):
        offset_x = 50
        offset_y = 100
        x = (mouse_x - offset_x) // 100
        y = (mouse_y - offset_y) // 100
        if 0 <= x <= 7 and 0 <= y <= 7:
            bierka = self.gra.tablica[y][x]
            if bierka and bierka.kolor == kolor:
                if self.zaznaczone == (x, y):
                    self.zaznaczone = None
                    self.mozliwe_ruchy = []
                    return False
                self.zaznaczone = (x, y)
                ruchy = bierka.podajRuchy(self.gra.tablica)
                if bierka.nazwa == 'krol':
                    ruchy.extend(self.podajMozliwosciRoszady(bierka))
                self.mozliwe_ruchy = []
                for ruch in ruchy:
                    board, piece, orig = self.symulujRuch((x, y), ruch)
                    legal = not self.czySzach(kolor, board)
                    if piece is not None:
                        piece.x, piece.y = orig
                    if legal:
                        self.mozliwe_ruchy.append(ruch)
                return True
            else:
                self.zaznaczone = None
                self.mozliwe_ruchy = []
                return False
            
    def przetworzRuch(self, mouse_x, mouse_y, player):
        offset_x = 50
        offset_y = 100
        x = (mouse_x - offset_x) // 100
        y = (mouse_y - offset_y) // 100
        if (x, y) in self.mozliwe_ruchy and self.zaznaczone is not None:
            sx, sy = self.zaznaczone
            bierka = self.gra.tablica[sy][sx]
            cel = self.gra.tablica[y][x]
            self.gra.tablica[sy][sx] = None
            self.gra.tablica[y][x] = bierka
            if bierka is not None:
                if cel is not None and cel.kolor != bierka.kolor:
                    self.wynik[bierka.kolor] += self.piece_values.get(cel.nazwa, 0)
                if bierka.nazwa == 'krol' and abs(x - sx) == 2:
                    self.wykonajRoszade(bierka, sx, sy, x, y)
                bierka.x = x
                bierka.y = y
                bierka.po_ruchu = True
            self.zaznaczone = None
            self.mozliwe_ruchy = []
            self.zapiszStanAuto(player)
            return True
        return False

    def podajMozliwosciRoszady(self, krol):
        ruchy = []
        if krol.po_ruchu:
            return ruchy

        kolor = krol.kolor
        if self.czySzach(kolor):
            return ruchy

        przeciwnik = 'czarny' if kolor == 'bialy' else 'bialy'
        ataki_przeciwnika = self.polaAtakowane(przeciwnik)
        wiersz = 7 if kolor == 'bialy' else 0
        if (krol.x, krol.y) != (4, wiersz):
            return ruchy

        if self.czyRoszadaMozliwa(krol, 7, [(5, wiersz), (6, wiersz)], ataki_przeciwnika):
            ruchy.append((6, wiersz))

        if self.czyRoszadaMozliwa(krol, 0, [(1, wiersz), (2, wiersz), (3, wiersz)], ataki_przeciwnika):
            ruchy.append((2, wiersz))

        return ruchy

    def czyRoszadaMozliwa(self, krol, wieza_x, puste_pola, ataki_przeciwnika):
        wiersz = krol.y
        wieza = self.gra.tablica[wiersz][wieza_x]
        if wieza is None or wieza.nazwa != 'wieza' or wieza.kolor != krol.kolor or wieza.po_ruchu:
            return False
        for x, y in puste_pola:
            if self.gra.tablica[y][x] is not None:
                return False
        przejscia = [(3, wiersz), (2, wiersz)] if wieza_x == 0 else [(5, wiersz), (6, wiersz)]
        for pole in przejscia:
            if pole in ataki_przeciwnika:
                return False
        return True

    def wykonajRoszade(self, krol, sx, sy, dx, dy):
        wiersz = sy
        if dx == 6:
            wieza = self.gra.tablica[wiersz][7]
            self.gra.tablica[wiersz][7] = None
            self.gra.tablica[wiersz][5] = wieza
            if wieza is not None:
                wieza.x = 5
                wieza.y = wiersz
                wieza.po_ruchu = True
        elif dx == 2:
            wieza = self.gra.tablica[wiersz][0]
            self.gra.tablica[wiersz][0] = None
            self.gra.tablica[wiersz][3] = wieza
            if wieza is not None:
                wieza.x = 3
                wieza.y = wiersz
                wieza.po_ruchu = True

    def symulujRuch(self, start, end):
        board = [row[:] for row in self.gra.tablica]
        sx, sy = start
        dx, dy = end
        piece = board[sy][sx]
        if piece is None:
            return board, None, None
        orig = (piece.x, piece.y)
        piece.x, piece.y = (dx, dy)
        board[dy][dx] = piece
        board[sy][sx] = None
        return board, piece, orig

    def rysujMozliweRuchy(self):
        offset_x = 50
        offset_y = 100
        selected_piece = None
        if self.zaznaczone is not None:
            sx, sy = self.zaznaczone
            selected_piece = self.gra.tablica[sy][sx]

        for x, y in self.mozliwe_ruchy:
            kx = offset_x + x*100 + 50
            ky = offset_y + y*100 + 50
            color = 'light blue'
            if selected_piece and selected_piece.nazwa == 'krol' and abs(x - selected_piece.x) == 2:
                color = 'purple'
            pygame.draw.circle(self.screen, color, (kx, ky), 20)

    def rysujResetButton(self):
        pygame.draw.rect(self.screen, (40, 40, 40), self.reset_rect)
        pygame.draw.rect(self.screen, 'white', self.reset_rect, 3)
        font = pygame.font.SysFont('arial', 24)
        text = font.render('Resetuj planszę', True, 'white')
        text_rect = text.get_rect(center=self.reset_rect.center)
        self.screen.blit(text, text_rect)

    def resetGame(self):
        self.gra = Szachownica()
        self.zaznaczone = None
        self.mozliwe_ruchy = []
        self.game_over = False
        self.zwyciezca = None
        self.wynik = {'bialy': 0, 'czarny': 0}
        self.state_history = [{'board': self.gra.generuj_stan(), 'player': 'bialy', 'score': self.wynik.copy()}]

    def zapiszStan(self, sciezka='szachownica_zapis.json'):
        self.gra.zapisz_stan(sciezka)

    def zapiszStanAuto(self, player):
        dane = self.gra.generuj_stan()
        with open(self.auto_save_file, 'w', encoding='utf-8') as plik:
            json.dump(dane, plik, ensure_ascii=False, indent=2)
        nastepny_gracz = 'czarny' if player == 'bialy' else 'bialy'
        self.state_history.append({'board': dane, 'player': nastepny_gracz, 'score': self.wynik.copy()})

    def cofnijRuch(self):
        if len(self.state_history) <= 1:
            return None
        self.state_history.pop()
        stan = self.state_history[-1]
        self.gra.wczytaj_stan(stan['board'])
        self.wynik = stan.get('score', {'bialy': 0, 'czarny': 0})
        self.zaznaczone = None
        self.mozliwe_ruchy = []
        self.game_over = False
        self.zwyciezca = None
        return stan['player']

    def rysujPunkty(self):
        font = pygame.font.SysFont('arial', 24)
        tekst_bialy = font.render(f'Biały: {self.wynik["bialy"]} pkt', True, 'white')
        tekst_czarny = font.render(f'Czarny: {self.wynik["czarny"]} pkt', True, 'white')
        self.screen.blit(tekst_bialy, (100, 20))
        self.screen.blit(tekst_czarny, (100, 50))

    def pozycjaKrola(self, kolor):
        for y in range(8):
            for x in range(8):
                bierka = self.gra.tablica[y][x]
                if bierka and bierka.nazwa == 'krol' and bierka.kolor == kolor:
                    return (x, y)
        return None

    def rysujUndoButton(self):
        pygame.draw.rect(self.screen, (40, 40, 40), self.undo_rect)
        pygame.draw.rect(self.screen, 'white', self.undo_rect, 3)
        font = pygame.font.SysFont('arial', 24)
        text = font.render('Cofnij ruch', True, 'white')
        text_rect = text.get_rect(center=self.undo_rect.center)
        self.screen.blit(text, text_rect)

    def polaAtakowane(self, kolor, board=None):
        if board is None:
            board = self.gra.tablica
        ataki = set()
        for y in range(8):
            for x in range(8):
                bierka = board[y][x]
                if bierka and bierka.kolor == kolor:
                    ruchy = bierka.podajRuchy(board)
                    ataki.update(ruchy)
        return ataki

    def koniec_gry(self, kolor):
        self.game_over = True
        self.zwyciezca = kolor

    def rysujWygrana(self):
        if self.game_over and self.zwyciezca:
            font = pygame.font.SysFont("arial", 50)
            text = font.render(f"Koniec gry! {self.zwyciezca.capitalize()} wygrywa!", True, 'red')
            rect = text.get_rect(center=(450, 500))
            self.screen.blit(text, rect)

    def czySzach(self, kolor, board=None):
        if board is None:
            board = self.gra.tablica
        krol_pozycja = None
        for y in range(8):
            for x in range(8):
                bierka = board[y][x]
                if bierka and bierka.nazwa == 'krol' and bierka.kolor == kolor:
                    krol_pozycja = (x, y)
                    break
            if krol_pozycja:
                break

        if not krol_pozycja:
            return False

        przeciwnik = 'czarny' if kolor == 'bialy' else 'bialy'
        ataki_przeciwnika = self.polaAtakowane(przeciwnik, board)
        return krol_pozycja in ataki_przeciwnika

    def czySzachMat(self, kolor):
        if not self.czySzach(kolor):
            return False

        for y in range(8):
            for x in range(8):
                bierka = self.gra.tablica[y][x]
                if bierka and bierka.kolor == kolor:
                    for ruch in bierka.podajRuchy(self.gra.tablica):
                        board, piece, orig = self.symulujRuch((x, y), ruch)
                        legal = not self.czySzach(kolor, board)
                        if piece is not None:
                            piece.x, piece.y = orig
                        if legal:
                            return False
        return True
    