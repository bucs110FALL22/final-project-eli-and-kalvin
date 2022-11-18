import requests
import pygame

class Background:
  def __init__(self):
    backgroundurl ="https://maps.googleapis.com/maps/api/staticmap?"
    center = 42.085057927873244, -75.97260743367059
    zoom = 20
    size = "400x400"
    api_key = "_your_api_key_"
    self.link = requests.get(f"{backgroundurl}center={center}&zoom={zoom}&size={size}&key={api_key}sensor=false")
  def test(self):
    f= open('address of the file location', 'wb')
    f.write(self.link.content)
  def BackgroundImage():
    pygame.init()
    image = pygame.image.load(link)
    