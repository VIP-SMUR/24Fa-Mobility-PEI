import requests
import addfips as af
import geopandas as gpd
from shapely.geometry import shape

# Create an AddFIPS object for converting state or county names to FIPS codes
af = af.AddFIPS()

def get_blockgroup_tract_area(state_fips, county_fips):

    # Convert county name to FIPS code if passed as a string
    if isinstance(county_fips, str):
        county_fips = int(af.get_county_fips(county_fips, state_fips)[-3:])
    # Convert state name to FIPS code if passed as a string
    if isinstance(state_fips, str):
        state_fips = int(af.get_state_fips(state_fips))

    # Define the API endpoint and parameters for querying census tracts
    base_url = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer/8/query"
    params = {
        "where": f"STATE='{state_fips}' AND COUNTY='{county_fips}'",
        "outFields": "GEOID",
        "outSR": "4326",
        "f": "geojson"
    }

    # Make the API call to retrieve census tract data
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract geometries and GEOIDs from the response, and create a GeoDataFrame
    geometries = [shape(feature['geometry']) for feature in data['features']]
    geo_ids = [feature['properties']['GEOID'] for feature in data['features']]
    gdf = gpd.GeoDataFrame({'GEOID': geo_ids, 'geometry': geometries})

    # Store the geometry coordinates for each census tract
    polygons = gdf['geometry']

    # Project the GeoDataFrame from EPSG 4326 to EPSG 3857 to calculate area in square meters. Like magic
    gdf.crs = "EPSG:4326"
    gdf = gdf.to_crs("EPSG:3857")
    gdf['area'] = gdf.area / 10**6  # Convert area from square meters to square kilometers

    # Create a new GeoDataFrame with GEOID, area in square kilometers, and coordinates of the polygon vertices
    blockgroup_area_gdf = gpd.GeoDataFrame({
        'GEOID': gdf['GEOID'],
        'Area': gdf['area'],
        'Polygons': polygons
    })

    return blockgroup_area_gdf
