import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure,show
x=np.linspace(0,10,100)
y=np.sin(x)
Tools="pan,wheel_zoom,box_zoom,reset,save,box_select"
p1=figure(title="Varsha HA-1KI23CS175",tools=Tools)
p1.line(x,y,line_width=2,legend_label="sin(x)",color="red")
p1.line(x,2*y,line_width=2,legend_label="2sin(x)",color="blue")
p1.legend.title="Marker"
show(gridplot([p1],ncols=1,width=500,height=500))