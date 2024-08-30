import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import numpy as np
from shapely.geometry import Polygon
import pyproj

data = gpd.read_file("/Users/ACER/Desktop/VIP_IDI/TAZ_Chicago.geojson")
data_projected=data.to_crs(epsg=26916)
proj = data_projected[data_projected['chicago'] == 1]
filtered_data = data[data['chicago'] == 1]
polygons_box=[[(x,y) for x, y in i.exterior.coords] for i in filtered_data["geometry"]]
polygons=[ i for i in filtered_data["geometry"]]
area=[i.area for i in proj["geometry"]]
E=[0]*len(area)

for i in range(len(polygons[:])):
    print("pol area",area[i])
    try:
        gdf= ox.features.features_from_polygon(polygons[i], tags = {'landuse': True})
    except:
        continue    
    gdf.reset_index(inplace=True)
    gdf = gdf.to_crs(epsg=26916)
    gdf["area"] = gdf.geometry.area
    landuse_area_dict = gdf.groupby('landuse')['area'].sum().to_dict()
    landuse_area_dict = {k: v for k, v in landuse_area_dict.items() if v != 0}
    

    k = len(landuse_area_dict)
    print("dict:",landuse_area_dict)
    if (k>1):
        denominator =  np.log(k)
        numerator = 0
        for j in landuse_area_dict.keys():
            p = landuse_area_dict[j]/sum(landuse_area_dict.values())
            numerator +=  p*np.log(p)
        print("num:",numerator)
        print("deno:",denominator)
        E[i]= -1*numerator/denominator
        print("val",E[i])
    else:
        E[i]=0
    print(i)
print(E)