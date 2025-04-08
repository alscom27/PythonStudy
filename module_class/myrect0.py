xpos, ypos = 0, 0


def get_area(width, height):
    area = width * height
    return area


def get_peri(width, height):
    peri = 2 * (width + height)
    return peri


def set_pos(x, y):
    global xpos, ypos
    xpos, ypos = x, y
