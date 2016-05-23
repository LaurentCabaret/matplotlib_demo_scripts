#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class PlotBuilder:
    def __init__(self, couleurs, title, label_X, label_Y):
        self.xlabel = label_X.decode('utf-8')
        self.ylabel = label_Y.decode('utf-8')
        self.title = title.decode('utf-8')
        self.couleurs = couleurs
        self.colorIndex = 0
        self.plt = plt
        self.clear()


    def initPicture(self):
        textcolor = '#000000'
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['font.size'] = 34

        plt.rcParams['mathtext.fontset'] = 'cm'
        plt.rcParams['mathtext.fallback_to_cm'] = True
        plt.rcParams['mathtext.default'] = 'regular'
        plt.rcParams['mathtext.default'] = 'sf'
        

        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['lines.antialiased'] = True

        plt.rcParams['text.latex.unicode'] = True
        plt.rcParams['text.color'] = textcolor
        plt.rcParams['text.hinting'] = 'auto'
        plt.rcParams['axes.labelcolor'] = textcolor
        plt.rcParams['axes.edgecolor'] = textcolor # couleur du cadre
        plt.rcParams['axes.facecolor'] = '#FFFFFF' # couleur du fond
        plt.rcParams['ytick.major.pad'] = 8

        plt.rcParams['grid.color'] = textcolor
        plt.rcParams['grid.alpha'] = '0.9'    
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['xtick.color'] = textcolor
        plt.rcParams['ytick.color'] = textcolor
        plt.rcParams['xtick.major.size'] = 6
        plt.rcParams['ytick.major.size'] = 6
        plt.rcParams['xtick.minor.size'] = 3
        plt.rcParams['ytick.minor.size'] = 3
        plt.rcParams['legend.fancybox'] = True
        plt.rcParams['xtick.major.pad']=4
        plt.rcParams['ytick.major.pad']=12
        plt.rcParams['figure.figsize'] = 7,4
        plt.grid(True)


    def drawLabels(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        pass

    def drawTitle(self):
        plt.title(self.title)
        pass

    def plot(self, x, y):
        plt.plot(x,y, self.couleurs[self.getColor()])


    def plotSubTimes(self, laListe, nom):
        timers = plt.stackplot(x,y,y3,y1,y2, colors = sub_couleurs)
        return timers

    def save(self, filename):
            plt.savefig(filename, bbox_inches='tight')

    def getColor(self):
        if self.colorIndex > len(self.couleurs)-1:
            self.colorIndex = 0
            colorIndex = 0
        else:
            colorIndex = self.colorIndex
            self.colorIndex +=1

        return colorIndex


    def clear(self):
        plt.clf()
        self.colorIndex = 0
        yminorLocator   = MultipleLocator(5)
        xmajorLocator   = MultipleLocator(10)
        xminorLocator   = MultipleLocator(1)

        plt.axes().yaxis.set_minor_locator(yminorLocator)
        plt.axes().yaxis.set_label_position('left')
        plt.axes().xaxis.set_minor_locator(xminorLocator)
        plt.axes().xaxis.set_major_locator(xmajorLocator)
        ylabel = plt.axes().yaxis.get_label()
        ylabel.set_va('baseline')
        ylabel.set_ha('center')
        plt.grid(True)
        self.drawLabels()
        self.drawTitle()    
        pass
