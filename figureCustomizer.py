import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
import matplotlib as mpl
from cycler import cycler

# Source : https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams


def set_pub():
    plt.rcdefaults()  # restores defaults

    # COLORS
    rcParams['figure.facecolor'] = 'white'
    rcParams['axes.facecolor'] = 'white'
    rcParams['savefig.facecolor'] = 'white'
    rcParams['axes.labelcolor'] = 'black'
    rcParams['grid.color'] = 'black'
    rcParams['legend.edgecolor'] = 'black'
    rcParams['axes.prop_cycle'] = cycler('color',
                                         ['red',
                                          'blue',
                                          'black',
                                          'magenta',
                                          '#a6cee3',
                                          '#1f78b4',
                                          '#b2df8a',
                                          '#33a02c',
                                          '#fb9a99',
                                          '#e31a1c',
                                          '#fdbf6f',
                                          '#ff7f00',
                                          '#cab2d6',
                                          '#6a3d9a',
                                          '#ffff99',
                                          '#b15928'])
    rcParams['grid.color'] = 'black'
    rcParams['grid.alpha'] = 0.15

    # TEXT
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Arial']
    rcParams['axes.titlesize'] = 16
    rcParams['axes.labelsize'] = 14
    rcParams['legend.fontsize'] = 10
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['text.usetex'] = False
    rcParams['axes.unicode_minus'] = False
    rcParams['pgf.preamble'] = '\n'.join([r'\usepackage{lmodern}',
                                          r'\usepackage[T1]{fontenc}',
                                          r'\usepackage[utf8]{inputenc}',
                                          r'\usepackage[detect-all,output-decimal-marker={,}]{siunitx}',
                                          r'\usepackage{icomma}',
                                          ])

    # GRIDS AND GRAPHICS
    rcParams['lines.linewidth'] = 3.0
    rcParams['axes.linewidth'] = 1.0
    rcParams['grid.linewidth'] = 0.5
    rcParams['axes.grid'] = True
    rcParams['xtick.top'] = True
    rcParams['xtick.direction'] = 'in'
    rcParams['xtick.major.size'] = 6
    rcParams['ytick.right'] = True
    rcParams['ytick.direction'] = 'in'
    rcParams['ytick.major.size'] = 6
    rcParams['xtick.major.width'] = rcParams['grid.linewidth']
    rcParams['ytick.major.width'] = rcParams['grid.linewidth']


set_pub()
