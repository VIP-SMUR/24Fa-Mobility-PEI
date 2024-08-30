### Land Diversity Index Generator

#### Description

This Python script analyzes a GeoJSON file containing block group data, calculating the Land Diversity Index (LDI) for each block group. It outputs a CSV file detailing these LDI values, providing insights into diversity within the analyzed area.

#### Parameters

- **GeoJSON file**: A GeoJSON file that must contain the block groups' geometries and the FIPS codes for the state and counties.

#### Returns

- **CSV file**: A new csv file is created, which contains columns from the geojson file as well as additional values collected for each block utilized in the IDI computation.
  - `Polygon`: the geometry of each block group
  - `Land_use_dict`: A dictionary for each block with key as the land use type and the value being the area occupied by the land type.
  - `Entropy`:The entropy of a block
  - `LDI`:The LDI value which is normalized  with the maximum LDI value for all the blocks.


#### Workflow

1. **Reading GeoJSON data**: Extracts the geometry of a polygons from a file.
2. **Land Use Data Extraction**: OSMNX is used to extract Land use data for a specified block.
3. **Entropy Calculation**:This is the first step of calculating LDI and the entropy is calculated for each block.
4. **Land Diversity Calculation**: Calculates LDI per block by normalizing the entropies of all the blocks
5. **return file**: generates a CSV with the data and LDI values required for creating visualizations in LDI_visualization.ipynb.
