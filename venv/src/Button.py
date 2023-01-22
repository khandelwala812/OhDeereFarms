import pygame, sys

#pygame.init()

class Button():
    def __init__(self, x, y, text, text_size):
        self.screen = pygame.display.set_mode((1280,720))
        self.text = text
        self.text_size = text_size
        self.font = pygame.font.Font('assets\Daydream.ttf', self.text_size)
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.moveText = self.font.render(text, True, (0, 200, 0))
        self.size = len(text)
        self.x = x
        self.y = y

    def draw(self, text_color):
        self.rect = pygame.draw.rect(self.screen, ('white'), (self.x, self.y, self.size * self.text_size * 1.5, self.text_size * 2), 2)
        self.screen.blit(self.font.render(self.text, True, (text_color)), (self.x + self.text_size / 2, self.y + 5))
        pygame.display.update()
    
    def detectClick(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True

start_button = Button(150, 200, "Test", 20)
another_button = Button(50, 20, "No", 24)

'''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    start_button.draw('green')
    another_button.draw('red')
    if another_button.detectClick() == True:
        print("True")
'''
