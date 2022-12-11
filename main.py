import pygame
import sys
import time
import config
from config import parsestory
import textwrap

# Colors
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

HEIGHT = 500
WIDTH = HEIGHT
LINEHEIGHT = 30
TEXTHEIGHT = 200

# Create game
pygame.init()
size = width, height = WIDTH, HEIGHT+TEXTHEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption(config.STORY)

font_name = pygame.font.get_default_font()
font = pygame.font.SysFont('Arial', 20)
bigfont = pygame.font.SysFont('Arial', 30)
hugefont = pygame.font.SysFont('Arial', 50)

def addText(text, position, color, font):
    giftText = font.render(text, True, color)
    giftRect = giftText.get_rect()
    giftRect.center = position
    screen.blit(giftText, giftRect)

pageopen=0


story=parsestory()

while True:

    # Check if game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
      
    if pageopen==0:
        filename="images/output"+(f"{config.PAGES:02d}")+".jpg"     
    else:
        filename='images/output'+ (f"{pageopen:02d}") +".jpg"
        
    image = pygame.image.load(filename)
    rect = image.get_rect()
    screen.blit(image, rect)

    s = pygame.Surface((width,TEXTHEIGHT))             
    s.fill(WHITE)
    screen.blit(s, (0,HEIGHT))

    if(pageopen==0):
        addText(config.STORY, ((width / 2), (HEIGHT+(2*LINEHEIGHT))), BLACK, hugefont)   
    else:
        text=story[pageopen-1]['text']
        lines = textwrap.wrap(text, 40, break_long_words=True)
        h=HEIGHT+(2*LINEHEIGHT)
        for line in lines:
            addText(line, ((width / 2), h), BLACK, bigfont)
            h+=LINEHEIGHT
        addText('page '+str(pageopen), ((width / 2),HEIGHT+TEXTHEIGHT-LINEHEIGHT), GRAY, font)
       
    # Check if play button clicked
    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:   
        pageopen =(pageopen+1)%(config.PAGES+1)
        time.sleep(0.2)

    pygame.display.flip()
