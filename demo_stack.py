#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'laurent'

import math
from Plotter.StackBuilder import StackBuilder
from Plotter.PlotBuilder import PlotBuilder

X = [x * 0.1 for x in range(0, 1000)]
Y = []
Y2 = []
Y3 = []
for abscisse in X: 
    Y.append(0.2+0.06*math.sin(2 * 3.14159 * abscisse/10))
    Y2.append(0.1*math.log(2 * 3.14159 * abscisse/10+ 1))
    Y3.append(0.1+0.07*math.sin(2 * 3.14159 * abscisse/33))


plotter = PlotBuilder(["red"], "Légende", "X", "Y")
plotter.plot(X, Y)
plotter.plt.xlim(0,100) # set the X limits
plotter.plt.ylim(0,1.32) # set the Y limits
plotter.save("produced/demo_simple_plot.pdf")


plotter2 = StackBuilder(["red", "blue", "#CAFE01", "#CA01FE", "#01CAFE"], "Légende", "X", "Y")
plotter2.add_X(X)
plotter2.add_Y(Y)
plotter2.add_Y(Y2)
plotter2.add_Y(Y3)
plotter2.plot()
plotter2.save("produced/demo_stack_plot.pdf")