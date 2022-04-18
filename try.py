width = 3
height = 5
image_matrix = [[0 for i in range(width)] for j in range(height)]
for i in range(height):
    for j in range(width):
        print(image_matrix[i][j], end='')
    print()

# self.image_matrix = [[0 for i in range(self.width)] for j in range(self.height)]
#         for i in range(self.height):
#             for j in range(self.width):
#                 r, g, b = self.pixels[i, j]
#                 if r != 118 and g != 255 and b != 97:  # if pix not green = if pix != None
#                     self.image_matrix[i][j] = 1
#         print(self.image_matrix)
#         self.image.save('aaaa.png')