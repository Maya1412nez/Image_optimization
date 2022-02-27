import pygame
from PIL import Image

image = Image.open('image/Image.png')

# pyuic5 interface1.ui -o interface1.py
img = Image.open('image/Image.png')

if img.mode == "RGB":
    a_channel = Image.new('L', img.size, 255)   # 'L' 8-bit pixels, black and white
    img.putalpha(a_channel)

pixels = img.load()
width, height = img.size
count = 0

for pix_x in range(width):
    for pix_y in range(height):
        count += 1

print(count)

if __name__ == '__main__':
    pygame.init()
    size = 1000, 800
    screen = pygame.display.set_mode(size)
    screen.fill("green")

    gg_image = pygame.image.load('image/Image.png')
    gg_image_rect = gg_image.get_rect()

    print(1)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

