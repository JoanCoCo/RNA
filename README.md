# Palette Corpus
Corpus created for the task of obatining the color palette from an image.

## Characteristics
Corpus formed by 15579 images and their associated color palettes of size 8. 
* The images are sized to 128 by 128 and they don't conserve its original aspect ratio. Therefore, they are distorted.
* The palettes are saved in image form, being images of 8 by 1. These palettes correspond to the means obtained when clustering the pixels of the images in eight groups by the conventional c-means algorithm.

## Structure
The source images are stored in the folder `corpus/images` following the naming convention `image-{n}.png` where n is in the range \[1, 15579\].

The palettes are stored in the folder `corpus/palettes` following the naming convention `palette-{n}.png` where n is in the range \[1, 15579\] and means that this palette corresponds to the image `image-{n}.png`.

## Sources
This corpus was created from the images provided by:
* [102 Category Flower Dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html)
* [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)

The palettes were obtained using the `Makefile` located in the `corpus` folder. By performing `$ make` on this folder, the source images are downloaded, scaled to 128 by 128 and analyzed to obtain their palettes. The palettes are stored as images.

## Requirements
For being able to regenerate this corpus, it's required:
* macOS 12.0 or higher (Intel)
* [magick](https://imagemagick.org)
