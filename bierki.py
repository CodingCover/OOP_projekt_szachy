class Bierka:
        def __init__(self, kolor, x, y):
            self.kolor = kolor
            self.x = x 
            self.y = y
            self.po_ruchu = False
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
        # pojedynczy krok do przodu (sprawdź zakres)
        if 0 <= nowy_y <= 7 and tablica[nowy_y][self.x] is None:
            ruchy.append((self.x, nowy_y))
            # podwójny krok z pozycji startowej (sprawdź też zakres)
            if self.y == start_y:
                nowy_y2 = self.y + kierunek * 2
                if 0 <= nowy_y2 <= 7 and tablica[nowy_y2][self.x] is None:
                    ruchy.append((self.x, nowy_y2))
        # bicie w lewo i w prawo — tylko jeśli nowy_y jest w zakresie
        if 0 <= nowy_y <= 7:
            if self.x - 1 >= 0 and tablica[nowy_y][self.x - 1] is not None:
                if tablica[nowy_y][self.x - 1].kolor != self.kolor:
                    ruchy.append((self.x - 1, nowy_y))

            if self.x + 1 <= 7 and tablica[nowy_y][self.x + 1] is not None:
                if tablica[nowy_y][self.x + 1].kolor != self.kolor:
                    ruchy.append((self.x + 1, nowy_y))
        return ruchy