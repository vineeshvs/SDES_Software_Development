import sys

def _make_canvas(size):
    global canvas
    cols, rows = size
    canvas = []
    for i in range(0, rows):
        canvas.append(list(' '*cols))
        return canvas

def plot_canvas(canvas, output_file):
    for line in canvas:
        output_file.write(''.join(line))
        output_file.write('\n')

def map_point(x, y, xmin, ymin, xmax, ymax):
    """ Return  pair of in the range (0,1) correspoinding to the point x, y in the domain (xmin,...)
    """
    len_x = float(xmax - xmin)
    len_y = float(ymax - ymin)
    xi = int (round((x - xmin) / len_x * size[1] ))
    yi = int (round( (y - ymin) / len_y * size[0] ))
    return xi, yi

def plot(x_a, y_a, size = (80,30), output_file = sys.stdout):
    if len(x_a) != len(y_a):
        raise PlotException("Inconsistent input arrays") 
    xmin, xmax = min(x_a), max(x_a)
    ymin, ymax = min(y_a), max(y_a) 
    canvas = make_canvas (size)
    n = len(x_a)
    for i in range(nx):
        x, y = x_a[i], y_a[i]
        xi, yi = map_point (x, y, xmin, ymin, xmax, ymax, size)
        canvas[yi][xi]= '*'

def test_make_canvas():
    size = (6,5)
    canvas = make_canvas(size)
    assert len(canvas)== size[1]
    assert len(canvas)== size[1]
    assert len(canvas)== size[1]
    assert len(canvas)== size[1]
    #canvas = 

def test_plot():
    x = [0, 1]
    y = [3, 4]
    plt.plot (x,y)

def main():
    import numpy as np
    x = np.linspace(0,2*np.pi, 20)
    plot (x, np.sin(x), size=(20,20))

#if __name__ = '__main__'
