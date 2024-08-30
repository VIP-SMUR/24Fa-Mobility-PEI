import os
import geopandas as gpd
import addfips as af
from census import Census
from census_tract_area_calculator import get_blockgroup_area

# Create an AddFIPS object for converting state or county names to FIPS codes
af = af.AddFIPS()

def get_blockgroup_population(state_fips, county_fips, census_api_key=""):

    # Check for the census API key. First, look in the census_api_key parameter, then in the 'census_api_key.txt' file in the current directory
    if not census_api_key and os.path.exists("census_api_key.txt"):
        # Read the API key from the file
        with open("census_api_key.txt", "r") as file:
            census_api_key = file.read().strip()
    elif not census_api_key:
        raise ValueError("No API key was provided, and the 'census_api_key.txt' file is not found or empty. Please provide a valid API key.")

    # Convert county name to FIPS code if passed as a string
    if isinstance(county_fips, str):
        county_fips = int(af.get_county_fips(county_fips, state_fips)[-3:])
    # Convert state name to FIPS code if passed as a string
    if isinstance(state_fips, str):
        state_fips = int(af.get_state_fips(state_fips))

    # Initialize the Census API with the provided key
    c = Census(census_api_key)

    # Retrieve census data by block group for the specified state and county
    # B01003_001E: Total population
    census_data_state_county = c.acs5.state_county_blockgroup('B01003_001E', state_fips, county_fips, Census.ALL)

    # Convert the list of dictionaries into a GeoDataFrame
    census_df = gpd.GeoDataFrame(census_data_state_county)

    # Create the 'GEOID' column by concatenating the 'state', 'county', 'tract', and 'block group' fields
    census_df['GEOID'] = census_df['state'] + census_df['county'] + census_df['tract'] + census_df['block group']

    # Rename the 'B01003_001E' column to 'Population'
    census_df.rename(columns={'B01003_001E': 'Population'}, inplace=True)

    # Uncomment the following lines if you want to calculate and include population density
    # Get area data by tract
    # area_df = get_blockgroup_area(state_fips, county_fips)
    # census_df = census_df.merge(area_df, on='GEOID', how='left')

    # Create population density column
    # census_df['Population Density'] = census_df['Population'] / census_df['Area']

    return census_df

