import json
from bierki import *

class Szachownica:
    def __init__(self):
        self.tablica = [[None]*8 for _ in range(8)]
        self.inicjalizujPlansze()

    def generuj_stan(self):
        dane = []
        for y in range(8):
            wiersz = []
            for x in range(8):
                bierka = self.tablica[y][x]
                if bierka is None:
                    wiersz.append(None)
                else:
                    wiersz.append({
                        'nazwa': bierka.nazwa,
                        'kolor': bierka.kolor,
                        'x': bierka.x,
                        'y': bierka.y,
                        'has_moved': getattr(bierka, 'has_moved', False),
                    })
            dane.append(wiersz)
        return dane

    def zapisz_stan(self, sciezka='szachownica_zapis.json'):
        dane = self.generuj_stan()
        with open(sciezka, 'w', encoding='utf-8') as plik:
            json.dump(dane, plik, ensure_ascii=False, indent=2)
    
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

    def wczytaj_stan(self, dane):
        self.tablica = [[None]*8 for _ in range(8)]
        for y, wiersz in enumerate(dane):
            for x, entry in enumerate(wiersz):
                if entry is None:
                    continue
                nazwa = entry['nazwa']
                kolor = entry['kolor']
                has_moved = entry.get('has_moved', False)
                if nazwa == 'krol':
                    bierka = Krol(kolor, x, y)
                elif nazwa == 'hetman':
                    bierka = Hetman(kolor, x, y)
                elif nazwa == 'wieza':
                    bierka = Wieza(kolor, x, y)
                elif nazwa == 'goniec':
                    bierka = Goniec(kolor, x, y)
                elif nazwa == 'skoczek':
                    bierka = Skoczek(kolor, x, y)
                elif nazwa == 'pion':
                    bierka = Pion(kolor, x, y)
                else:
                    bierka = None
                if bierka is not None:
                    bierka.has_moved = has_moved
                self.tablica[y][x] = bierka
