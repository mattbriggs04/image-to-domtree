from PIL import Image
import sys

class DOMNode:
    def __init__(self, id, layout_dir, margin=0.0):
        self.id = id
        self.layout_dir = layout_dir
        self.margin = margin
        self.children = []

    def __str__(self):
        s = f"({self.id} {self.layout_dir} {self.margin:.2f}"
        for child in self.children:
            s += " " + str(child) # recursion baby
        s += ")"
        return s

def build_color_map():
    cols = []
    for col in range(8):
        cols.append(round(col * 255 / 7))
    return cols

def nearest_idx(col):
    return round(col * 7 / 255)

def color_to_id(r, g, b):
    r_id = nearest_idx(r)
    g_id = nearest_idx(g)
    b_id = nearest_idx(b)
    return b_id * 64 + g_id * 8 + r_id

def build_dom_tree(img):
    width, height = img.size
    print(f"Processing image of size {width}x{height} px")
    pxcol_map = img.load()
    node_id = 0

    # vertically stack a number of nodes = height of pixels and horizontally stack number of nodes = width of pixels
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
    if len(sys.argv) != 3:
        print("Usage: python3 parser.py <bmpfile> <outfile>")
        sys.exit(1)
    path, outfilename = sys.argv[1], str(sys.argv[2])

    # load and convert to rgb
    img = Image.open(path).convert("RGB")

    # build tree and print out 
    tree = build_dom_tree(img)
    with open(outfilename, "w") as f:
        f.write(str(tree))

if __name__ == '__main__':
    main()
