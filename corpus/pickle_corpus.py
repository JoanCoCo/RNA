import numpy as np
import pickle
import random
from PIL import Image
random.seed(37)

indices = [x for x in range(1, 15580)]
random.shuffle(indices)

image_shape = (256, 256, 3)
images_set = []
palettes_set = []

for i in indices:
    image = np.array(Image.open('images/image-' + str(i) + '.png'))
    if image.shape == image_shape:
        palette = np.array(Image.open('palettes/palette-' + str(i) + '.png'))
        images_set.append(image)
        palettes_set.append(palette)
images = np.array(images_set)
palettes = np.array(palettes_set)

print(images.shape)
print(palettes.shape)

