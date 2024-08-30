import geopandas as gpd
import osmnx as ox
import addfips as af
import matplotlib.pyplot as plt
from census_tract_area_calculator import get_blockgroup_area
from census_blockgroup_population_retriever import get_blockgroup_population

# Input for state and county name
state_name = input("Enter a state name or abbreviation: ")
county_name = input("Enter a county name: ")

# Create addFIPS object to convert names of state/county to FIPS code
af = af.AddFIPS()

# Converts string names of state/county to FIPS code
state_fips = int(af.get_state_fips(state_name))
county_fips = int(af.get_county_fips(county_name,state_name)[-3:])

# Get populatiop data for blockgroups
blockgroup_population_gdf = get_blockgroup_population(state_fips, county_fips)

# Get area and polygons for blockgroups
blockgroup_area_gdf = get_blockgroup_area(state_fips, county_fips)

# Merge gdfs for population and area
blockgroup_gdf = blockgroup_population_gdf.merge(blockgroup_area_gdf, on='GEOID', how='left')
blockgroup_gdf = blockgroup_gdf.set_geometry('geometry')

# Create population density column
blockgroup_gdf['Population Density'] = blockgroup_gdf['population'] / blockgroup_gdf['area']


# Normalize the population density values for color mapping
# This will scale the densities to a range between 0 and 1
blockgroup_gdf['Normalized Population Density'] = (blockgroup_gdf['Population Density'] - blockgroup_gdf['Population Density'].min()) / \
(blockgroup_gdf['Population Density'].max() - blockgroup_gdf['Population Density'].min())

print(blockgroup_gdf)

fig, ax = plt.subplots(figsize=(10, 10))
blockgroup_gdf.plot(ax=ax, column='Population Density', cmap='plasma', legend=True)
ax.set_title(f'Census Block Groups by Population Density: {county_name}, {state_name}')
plt.show()
