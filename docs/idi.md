### Intersection Density Index Generator

#### Description

This Python script analyzes a GeoJSON file containing block group data, calculating the Intersection Density Index (IDI) for each block group. It outputs a CSV file detailing these IDI values, providing insights into intersection patterns within the analyzed area.

#### Parameters

- **GeoJSON file**: A GeoJSON file that must contain the block groups' geometries and the FIPS codes for the state and counties.

#### Returns

- **CSV file**: A new csv file is created, which contains columns from the geojson file as well as additional values collected for each block utilized in the IDI computation.
  - `Polygon`: the geometry of each block group
  - `Area`: The area of the block group
  - `Intersection`:Sum of the roads connected to an intersection in a block group.
  - `IDI`:The IDI value which is normalized IDI value for all the blocks.


#### Workflow

1. **Reading GeoJSON data**: Extracts the geometry of a polygons from a file.
2. **Intersection Data Extraction**: OSMNX is used to extract intersection data for a specified block.
3. **Equivalency Factor Calculation**:The number of roads connecting each intersection in a polygon is determined, as is the total of the Equivalency factors of all intersections in a block.
4. **Population Density Calculation**: Calculates IDI per block by dividing equivalency factor sums by respective areas. Normalize all IDIs.
5. **return file**: generates a CSV with the data and IDI values required for creating visualizations in IDI_visualization.ipynb.
