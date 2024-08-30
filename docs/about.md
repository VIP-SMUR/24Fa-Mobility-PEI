**About**

This project implements the Pedestrian Environment Index (PEI) methodology, a composite measure of walkability. It uses four key subindices:

* **Population Density Index (PDI):** Measures the density of residential population within a given area. Data for this index is derived from Census block groups  (_PDI_generator.ipynb_).
* **Commercial Density Index (CDI):** Calculates the density of commercial establishments in a Block Group, indicating the availability of destinations and services within walking distance (_CDI_generator.ipynb_).
* **Intersection Density Index (IDI):**  Measures the density of intersections within an area. Intersections can influence route options and pedestrian safety  (_IDI_generator.ipynb_).
* **Land-use Diversity Index (LDI):** Assesses the mix of different land-use types (e.g., residential, commercial, industrial) present. Diverse land uses often correspond with more walkable environments (_LDI_generator.ipynb_). 

**Workflow**

1. **Subindex Calculation:** Each Jupyter Notebook file (`*_generator.ipynb`) processes a Census block group shapefile to compute its respective subindex score. The output is saved as either a CSV or GeoJSON file.
2. **PEI Compilation:**  The `PEI_generator.ipynb` notebook takes the outputs from the subindex generators and computes the final PEI score for each block group.
3. **Visualization:**  The results are presented as a map, visualizing the PEI scores across census block groups.

**Note:** To ensure consistency and ease of use, we are in the process of consolidating all output files into the GeoJSON format.