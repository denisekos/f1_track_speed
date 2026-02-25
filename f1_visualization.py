import matplotlib as mpl
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import fastf1 as ff1

# ---------------------------------
# PARAMETERS 
# Driver: Lewis Hamilton
# Race: Spanish Grand Prix
# Season: 2025
# Round: 9th race of the season
# Focus: Fastest lap analysis
# ---------------------------------
year = 2025 
wknd = 9 
ses = 'R'
driver = 'HAM'
colormap = mpl.cm.plasma

# load session 
session = ff1.get_session(year, wknd, ses)
session.load()
weekend = session.event

# pick fastest lap for the driver 
lap = session.laps.pick_drivers(driver).pick_fastest()

# get telemetry data
tel = lap.get_telemetry()
x = tel['X']
y = tel['Y']
speed = tel['Speed']

# create line segments for coloring
points = np.array([x, y]).T.reshape(-1, 1, 2)                   # shape (N, 1, 2) 
segments = np.concatenate([points[:-1], points[1:]], axis=1)    # shape (N-1, 2, 2)

# create plot 
fig, ax = plt.subplots(figsize=(12, 6.75))
fig.suptitle(f'Race {weekend.name} {year} - {driver} - Speed', size=24, y=0.97)

# plot background track line 
ax.plot(x, y, color='black', linestyle='-', linewidth=16, zorder=0)

# create line collection for colored track 
norm = plt.Normalize(speed.min(), speed.max())
lc = LineCollection(segments, cmap=colormap, norm=norm, linestyle='-', linewidth=5)
lc.set_array(speed)
ax.add_collection(lc)

# color bar 
cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])  # x, y, width, height
normlegend = mpl.colors.Normalize(vmin=speed.min(), vmax=speed.max())
mpl.colorbar.ColorbarBase(cbaxes, norm=normlegend, cmap=colormap, orientation='horizontal', label='Speed (km/h)')

# adjust plot 
ax.axis('off')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)
plt.show()