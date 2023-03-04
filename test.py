import pyqtgraph as pg


pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


graph = pg.PlotWidget()

## The following plot has inverted colors
graph.plot([1,4,2,3,5])