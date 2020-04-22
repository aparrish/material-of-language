import random
from bezmerizing import Polyline
from flat import document, shape, rgb, rgba
from numpy.random import uniform, normal, choice
from scipy.stats import truncnorm

def t_normal(a, b, mu, sigma):
    tn = truncnorm((a-mu)/sigma, (b-mu)/sigma, loc=mu, scale=sigma)
    return tn.rvs(1)[0]
  
def make_scribble(width, height, steps, stddev=0):
    pts = []
    for i in range(steps):
        x = ((width / steps) * i) + normal(0, stddev)
        y = normal(0, height)
        pts.append([x, y])
    return Polyline(pts)

size = 200
d = document(size, size, 'mm')
page = d.addpage()
curve_figure = shape().stroke(rgba(0, 0, 0, 255)).width(2)
row_n = 16
for i in range(row_n):
    scribble_poly = make_scribble(
                        width=size-20,
                        height=(size/row_n)*0.25,
                        steps=int(uniform(25, 250)),
                        stddev=uniform(2))
    scribble_poly_tr = scribble_poly.translate(
        10, 10 + (i*size/(row_n+1)))
    curve = curve_figure.path(scribble_poly_tr.smooth_path(tightness=-0.5))
    page.place(curve)

with open("scribble.svg", "wb") as fh:
    fh.write(page.svg())

