import tkinter
from tkinter import *


def create_circle_center(self, x, y, r, **kwargs):
    kwargs = {'width': '20', 'fill': ''} | kwargs
    return self.create_oval(x-r, y-r, x+r, y+r,
                            width=kwargs.get('width'),
                            fill=kwargs.get('fill'))


def create_circle_center_ul(self, x, y, r, **kwargs):
    kwargs = {'width': '0', 'fill': ''} | kwargs
    return self.create_oval(x, y, x+r+r, y+r+r,
                            width=kwargs.get('width'),
                            fill=kwargs.get('fill'))


def rgb_to_hex_color(rgb):
    r, g, b = rgb  # translates an rgb tuple of int to a tkinter friendly color code
    return f'#{r:02x}{g:02x}{b:02x}'


# Canvas.create_circle_center = create_circle_center
# Canvas.create_circle_center_ul = create_circle_center_ul
tkinter.Canvas.create_circle_center = create_circle_center
tkinter.Canvas.create_circle_center_ul = create_circle_center_ul
