# Student Name: Deniz Güneş
# Author Name : Ayca Tuzmen, Sasan Asadiabadi


# import libraries here
from matplotlib import pyplot as plt
import numpy as np
######## part a #########

def draw_function(tuples_list):
    """
    This function receives a list of tuples and plot them in a figure (No return object)
    input: a list of tuples [(x1,y1), (x2,y2), ...]
    input2: plot_style, dictionary of plot configurations
    """
    ###### Write you code here ######
    style = input('Please enter color, linestyle, linewidth, label, xlabel, ylabel  preferences: ')
    lst = style.split(',')
    color = lst[0]
    lnstyle = lst[1]
    lnwidth = int(lst[2])
    lbl = lst[3]
    xlbl = lst[4]
    ylbl = lst[5]
    x_coords = []
    y_coords = []
    for i in range(len(tuples_list)):
        temp = tuples_list[i]
        x = int(temp[0])
        y = int(temp[1])
        x_coords.append(x)
        y_coords.append(y)
    plt.plot(x_coords, y_coords, color=color, label=lbl, linestyle=lnstyle, linewidth=lnwidth)
    plt.title(lbl)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid('whitegrid')
    plt.legend(loc='upper left')
    plt.show()
    #################################


######## part b #########
def draw_from_file():
    """
    plots function in the given sample.txt file, using the function in part a.
    1. open and read file to a list of tuples.
    2. call draw_function()
    """
    #To obtain the plot in the example enter this: g,dotted,2,graph,x,y
    ###### Write you code here ######
    filename = 'sample.txt'
    firstrow = True
    x = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            if firstrow:
                firstrow = False
            else:
                split_line = line.split(',')
                x.append(split_line[0])
                y.append(split_line[1].rstrip('\n'))
    make_tuple = []
    for i in range(0, len(x)):
        temp = (x[i], y[i])
        make_tuple.append(temp)

    draw_function(make_tuple)
    #################################


######## part c #########
def draw_exp():
    """
    plots exponential function in the given range, using the function in part a.
    1. create a list of (x, y) tuples in the given range (you can only use integers,)
    2. call draw_function()
    """
    #to obtain the plot in the example enter: r,--,3,y=exp(-x^3),x,y
    ###### Write you code here ######

    lst = [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
    x = []
    y = []

    for i in range(len(lst)):
        temp = lst[i]
        x.append(temp[0])
        y.append(np.exp(int(temp[0]) * -3))

    make_tuple = []
    for i in range(0, len(x)):
        temp = (x[i], y[i])
        make_tuple.append(temp)

    draw_function(make_tuple)

    #################################


if __name__ == '__main__':
    draw_from_file()
    draw_exp()
