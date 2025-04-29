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
            s += " " + str(child) # recursive call
        s += ")"
        return s

def build_dom_tree(img):
    width, height = img.size
    black_threshold = 255 // 2
    pxcol_map = img.load()
    node_id = 0
    odd_id = 1
    even_id = 0

    root = DOMNode(even_id, 'vert', 0.0)
    even_id += 2
    for y in range(height):
        row_node = DOMNode(odd_id, 'horiz', 0.0)
        odd_id += 2
        x = 0

        while x < width:
            is_black = pxcol_map[x, y] < black_threshold
            if is_black:
                node_id = odd_id
                odd_id += 2
            else:
                node_id = even_id
                even_id += 2

            # continually add to rectangle until different color is met
            while x < width and (pxcol_map[x, y] < black_threshold) == is_black:
                x += 1

            pixel_node = DOMNode(node_id, 'none', 0.0)
            
            row_node.children.append(pixel_node)
        
        if row_node.children:
            root.children.append(row_node)
                 
    return root

def main():
    # parse args
    if len(sys.argv) != 4:
        print("Usage: python parser.py <bmp-file> <width> <height>")
        sys.exit(1)
    path, exp_w, exp_h = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    # load and convert to grayscale
    img = Image.open(path).convert('L')

    # ensure dimensions match
    if img.size != (exp_w, exp_h):
        print(f"Image size mismatch {img.size} != {exp_w,exp_h}")

    # build tree and print out 
    tree = build_dom_tree(img)
    with open("qr_code.txt", "w") as f:
        f.write(str(tree))

if __name__ == '__main__':
    main()
