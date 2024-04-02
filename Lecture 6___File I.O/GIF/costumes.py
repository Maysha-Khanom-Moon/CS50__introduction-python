# to access the command line arguments
import sys

# pip install Pillow
# PIL: Python Imaging Library
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# python costumes.py costume1.gif costume2.gif
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)