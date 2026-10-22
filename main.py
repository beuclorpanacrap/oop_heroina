from display import Display

screen = Display()   
screen.draw_text(4, 2, "let me out")
screen.set_pixel(0, 0)
screen.set_pixel(19, 4)
screen.show()
screen.clear()
screen.draw_text(3, 2, "pretty please")
screen.show()