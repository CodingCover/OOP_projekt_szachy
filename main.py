import pygame
from bierki import *
from szachownica import Szachownica
from GUI import InterfejsGraficzny

pygame.init()

SZEROKOSC = 900
WYSOKOSC = 1000

screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption('Szachy')

font = pygame.font.SysFont("arial", 20)
big_font = pygame.font.SysFont("arial", 50)

timer = pygame.time.Clock()
fps = 60



szachownica = Szachownica()
interfejs = InterfejsGraficzny(screen, szachownica)
moved = False
kolor = 'bialy'
run = True
while run:
    timer.tick(fps)
    screen.fill((50, 50, 50))
    interfejs.rysujPlansze()
    interfejs.rysujMozliweRuchy()
    interfejs.rysujBierki()
    print("pętla")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if interfejs.reset_rect.collidepoint(mouse_pos):
                interfejs.resetGame()
                kolor = 'bialy'
                moved = False
                continue

            if interfejs.undo_rect.collidepoint(mouse_pos):
                poprzedni_kolor = interfejs.cofnijRuch()
                if poprzedni_kolor is not None:
                    kolor = poprzedni_kolor
                continue

            if not interfejs.game_over:
                if interfejs.zaznaczone is not None:
                    moved = interfejs.przetworzRuch(*mouse_pos, kolor)
                    if not moved:
                        interfejs.przetworzKlikniecie(*mouse_pos, kolor)
                else:
                    interfejs.przetworzKlikniecie(*mouse_pos, kolor)

    if moved:
        poprzedni_gracz = kolor
        kolor = 'czarny' if kolor == 'bialy' else 'bialy'
        if interfejs.czySzachMat(kolor):
            interfejs.koniec_gry(poprzedni_gracz)
        moved = False

    if interfejs.game_over:
        interfejs.rysujWygrana()
    

    


    pygame.display.flip()

pygame.quit()