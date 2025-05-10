# Image to DOMTree - ECE 26400 HW 14
Feel free to download or clone this repository and use it to convert images into the expected format for your homework 14 solution to convert.

### Examples -- Explaining the parameters
The format of calling the parser is:
```
python3 parser.py images/[image] output/[output-file] [optional: num-discrete-colors]
```
This will generate an output file at the given output destination and also generate a *colors-X.txt* file in the colors folder.

The number of discrete colors option is used for the creation of the colors file, with a default value of 8. This number effectively is used to compress the number of possible colors. This is done because using all 255 color possibilites, for the three colors (RGB), results in X = 255^3 = very large *colors* file (many MB). Using a smaller value like 16 will approximate many of the colors, but use a much smaller colors file (16^3 = 4096 total lines), and a file named *colors-4096.txt* would be generated. See `colors_gen.py` for how this works.
