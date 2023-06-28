# %%
from glob import glob
import pandas as pd
import geopandas as gpd
import pyarrow
# beautiful soup
from bs4 import BeautifulSoup
import requests
# remove pandas column limit
pd.set_option('display.max_columns', None)

# %%
text_files = glob("../data/pur2020/udc*.txt")
print(text_files)
# %%
for file in text_files:
    data = pd.read_csv(file)
    filename = file.split('/')[-1].split('.txt')[0]
    convert_to_str = ['grower_id', 'township', 'site_loc_id']
    for col in convert_to_str:
        data[col] = data[col].astype(str)
        
    data.to_parquet(f'../data/pur2020/{filename}.parquet', index=False)
# %%
parquet_files = glob("../data/pur2020/udc*.parquet")
# %%
# concat all parquet files into one
df = pd.concat([pd.read_parquet(file) for file in parquet_files])
# # export
df.to_parquet('../data/pur2020/udc2020.parquet', index=False)
# %%
df = pd.read_parquet('../data/pur2020/udc2020.parquet')
# %%
base_url = 'https://www.cdpr.ca.gov'
geo_url = f'{base_url}/docs/emon/grndwtr/plss_shapefiles.htm'
# get every href value of a elements from above url within table with role="presentation"
html = requests.get(geo_url).text
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
links = table.find_all('a')
hrefs = [link.get('href') for link in links]

# %%
# download all shapefiles to data dir
for href in hrefs:
    if href.endswith('.zip'):
        url = f'{base_url}{href}'
        print(url)
        r = requests.get(url)
        filename = href.split('/')[-1]
        with open(f'../data/shp/{filename}', 'wb') as f:
            f.write(r.content)
# %%
# import and concat all shp files with geopandas
shp_files = glob('../data/shp/*.zip')
gdf = pd.concat([gpd.read_file(file) for file in shp_files])
# %%
# convert to wgs84
gdf = gdf.to_crs('EPSG:4326')
# %%
# export to parquet
gdf.to_parquet('../data/shp/parcels.parquet', index=False)
# %%
# export to gpkg
gdf.to_file('../data/shp/parcels.gpkg', driver='GPKG')
# %%
# read chem data and convert to parquet
chem = pd.read_csv('../data/pur2020/chemical.txt')
# %%
chem.to_parquet('../data/pur2020/chemical.parquet', index=False)
# %%
names = list(chem.sort_values('chemname').chemname)
# export to json list
import json
with open('../data/pur2020/chemnames.json', 'w') as f:
    json.dump(names, f)
# %%
