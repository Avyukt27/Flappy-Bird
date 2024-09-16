import pygame

pygame.init()

win_width: int = 700
win_height: int = 1000
window: pygame.Surface = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy Bird")

class Bird:
    def __init__(self, pos: pygame.Vector2, width: int, height: int, flap_force: int) -> None:
        self.pos: pygame.Vector2 = pos
        self.speed: pygame.Vector2 = pygame.Vector2(0, 0)
        self.width: int = width
        self.height: int = height
        self.hitbox: pygame.Rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.flap_force: int = flap_force
        self.flapped: bool = False
    
    def update(self) -> None:
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.flap()
        self.speed.y += GRAVITY
        self.speed.y *= AIR_RESISTANCE
        self.pos.y += self.speed.y

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.rect(win, (255,0,0), self.hitbox)
    
    def flap(self) -> None:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.KEYDOWN:
                print(event.key, pygame.K_SPACE)
                if event.key == pygame.K_SPACE:
                    self.speed.y -= self.flap_force
                    self.flapped = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                if event.button == 1:
                    self.speed.y -= self.flap_force
                    self.flapped = True

def refresh_screen(win: pygame.Surface) -> None:
    win.fill((0,0,0))
    player.draw(win)
    pygame.display.update()

GRAVITY: int = 0.2
AIR_RESISTANCE: int = 0.8

player: Bird = Bird(pygame.Vector2(250, 250), 50, 50, 10)

def main() -> None:
    run: bool = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.update()

        refresh_screen(window)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()