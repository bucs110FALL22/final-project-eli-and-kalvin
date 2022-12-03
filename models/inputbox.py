import pygame 
from src.pokemon import Pokemon

pygame.init()
class InputBox:
    def __init__(self, x=100, y=100, w=160, h=32, text=''):
        self.screen = pygame.display.set_mode()  
        self.rect = pygame.Rect(x, y, w, h)
        self.colorOff = pygame.Color('lightskyblue3')
        self.colorOn = pygame.Color('dodgerblue2')
        self.font = pygame.font.Font(None, 32)
        self.color = self.colorOff
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
      # Handles the pygame event and gives a response accoding to what key is clicked. The enter key runs the pokemon model.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.colorOn if self.active else self.colorOff
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    Pokemon().pokemonsprite(pokemonname=self.text)
                    print(self.text)
                    pokemonspritename = self.text
                    self.text = ''
                    self.txt_surface = self.font.render(self.text, True, self.color)
                    return pokemonspritename
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
    def update(self):
      # Changes the width of the textbox if the text is too long
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def draw(self, screen):
      # Draws/shows the text and textbox 
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)    
  