.PHONY: make

make:
	make clean
	mkdir tmp
	curl -L https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz --output tmp/flowers.tgz
	curl -L https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz --output tmp/dogs.tar.gz
	tar -zxvf tmp/dogs.tar.gz -C tmp/
	tar -zxvf tmp/flowers.tgz -C tmp/
	cp tmp/jpg/* images/
	cp tmp/images/* images/
	rm -rf tmp
	./rename.sh
	./generate_palettes.sh
	
.PHONY: clean

clean:
	rm -rf images
	rm -rf palettes
	mkdir images
	mkdir palettes
