import random

# Color Constants
# Color RGB Chart  https://www.rapidtables.com/web/color/RGB_Color.html
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (224, 224, 224)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
