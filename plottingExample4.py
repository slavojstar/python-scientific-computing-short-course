from mpl_toolkits.basemap import Basemap
from matplotlib.pyplot import *

m = Basemap(projection='merc', llcrnrlat=-10, urcrnrlat=80,
           llcrnrlon=-140, urcrnrlon=100, lat_ts=40,
           resolution='h', area_thresh=10000)

m.drawcoastlines()
m.drawcountries()
m.fillcontinents()

(ny_lat, ny_lon) = (40.6397, -73.7789)
(lon_lat, lon_lon) = (51.4775, 0.4614)
m.drawgreatcircle(lon_lon, lon_lat, ny_lon, ny_lat, linewidth=3)
savefig("greatcircle.pdf")