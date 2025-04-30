# Generates a color file with num_discrete evenly spaced numbers from 0-255
# and all combination therein (num_discrete^3 lines)
def generate_color_file(num_discrete=8):
    if not (0 <= num_discrete <= 255):
        print("Invalid number of discrete colors for color file")
        return None
    
    def map_color(col):
        return round(col * 255 / (num_discrete-1))
    
    with open(f"colors-{num_discrete**3}.txt", "w") as f:
        f.write(f"{num_discrete ** 3}\n")
        for blue in range(num_discrete):
            for green in range(num_discrete):
                for red in range(num_discrete):
                    f.write(f"{map_color(red)} {map_color(green)} {map_color(blue)}\n")

if __name__ == "__main__":
    generate_color_file()
