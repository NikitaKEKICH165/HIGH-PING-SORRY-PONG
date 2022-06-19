from pygame import *

print("СТАПЕ")
print("Ты должен выбрать режим.")
ig = input("1 - одиночный; 2 - с другом(можно вымышленным):")
window = display.set_mode((700, 500))
display.set_caption("ПИНГ ВЫСОКИЙ ТОЕСТЬ ПОНГ")
klok = time.Clock()
FPS = 60
kek = Surface((1, 1))
kek.fill((255, 255, 200))
backrooms = transform.scale(kek, (700, 500))

class Persona(sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset_iz_undertale(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(Persona):
    def __init__(self, x):
        self.calor = 0
        self.colar = 255
        self.calar = 0
        self.widt = 50
        self.higt = 50
        self.kartina = Surface((self.widt, self.higt))
        self.kartina.fill((self.calor, self.colar, self.calar))
        self.rect = self.kartina.get_rect()
        self.rect.x = x
        self.rect.y = 0
    def narisuy(self):
        window.blit(self.kartina, (self.rect.x, self.rect.y))
    def move(self):
        window.blit(self.kartina, (self.rect.x, self.rect.y))
        global napravlenie, finish
        if self.rect.x <= 0 and sprite.collide_rect(self, pl1):
            napravlenie = "pravo"
        if self.rect.x >= 650 and sprite.collide_rect(self, pl2):
            napravlenie = "levo"

        if napravlenie == "pravo":
            self.rect.x += 5
        if napravlenie == "levo":
            self.rect.x -= 5
        global chast
        if self.rect.y <= 0:
            chast = "d"
        if self.rect.y >= 450:
            chast = "v"

        if chast == "v":
            self.rect.y -= 5
        if chast == "d":
            self.rect.y += 5
    def mesto(self):
        if self.rect.x <= -35:
            fif = True
        elif self.rect.x >= 655:
            fif = True
        else:
            fif = False
        return fif

class Doska(Persona):
    def __init__(self, calor, colar, calar, x, f):
        self.calor = calor
        self.colar =colar
        self.calar = calar
        self.widt = 10
        self.higt = 100
        self.kartina = Surface((self.widt, self.higt))
        self.kartina.fill((self.calor, self.colar, self.calar))
        self.rect = self.kartina.get_rect()
        self.rect.x = x
        self.rect.y = 100
        self.f = f
    def narisuy(self):
        window.blit(self.kartina, (self.rect.x, self.rect.y))
    def move(self):
        naszali = key.get_pressed()
        window.blit(self.kartina, (self.rect.x, self.rect.y))
        if self.f == 1:
            if naszali[K_w] and self.rect.y > 0:
                self.rect.y -= 5
            if naszali[K_s] and self.rect.y < 450:
                self.rect.y += 5
        else:
            if naszali[K_UP] and self.rect.y > 0:
                self.rect.y -= 5
            if naszali[K_DOWN] and self.rect.y < 450:
                self.rect.y += 5

ball = Ball(-30)
pl1 = Doska(255, 0, 0, 0, 1)
if ig == "1":
    pl2 = Doska(0, 0, 255, 690, 1)
elif ig == "2":
    pl2 = Doska(0, 0, 255, 690, 0)
font.init()
fontan = font.Font(None, 35)
loh1 = fontan.render("PLAYER 1 SUCK!", True, (180, 0, 0))
loh2 = fontan.render("PLAYER 2 SUCK!", True, (180, 0, 0))
igra = True
finish = False
napravlenie = ""
chast = ""
while igra:
    for e in event.get():
        if e.type == QUIT:
            igra = False
    window.blit(backrooms, (0, 0))
    pl2.narisuy()
    pl1.narisuy()
    ball.narisuy()
    if not finish:
        ball.move()
        pl1.move()
        pl2.move()
        if ball.mesto():
            finish = True
    if ball.rect.x <= -35:
        window.blit(loh1, (200, 200))
    elif ball.rect.x >= 655:
        window.blit(loh2, (200, 200))
    klok.tick(FPS)
    display.update()