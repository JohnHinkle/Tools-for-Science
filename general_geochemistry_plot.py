# Geochemistry Plot
# Plots geochemical data vs depth (mbsf)


from datascience import *
import numpy as np
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style
plt.style.use('seaborn-poster')
plt.rcParams.update({'font.family':'sans-serif'})

# Make sure to tidy up your csv file before working with it
# encoding = 'unicode_escape' is needed for the IODP 385 data to work. Other projects may not require this.
t = Table.read_table("tidied_IODP_data.csv", encoding = 'unicode_escape')

# Forms tables for each drilling hole (ex. 1552A, 1552B, etc.).
tA = t.where('Hole','A')
tB = t.where('Hole','B')
tC = t.where('Hole','C')
tD = t.where('Hole','D')

# In the IODP data tables, alkalinity (x-value) is formatted as a string, so it needs to be converted to a float

xA = tA.column(8).astype('float64')
yA = tA.column(5)

xB = tB.column(8).astype('float64')
yB = tB.column(5)

xC = tC.column(8).astype('float64')
yC = tC.column(5)

xD = tD.column(8).astype('float64')
yD = tD.column(5)

ax = plt.gca()

# inverts the y-axis so that zero is at the top
ax.invert_yaxis()

# Use to alter your x and y-axis values
ax.set_ylim([475,0])
ax.set_xlim([0,18])

# plots each value with a circle, connected by a dotted line
plt.plot(xA, yA,linewidth=2,linestyle='dotted', marker='o',color='goldenrod', mfc='#FFC107', label='A')
plt.plot(xB, yB,linewidth=2,linestyle='dotted', marker='o',color='lightgreen', mfc='#004D40', label='B')
plt.plot(xC, yC,linewidth=2,linestyle='dotted', marker='o',color='pink', mfc='#D81B60', label='C')
plt.plot(xD, yD,linewidth=2,linestyle='dotted', marker='o',color='skyblue', mfc='#1E88E5', label='D')

# creates the legend
plt.legend()

# Creates the title
plt.title('Site XXXX', fontname='arial', fontweight='bold', fontsize=22, y=0)

# Creates the x-axis label
plt.xlabel('Geochemistry (concentration)', fontname='helvetica')

# Creates the y-axis label, usually 'Depth (mbsf)'
plt.ylabel('Depth (mbsf)', fontname='helvetica')

# Places the x-axis label at the top
ax.xaxis.set_label_position('top')

# Places the x-axis tick marks at the top
ax.xaxis.tick_top()

# Shows the plot
plt.show()