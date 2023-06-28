# %%
import pandas as pd
import geopandas as gpd
# remove pandas limit of cols
pd.set_option('display.max_columns', None)
# %%
data = pd.read_parquet('../data/pur2020/udc2020.parquet')
data = data[data.comtrs.isnull()]
chem = pd.read_parquet('../data/pur2020/chemical.parquet')
sites = pd.read_csv('../data/pur2020/site.txt')
sections = gpd.read_parquet('../data/shp/parcels.parquet')
sections = sections[~sections.CO_MTRS.duplicated()]
# %%
combined = data.merge(chem, how="left", on="chem_code")
# %%
# combined = combined.merge(sections, how="left", left_on="comtrs", right_on="CO_MTRS")
# %%
county_id_crosswalk = pd.read_csv('../data/california_counties.csv')[['county_cd','COUNTYFP','NAME']]
# %%
combined = combined.merge(sites, how="left", on="site_code")
# %%
combined = combined.merge(county_id_crosswalk, how="left", left_on="county_cd", right_on="county_cd")

# %%
# combined = combined.drop(columns="NAME_x")
combined = combined.rename(columns={"NAME":"county_name"})
# %%
combined = pd.DataFrame(combined)

# %%
combined.to_parquet('../data/pur2020/pur2020_nonag.parquet')

# %%
