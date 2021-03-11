import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import time
import datetime
from sklearn.preprocessing import OneHotEncoder
from scipy import stats
from sklearn.ensemble import IsolationForest

conn_string = 'postgres://whnpmxwsiccrtg:53c453893549d2b1e6a4ff92e626a2a08ebcaff66678e50d33e3742f66e3e4f4@ec2-52-4-171-132.compute-1.amazonaws.com/d2ajro4cjr10lb'
db = create_engine(conn_string)
conn = db.connect()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# read in listing data
list_data = pd.read_sql_query(('select * from "{}"').format('listings_full'), con=conn)

# Make a list of columns that will not be used in the analysis
columns_to_drop = list_data[['listing_url', 'scrape_id', 'name', 'summary', 'space', 'description', 'neighborhood_overview', 'latitude', 'longitude', 'notes', 'transit', 'access', 
                            'interaction', 'house_rules', 'thumbnail_url', 'medium_url', 'picture_url', 'xl_picture_url', 'host_id', 'host_url', 'host_name', 'host_location', 'host_about', 
                            'host_thumbnail_url', 'host_picture_url', 'host_neighbourhood', 'host_verifications', 'street', 'neighbourhood', 'neighbourhood_group_cleansed', 'city', 'state', 
                            'zipcode', 'market','smart_location', 'country_code', 'country', 'latitude', 'longitude', 'is_location_exact', 'calendar_updated', 'calendar_last_scraped', 
                            'extra_people', 'jurisdiction_names', 'host_acceptance_rate', 'host_response_time', 'host_response_rate', 'license', 'square_feet', 'weekly_price', 
                            'monthly_price', 'first_review', 'last_review', 'host_total_listings_count', 'calculated_host_listings_count', 'calculated_host_listings_count_entire_homes', 
                            'calculated_host_listings_count_private_rooms', 'calculated_host_listings_count_shared_rooms', 'host_has_profile_pic', 'has_availability', 
                            'requires_license','is_business_travel_ready', 'require_guest_profile_picture', 'require_guest_phone_verification', 'experiences_offered']]

# Drop columns that will not be used in the analysis
list_data_new = list_data.drop(columns=columns_to_drop)

#  replace all NaNs with 0s
cols=['security_deposit', 'cleaning_fee', 'review_scores_value','review_scores_location','review_scores_checkin','review_scores_communication','review_scores_cleanliness',
    'review_scores_rating', 'reviews_per_month','review_scores_accuracy']
list_data_new[cols]=list_data_new[cols].fillna('0')

# add new variable called "days_host" which is a calculated value of the difference between the scrape date and the host_since date
list_data_new[['last_scraped', 'host_since']] = list_data_new[['last_scraped', 'host_since']].apply(pd.to_datetime)  # if conversion required
list_data_new['days_host'] = (list_data_new['last_scraped'] - list_data_new['host_since']).dt.days
list_data_new = list_data_new.drop(columns=['last_scraped', 'host_since'])

# Drop two listings where beds are NaN
list_data_new = list_data_new.dropna(subset=['beds'])

# Remove $ and comma from prices and change from string to float
list_data_new['price']=list_data_new['price'].str.replace('$','').str.replace(',','').astype(float)
list_data_new['security_deposit']=list_data_new['security_deposit'].str.replace('$','').str.replace(',','').astype(float)
list_data_new['cleaning_fee']=list_data_new['cleaning_fee'].str.replace('$','').str.replace(',','').astype(float)

# Create a separate dataframe of id and amenities to parse.
amenities_df = list_data_new[['id', 'amenities']]
# Clean the amenities lists to remove spaces, quotes, parenthesis, brackets and capitals.
amenities_df['amenities'] = amenities_df['amenities'].str.lower().str.replace(' ', '_').str.replace('"', '').str.replace('{', '').str.replace('}', '').str.replace('(', '').str.replace(')', '')

# iterate over each row, parse the amenities string and assign 1 for amenities listed and 0 for amenities not listed in each row.
for index, row in amenities_df.iterrows():
    for amenity in row['amenities'].split(','):
        amenities_df.loc[index, amenity] = 1
amenities_df.fillna(0, inplace=True)

# Drop the amenities column and the column with no name.
amenities_df = amenities_df.drop(columns=['amenities', '', 'essentials', 'translation_missing:_en.hosting_amenity_49', 'translation_missing:_en.hosting_amenity_50'])

# read in calendar data from postgres
cal_data = pd.read_sql_query(('select * from "{}"').format(cal_table_raw), con=conn)

# Drop adjusted price, available and min/max nights from the cal_data dataframe
cal_data = cal_data.drop(columns=['available', 'adjusted_price', 'minimum_nights', 'maximum_nights'])   

# Remove $ and commas from price and change it from a string to a float value.
cal_data['price']=cal_data['price'].str.replace('$','').str.replace(',','').astype('float')

# Change the date from a string to a datetime format
cal_data['date']=pd.to_datetime(cal_data['date'])

# Renaming listing_id column to id to be consistent with other dataframe
cal_data=cal_data.rename(columns={'listing_id':'id'})

# Create day and month from cal_data
cal_data['day'] = cal_data['date'].dt.day_name()
cal_data['month'] = cal_data['date'].dt.month

# Converting day of the week to weekday or weekend
cal_data.loc[(cal_data.day =="Friday"),"day"]='weekend'
cal_data.loc[(cal_data.day =="Saturday"),"day"]='weekend'
cal_data.loc[(cal_data.day =="Monday"),"day"]='weekday'
cal_data.loc[(cal_data.day =="Tuesday"),"day"]='weekday'
cal_data.loc[(cal_data.day =="Wednesday"),"day"]='weekday'
cal_data.loc[(cal_data.day =="Thursday"),"day"]='weekday'
cal_data.loc[(cal_data.day =="Sunday"),"day"]='weekday'

# Drop date column since it will no longer be used
cal_data = cal_data.drop(['date'],axis=1)

# Group id, day, and month and calculate mean price
cal_data_grouped = cal_data.groupby(['id','day','month']).mean().reset_index()

# export data to postgres
list_data_new.to_sql('listings_full_clean', con=conn, if_exists='replace', index=False)
amenities_df.to_sql('amenities_clean', con=conn, if_exists='replace', index=False)
cal_data_grouped.to_sql('calendar_clean', con=conn, if_exists='replace', index=False)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Drop the price column in the listings data since the price is in the calendar data.
list_data_to_merge = list_data_new.drop(columns = 'price')

# Merge listing, amenities and calendar data into one table.
merge1 = list_data_to_merge.merge(amenities_df, how='left', on ='id')
merged = merge1.merge(cal_data_grouped, how='left', on ='id')

# Drop the id column
merged = merged.drop(columns = 'id')

# Get a list of the object type columns.
objects = merged.dtypes[merged.dtypes == 'object'].index.tolist()

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False, drop='if_binary')

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(merged[objects]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names(objects)
encode_df.head()

# Merge one-hot encoded features and drop the originals
merged = merged.merge(encode_df,left_index=True, right_index=True)
merged = merged.drop(columns=objects)

# Dropping columns with collinearity above 0.8:
merged = merged.drop(columns=['minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm', 
                              'review_scores_accuracy', 'review_scores_communication', 'review_scores_checkin', 'review_scores_cleanliness', 'review_scores_value', 'review_scores_location', 
                              "availability_60", "availability_90", "number_of_reviews_ltm", "beds", "room_type_Private room"])

# Repeat previous step for the table prior to merge due to no longer using the calendar data.
list_data_new = list_data_new.drop(columns=['minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'minimum_nights_avg_ntm', 
                                            'maximum_nights_avg_ntm', 'review_scores_accuracy', 'review_scores_communication', 'review_scores_checkin', 'review_scores_cleanliness', 
                                            'review_scores_value', 'review_scores_location', "availability_60", "availability_90", "number_of_reviews_ltm", "beds"])

# Bucket bathroom items
merged["Bathroom_Summed"] = merged[["bathroom_essentials", "body_soap"]].sum(axis=1)
merged = merged.drop(columns=["Bathroom_Summed", "bathroom_essentials", "body_soap"])
merged = merged.drop(columns=["Bathroom_Summed", "bathroom_essentials", "body_soap"])

# Repeat previous step for the table prior to merge due to no longer using the calendar data.
amenities_df["Bathroom_Summed"] = amenities_df[["bathroom_essentials", "body_soap"]].sum(axis=1)
amenities_df["Bathroom_Grouped_Binary"] = amenities_df["Bathroom_Summed"].replace({0:0, 1:0, 2:1})
amenities_df = amenities_df.drop(columns=["Bathroom_Summed", "bathroom_essentials", "body_soap"])

# Bucket laundry items
merged["Laundry_Summed"] = merged[["washer", "dryer"]].sum(axis=1)
merged["Laundry_Grouped"] = merged["Laundry_Summed"].replace({0:0, 1:0, 2:1})
merged = merged.drop(columns=["Laundry_Summed", "washer", "dryer"])

# Repeat previous step for the table prior to merge due to no longer using the calendar data.
amenities_df["Laundry_Summed"] = amenities_df[["washer", "dryer"]].sum(axis=1)
amenities_df["Laundry_Grouped"] = amenities_df["Laundry_Summed"].replace({0:0, 1:0, 2:1})
amenities_df = amenities_df.drop(columns=["Laundry_Summed", "washer", "dryer"])

# Bucket kitchen items
merged["Kitchen_Summed"] = merged[["dishes_and_silverware", "refrigerator", "oven", "coffee_maker", "stove", "microwave", "dishwasher", "cooking_basics"]].sum(axis=1)
merged["Kitchen_Grouped"] = merged["Kitchen_Summed"].replace({0:0, 1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:1, 8:1})
merged = merged.drop(columns=["Kitchen_Summed", "dishes_and_silverware", "refrigerator", "oven", "coffee_maker", "stove", "microwave", "dishwasher", "cooking_basics"])

# Repeat previous step for the table prior to merge due to no longer using the calendar data.
amenities_df["Kitchen_Summed"] = amenities_df[["dishes_and_silverware", "refrigerator", "oven", "coffee_maker", "stove", "microwave", "dishwasher", "cooking_basics"]].sum(axis=1)
amenities_df["Kitchen_Grouped"] = amenities_df["Kitchen_Summed"].replace({0:0, 1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:1, 8:1})
amenities_df = amenities_df.drop(columns=["Kitchen_Summed", "dishes_and_silverware", "refrigerator", "oven", "coffee_maker", "stove", "microwave", "dishwasher", "cooking_basics"])

# export merged and bucketed data to postgres
merged.to_sql('merged_bucketed', con=conn, if_exists='replace', index=False)
list_data_new.to_sql('listings_full_bucketed', con=conn, if_exists='replace', index=False)
amenities_df.to_sql('amenities_bucketed', con=conn, if_exists='replace', index=False)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Merge amenities table to full listings. (left merge on id)
merged_no_cal = list_data_new.merge(amenities_df, how='left', on ='id')

# Drop 'id' (unique identifier - not relevant)
merged_no_cal = merged_no_cal.drop(columns = 'id')

# Get a list of all object columns for OneHotEncoding
objects = merged_no_cal.dtypes[merged_no_cal.dtypes == 'object'].index.tolist()

# OneHotEncode object values
enc = OneHotEncoder(sparse=False, drop='if_binary')

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(merged_no_cal[objects]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names(objects)

# Merge one-hot encoded features and drop the originals
merged_no_cal = merged_no_cal.merge(encode_df,left_index=True, right_index=True)
merged_no_cal = merged_no_cal.drop(columns=objects)

# Drop the room_type_Private room column:
merged_no_cal = merged_no_cal.drop(columns=["room_type_Private room"])

# Set erroneous 30 bedroom listings for apartments to 1
merged_no_cal.loc[merged_no_cal['bedrooms'] > 29, 'bedrooms'] = 1

# Convert zero bedrooms with more than 4 accommodates to 2 bedrooms
merged_no_cal.loc[(merged_no_cal['bedrooms'] == 0) & (merged_no_cal['accommodates'] > 4), 'bedrooms'] = 2

# Convert zero bedrooms with more than 4 accommodates to 1 bedroom
merged_no_cal.loc[(merged_no_cal['bedrooms'] == 0) & (merged_no_cal['accommodates'] < 5), 'bedrooms'] = 1

# Drop all listings that are more than 2 standard deviations from the mean.
merged_no_cal = merged_no_cal[(np.abs(stats.zscore(merged_no_cal['accommodates_logs'])) < 2)]

# Drop the log column that was created.
merged_no_cal = merged_no_cal.drop(columns=['accommodates_logs'])

# Drop all listings that are more than 2 standard deviations from the mean.
merged_no_cal = merged_no_cal[(np.abs(stats.zscore(merged_no_cal['baths_logs'])) < 2)]

# Drop the log column that was created.
merged_no_cal = merged_no_cal.drop(columns=['baths_logs'])

# Drop all listings that are more than 2 standard deviations from the mean.
merged_no_cal = merged_no_cal[(np.abs(stats.zscore(merged_no_cal['host_listings_count'])) < 3)]

# Drop the log column that was created.
merged_no_cal = merged_no_cal.drop(columns=['host_listings_count_log'])

log_column_list = []

for column in merged_no_cal.columns:
    log_col_name = column + "_logs"
    # Ignore columns with max less than or equal to 1 (binary)
    if merged_no_cal[column].max() > 1:
        # natural log transform (+1 to handle 0 values)
        merged_no_cal[log_col_name] = np.log(merged_no_cal[column]+1)
        merged_no_cal = merged_no_cal[(np.abs(stats.zscore(merged_no_cal[log_col_name])) < 3)]
        log_column_list.append(log_col_name)
        print(log_col_name)
        print(merged_no_cal.shape)

merged_no_cal.drop(columns=log_column_list, inplace=True)

# Delete any rows with outliers in any row (3 SD) using calculated field log(price/accommodates)
merged_no_cal = merged_no_cal[(np.abs(stats.zscore(np.log(merged_no_cal['price']/merged_no_cal['accommodates']))) < 3)]

# Drop additional outliers using IsolationForest
X = merged_no_cal.drop(columns=['price']).values
iso = IsolationForest(contamination='auto')
yhat = iso.fit_predict(X)
merged_no_cal['outlier'] = yhat

# Drop any listings with an anomaly score of -1 from the data.
merged_no_cal = merged_no_cal[merged_no_cal['outlier']!=-1]
merged_no_cal.drop(columns=['outlier'], inplace=True)

# Upload cleaned data to Postgres
merged_no_cal.to_sql('merged_no_cal', con=conn, if_exists='replace', index=False)

conn.close ()