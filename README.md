# Image to DOMTree - ECE 26400 HW 14
Feel free to download or clone this repository and use it to convert images into the expected format for your homework 14 solution to convert.

### Examples -- Explaining the parameters
The format of calling the parser is:
```
python3 parser.py images/[image] output/[output-file] [optional: num-discrete-colors]
```
The number of discrete colors option is used for the creation of the colors file. This number effectively is used to compress the number of possible colors. This is done because using all 255 color possibilites, for the three colors (RGB), results in 255^3 = very large *colors* file. Using a smaller value like 16 will approximate many of the colors, but use a much smaller colors file
