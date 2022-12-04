from PIL import Image
import numpy as np

# Create a function to convert an image to ASCII art
def img_to_ascii(img_file):
  # Load the image and convert it to grayscale
  img = Image.open(img_file).convert('L')

  # Create a matrix of pixel values
  pixels = np.asarray(img)

  # Map each pixel to an ASCII character
  chars = '@B%8WM#*oahkbdpwmZO0QJLXNcrsvxn...'  # List of characters sorted by visual intensity
  ascii_img = ''
  for row in pixels:
    for pixel in row:
      ascii_img += chars[pixel//25]
    ascii_img += '\n'

  # Return the ASCII art
  return ascii_img

# Get the input image file
img_file = input('Enter the image file to convert: ')

# Convert the image to ASCII art
ascii_img = img_to_ascii(img_file)

# Output the ASCII art to a text file
with open('ascii_img.txt', 'w') as f:
  f.write(ascii_img)