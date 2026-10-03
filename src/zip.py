import pandas as pd
## Zip and save the original raw file as a csv file for usability when working with Github repositories ##

# Read in the original dataset
import pandas as pd
file = pd.read_csv(r"..\data\amazon_reviews_us_Apparel_v1_00.csv",index_col=0)
# Compress and save raw file version
compression_opts = dict(method='zip',archive_name='amazon_reviews_us_Apparel_v1_00.csv')
file.to_csv('..\data\amazon_reviews_us_Apparel_v1_00.zip',index=False, compression=compression_opts)
#Zip.py
