"""import geopandas as gpd
import osmnx as ox
data = gpd.read_file("/Users/ACER/Desktop/VIP_IDI/TAZ_Chicago.geojson")
filtered_data = data[data['chicago'] == 1]
print((filtered_data))
mission_shape=filtered_data.geometry[0]
G = ox.graph_from_polygon(mission_shape, network_type='walk')
ox.plot_graph(G)"""

import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
data = gpd.read_file("/Users/ACER/Desktop/VIP_IDI/TAZ_Chicago.geojson")
filtered_data = data[data['chicago'] == 1]
polygons_box=[[(x,y) for x, y in i.exterior.coords] for i in filtered_data["geometry"]]
polygons=[ i for i in filtered_data["geometry"]]
area=[i for i in filtered_data["Shape__Area"]]
num=[0]*len(area)
for i in range(len(polygons)):
    print(i)
    sum=0
    graph=G = ox.graph_from_polygon(polygons[i], network_type='walk')
    for node in graph.nodes():
        sum= sum+len(list(graph.neighbors(node)))
    num[i]=sum/area[i]

maxi=max(num)
IDI= [value / maxi for value in num]

norm = Normalize(vmin=min(IDI), vmax = max(IDI))
cmap = plt.cm.get_cmap('Purples')

sm = ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])

G = ox.graph_from_place('chicago')

fig, ax = ox.plot_graph(G, show=False, close=False)

for i in range(len(polygons_box)):
    poly = plt.Polygon(polygons_box[i], edgecolor='r', alpha=1,facecolor=cmap(norm(IDI[i])))  # Red polygon with transparency
    ax.add_patch(poly)

cbar = plt.colorbar(sm)
cbar.set_label('IDI')
plt.show()


