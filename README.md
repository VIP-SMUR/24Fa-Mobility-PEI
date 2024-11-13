# Pedestrian Environment Index (PEI) Implementation

This project implements the Pedestrian Environment Index (PEI) methodology as developed at the University of Illinois Chicago (see the research paper: [https://www.sciencedirect.com/science/article/pii/S0966692314001343](https://www.sciencedirect.com/science/article/pii/S0966692314001343)). The PEI provides a composite measure of the walkability of an environment, incorporating the following subindices:

* Population Density Index (PDI)
* Commercial Density Index (CDI)
* Intersection Density Index (IDI)
* Land-use Diversity Index (LDI)

## Team

| Name                  | Seniority | Major                  | Department | GitHub Handle                                                 | Topic Area                                             |
| --------------------- | --------- | ---------------------- | ---------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| Yilun Zha             | PhD       | Planning/Urban Design  | ARCH       | [elonncha](https://github.com/elonncha)                       | [Mobility-PEI](/24fa-mobility-pei)                     |
| C. "Albert" Le        | Sophomore | Computer Engineering   | ECE        | [balbertle](https://github.com/balbertle)                     | [Mobility-PEI](/24fa-mobility-pei)                     |
| Chunlan Wang          | Masters   | Architecture (DC)      | ARCH       | [wang-123-xi](https://github.com/wang-123-xi)                 | [Mobility-PEI](/24fa-mobility-pei)                     |
| Yichao Shi            | PhD       | Architecture           | ARCH       | [SHIyichao98](https://github.com/SHIyichao98)                 | [Mobility-PEI](/24fa-mobility-pei)                     |
| Atharva Beesen        | Junior    | Computer Science       | COC        | [AtharvaBeesen](https://github.com/AtharvaBeesen)             | [Mobility-PEI](/24fa-mobility-pei)                     |



**Motivation**

Understanding the walkability of an environment is important for urban planning, public health initiatives, and promoting active transportation. This implementation of the PEI can be used by researchers to:

* Assess the current walkability of neighborhoods or regions
* Compare walkability across different areas
* Identify areas with potential for improvement

**Getting Started**



* **Prerequisites:**
   * Python 3.x 
   * **Libraries:**
        * osmnx
        * pandas
        * numpy
        * matplotlib.pyplot
        * csv
        * census
   * Census API Key: Can be found at: [https://api.census.gov/data/key_signup.html](https://api.census.gov/data/key_signup.html). **Must paste key in text file titled census_api_key.txt in the same directory as PDI_generator.ipynb to access population data.**

**Installation**

You can install the required libraries using pip:

```bash
pip install osmnx pandas numpy matplotlib csv census
```

* **Usage:** 

**Contributing**



**License**

Idk how licensing works... Just don't sell it I guess.

***
