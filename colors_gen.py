
def col_map(col):
    return round(col * 255 / 7)
if __name__ == "__main__":
    with open("col512.txt", "w") as f:
        f.write("512\n") # total number of colors
        for blue in range(8):
            for green in range(8):
                for red in range(8):
                    red_map = col_map(red)
                    green_map = col_map(green)
                    blue_map = col_map(blue)
                    f.write(f"{red_map} {green_map} {blue_map}\n")