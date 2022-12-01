import pygame 
from src.pokemon import Pokemon

pygame.init()
class InputBox:
    def __init__(self, x=100, y=100, w=160, h=32, text=''):
        self.screen = pygame.display.set_mode((640, 480))  
        self.rect = pygame.Rect(x, y, w, h)
        self.colorOff = pygame.Color('lightskyblue3')
        self.colorOn = pygame.Color('dodgerblue2')
        self.font = pygame.font.Font(None, 32)
        self.color = self.colorOff
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.colorOn if self.active else self.colorOff
          # changing the string
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    Pokemon().pokemonsprite(pokemonname=self.text)
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)    
  