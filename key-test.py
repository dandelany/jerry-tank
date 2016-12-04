import pygame
pygame.init()

finished = False

while not finished:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      finished = True
      
    if event.type == pygame.KEYDOWN:
      if event.key == 273:
        print('forward')
      elif event.key == 274:
        print('reverse')
      elif event.key == 275:
        print('right')
      elif event.key == 276:
        print('left')
    if event.type == pygame.KEYUP:
      print('stop')