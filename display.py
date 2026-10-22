class Display:

    def __init__(self, width=20, height=5):
        self.width = width
        self.height = height
        self.grid = []
        self.clear()

    def clear(self):
        self.grid = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(" ")
            self.grid.append(row)

    def set_pixel(self, x, y, char="#"):
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            self.grid[y][x] = char

    def draw_text(self, x, y, text):
        for letter in text:
            self.set_pixel(x, y, letter)
            x = x + 1

    def show(self):
        border = "~" * (self.width + 2)
        print(border)
        for row in self.grid:
            line = ""
            for char in row:
                line = line + char
            print("I" + line + "I")
        print(border)