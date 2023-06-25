# Californians for Pesticide Reform CAN Summer Lab

##  Problem Statement
California leads the nation in pesticide use. Nearly 20 percent of the total pesticides used in the U.S. are used in California, a startling statistic considering that California cropland represents only 2-3 percent of the total planted acreage in the U.S. Unfortunately, a significant fraction of these pesticides are associated with acute poisoning, cancer, birth defects, sterility, neurotoxicity, damage to children and/or groundwater contamination. Of the 213 million pounds of pesticides applied within the state in 2015, 25 percent met one or more of these criteria.
The DSI OSL recently created a new webtool that CPR and its partners can use to query, visualize, and export pesticide and related datasets. Our team will help CPR conduct an initial analysis of the data to discover where (and which) pesticides are being applied most heavily in the state and whether recorded pesticide applications strongly correlate with social determinants of health (SDOH), race and ethnicity, acute illnesses, and/or pesticide drift.

## Research Questions
- Which pesticides are being applied in various spatial areas of concern (e.g., counties, school districts) and in what quantities?  What are the known health effects of those pesticides’ active ingredients?  How have application amounts changed over time?
- Is there a strong correlation between poor social determinants of health (e.g., lack of economic stability or access to quality education), belonging to an underrepresented racial minority, or contracting acute illnesses on the one hand, and living in or near a township or section that applies pesticides on the other? 
- How does non-agricultural pesticide use (eg. golf courses, parks, landscaping) compare in volume of pesticide application to agricultural uses? Where are the highest volumes or people potentially exposed to pesticide use?
- Based on local air and water surface monitoring studies, is there a statistically significant relationship between known cases of pesticide application and pesticide drift?

## Project Deliverables
- A Jupyter notebook that visualizes which pesticides have been applied, and in what amounts, across the state over time and then describes any trends (e.g., using spatial clustering tests/hotspot detection).
- A Jupyter notebook that analyzes correlations between pesticide amounts or class of pesticide and social determinants of health, race, and acute illnesses.
- A Jupyter notebook that visualizes reported pesticide applications against chemicals detected by air and surface water quality studies over time and describes the relationship between the two.

## Data Description

- `california_counties.gpkg` contains census county geographies for california.
- `california_elementary_school_districts.gpkg` contains Elementary School Divisions (ESLD) based on [TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) geographies.
- `california_tracts.gpkg` contains census tract geographies for California.
- `california_zctas.gpkg` contains census zip code tabulation area geographies for California.
- `california_watersheds.gpkg` contains various river watersheds in California, via [California Open Data](https://data.ca.gov/dataset/watershed-boundary-dataset-wbd).
- `pur2020_ag.parquet` contains agricultural PUR data for 2020, joined to the geographic boundaries. See California's [Department of Pesticide Regulation Data Dictionary](https://calpip.cdpr.ca.gov/infodocs.cfm?page=columndefs) for more information. 
- `pur2020_nonag.parquet` contains non-agricultural (eg. Landscaping, golf courses) PUR data for 2020. These PUR data are only recorded at the county leve. 
- `cleaned_county_data.csv`, `cleaned_elsd_data.csv`, and `cleaned_tract_data.csv` contain relevant census data at the county, Elementary School District, and Tract scales, respectively. They includedata such as the FIPS code, county name, total population, housing units, median household income, racial demographics, poverty levels, health insurance coverage, and other relevant socio-economic indicators for each county. Preliminary data cleaning have removed unnneeded columns and derived some common columns for your convenience, documented the the section titled "Census Data Dictionary" below.

## Census Data Dictionary

| Column Name                                             | Description                                                                                     |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| FIPS                                                    | Federal Information Processing Standards code                                                   |
| state                                                   | State name                                                                                      |
| state_fips                                              | State FIPS code                                                                                 |
| county                                                  | County name                                                                                     |
| tract                                                   | Census tract identifier                                                                         |
| geoid                                                   | Geographical identifier                                                                         |
| area_name                                               | Name of the area                                                                                |
| area_land                                               | Land area in square meters                                                                      |
| total_pop                                               | Total population count                                                                          |
| housing_units                                           | Total number of housing units                                                                   |
| owner_occupied_housing_units                            | Number of owner-occupied housing units                                                          |
| persons_no_health_insurance                             | Number of individuals without health insurance                                                  |
| families                                                | Number of families                                                                              |
| families_income_below_poverty_level                     | Number of families with income below the poverty level                                          |
| median_household_income                                 | Median household income                                                                         |
| nh_white_alone                                          | Number of individuals who are non-Hispanic white alone                                          |
| nh_black_or_african_american_alone                      | Number of individuals who are non-Hispanic Black or African American alone                      |
| nh_american_indian_and_alaska_native_alone              | Number of individuals who are non-Hispanic American Indian and Alaska Native alone              |
| nh_asian_alone                                          | Number of individuals who are non-Hispanic Asian alone                                          |
| nh_native_hawaiian_and_other_pacific_islander_alone     | Number of individuals who are non-Hispanic Native Hawaiian and Other Pacific Islander alone     |
| nh_other                                                | Number of individuals who are non-Hispanic other race alone                                     |
| nh_two_or_more                                          | Number of individuals who are non-Hispanic two or more races                                    |
| hispanic_or_latino                                      | Number of individuals who are Hispanic or Latino                                                |
| households_receiving_assistance                         | Number of households receiving assistance                                                       |
| households                                              | Total number of households                                                                      |
| pct_owner_occupied                                      | Percentage of owner-occupied housing units                                                      |
| pct_no_health_insurance                                 | Percentage of individuals without health insurance                                              |
| pct_families_income_below_poverty_level                 | Percentage of families with income below the poverty level                                      |
| pct_households_receiving_assistance                     | Percentage of households receiving assistance                                                   |
| pct_nh_white_alone                                      | Percentage of individuals who are non-Hispanic white alone                                      |
| pct_nh_black_or_african_american_alone                  | Percentage of individuals who are non-Hispanic Black or African American alone                  |
| pct_nh_american_indian_and_alaska_native_alone          | Percentage of individuals who are non-Hispanic American Indian and Alaska Native alone          |
| pct_nh_asian_alone                                      | Percentage of individuals who are non-Hispanic Asian alone                                      |
| pct_nh_native_hawaiian_and_other_pacific_islander_alone | Percentage of individuals who are non-Hispanic Native Hawaiian and Other Pacific Islander alone |
| pct_nh_other                                            | Percentage of individuals who are non-Hispanic other race alone                                 |
| pct_nh_two_or_more                                      | Percentage of individuals who are non-Hispanic two or more races                                |
| pct_hispanic_or_latino                                  | Percentage of individuals who are Hispanic or Latino                                            |

Isaiah Gonzalez