#!/bin/bash
rm images/*.mat
N=1
for FILE in $(ls "images/")
do
	#magick convert "images/$FILE" -gravity Center -crop 256x256+0+0 +repage "images/image-$N.png"
	magick convert "images/$FILE" -resize 128x128\! "images/image-$N.png"
	rm "images/$FILE"
	((N=N+1))
done
