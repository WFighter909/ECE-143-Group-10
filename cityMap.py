#!/usr/bin/env python
# coding: utf-8

# In[1]:
'''
Generate city distribution on the map of the United States
'''

import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
plt.figure(figsize=(20,23))
m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution='l')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')

cities = ['Seattle','San Francisco','Los Angeles',
                   'San Diego',
                   'Boston',
                   'New York City',
                   'Washington DC']

# Get the location of each city and plot it
geolocator = Nominatim()
for city in cities:
    loc = geolocator.geocode(city)
    x, y = m(loc.longitude, loc.latitude)
    m.plot(x, y, 'r*', markersize=15)
    plt.text(x+3000, y, city,fontsize=30)

plt.savefig('citymap')
plt.show()


# In[ ]:




