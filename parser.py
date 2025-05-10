from PIL import Image
from colors_gen import generate_color_file
import sys

# The number of discrete possible colors in the range [0, 255]
# For example, if the num is 4, the colors would be {0, 85, 170, 255} for red, green, and blue
NUM_DISCRETE_COLORS=8

class DOMNode:
    def __init__(self, id, layout_dir, margin=0.0):
        self.id = id
        self.layout_dir = layout_dir
        self.margin = margin
        self.children = []

    def __str__(self):
        # margin should always be 0, .0f is used in order to save the 3 bytes from the ".00" (actually a big optimization ngl)
        s = f"({self.id} {self.layout_dir} {self.margin:.0f}" 
        for child in self.children:
            s += " " + str(child) # recursion baby
        s += ")"
        return s

def color_to_id(r, g, b):

    def nearest_idx(col):
        return round(col * (NUM_DISCRETE_COLORS-1) / 255)
    
    r_id = nearest_idx(r)
    g_id = nearest_idx(g)
    b_id = nearest_idx(b)
    return b_id * (NUM_DISCRETE_COLORS ** 2) + g_id * NUM_DISCRETE_COLORS + r_id

def build_dom_tree(img):
    width, height = img.size
    print(f"Processing image of size {width}x{height} px")
    pxcol_map = img.load()
    node_id = 0

    # vertically stack a number of nodes = height of pixels 
    # and horizontally stack number of nodes = width of pixels
    root = DOMNode(node_id, 'vert', 0.0)
    for y in range(height):
        row_node = DOMNode(node_id, 'horiz', 0.0)

        for x in range(width):
            r, g, b = pxcol_map[x, y]
            node_id = color_to_id(r, g, b)

            pixel_node = DOMNode(node_id, 'none', 0.0)

            row_node.children.append(pixel_node)
        
        if row_node.children:
            root.children.append(row_node)
                 
    return root

def main():
    # parse args
    if len(sys.argv) not in (3, 4):
        print("Usage: python3 parser.py <bmp file> <output file> <?num_discrete for color file>")
        sys.exit(1)
    
    if len(sys.argv) == 4:
        # "but convention is that uppercase is constant" -- it's python and idc
        global NUM_DISCRETE_COLORS
        NUM_DISCRETE_COLORS=int(sys.argv[3])
        generate_color_file(int(sys.argv[3]))

    path, outfilename = sys.argv[1], str(sys.argv[2])
    # load and convert to rgb
    img = Image.open(path).convert("RGB")

    # build tree and print out to file
    tree = build_dom_tree(img)
    with open(outfilename, "w") as f:
        print(f"Generating tree file {outfilename}")
        f.write(str(tree))

if __name__ == '__main__':
    main()
