### get_blockgroup_population Function

#### Description

This function retrieves the population data for each block group within the given geographic areas from the U.S. Census Bureau's API and merges it with an existing GeoDataFrame containing block group geometries. The result includes added columns for population density and PDI (normalized population density relative to the maximum value in the dataset).

#### Parameters

- **census_gdf** (`GeoDataFrame`): A GeoDataFrame that must contain the block groups' geometries and the FIPS codes for the state and counties.
- **census_api_key** (`str`, optional): The API key for accessing the U.S. Census Bureau data. If not provided, the function will attempt to read it from a local file named `census_api_key.txt`. Census API keys may be generated at https://api.census.gov/data/key_signup.html.

#### Returns

- **GeoDataFrame**: The original GeoDataFrame is returned with additional columns:
  - `POP`: Population of the block group.
  - `POPDENSITY`: Population density of the block group in persons per square kilometer.
  - `NORMPOPDENSITY`: Normalized population density scaled by the maximum population density across all block groups.

#### Raises

- **ValueError**: If no API key is provided and it is also not found in the file `census_api_key.txt`, a `ValueError` is raised.

#### Workflow

1. **API Key Validation**: Checks for the presence of an API key either directly through the parameter or within a local file.
2. **FIPS Code Extraction**: Extracts the state and unique county FIPS codes from the GeoDataFrame.
3. **Census Data Retrieval**: Uses the Census API to fetch population data for each block group in the specified counties and state.
4. **Data Integration**: The fetched data is integrated into the original GeoDataFrame, converting population data to a usable format and creating new columns for population and population density.
5. **Population Density Calculation**: Calculates the population density and normalized population density, adding these metrics to the GeoDataFrame.
6. **Data Cleaning**: Cleans up the GeoDataFrame by removing unnecessary columns and ensuring proper indexing and geometry settings.

