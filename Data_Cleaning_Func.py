import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import time
import datetime


def clean_airbnb_data(cal_table_raw, listing_table_raw, cal_table_to_save, listing_table_to_save, amenities_table_to_save):
    conn_string = 'postgres://whnpmxwsiccrtg:53c453893549d2b1e6a4ff92e626a2a08ebcaff66678e50d33e3742f66e3e4f4@ec2-52-4-171-132.compute-1.amazonaws.com/d2ajro4cjr10lb'
    db = create_engine(conn_string)
    conn = db.connect()

    # # read in calendar data from postgres
    # cal_data = pd.read_sql_query(
    #     ('select * from "{}"').format(cal_table_raw), con=conn)

    # # Renaming listing_id column to id to be consistent with other dataframe
    # cal_data = cal_data.rename(columns={'listing_id': 'id'})

    # # create day and month from data df.
    # cal_data['date'] = pd.to_datetime(cal_data['date'])
    # cal_data['day'] = cal_data['date'].dt.day_name()
    # cal_data['month'] = cal_data['date'].dt.month

    # # Converting day of the week to weekday or weekend
    # cal_data.loc[(cal_data.day == "Friday"), "day"] = 'weekend'
    # cal_data.loc[(cal_data.day == "Saturday"), "day"] = 'weekend'
    # cal_data.loc[(cal_data.day == "Monday"), "day"] = 'weekday'
    # cal_data.loc[(cal_data.day == "Tuesday"), "day"] = 'weekday'
    # cal_data.loc[(cal_data.day == "Wednesday"), "day"] = 'weekday'
    # cal_data.loc[(cal_data.day == "Thursday"), "day"] = 'weekday'
    # cal_data.loc[(cal_data.day == "Sunday"), "day"] = 'weekday'

    # # Dropped date, available, adjusted_price, minimum_nights, and maximum_nights column
    # cal_data_new = cal_data.drop(
    #     ['date', 'available', 'adjusted_price', 'minimum_nights', 'maximum_nights'], axis=1)

    # # Remove and replace $ and ,
    # cal_data_new['price'] = cal_data_new['price'].str.replace('$', '')
    # cal_data_new['price'] = cal_data_new['price'].str.replace(',', '')

    # # Converting price from object to float
    # cal_data_new['price'] = cal_data_new['price'].astype(float)

    # # Group id, day, and month and calculate mean price
    # cal_data_grouped = cal_data_new.groupby(
    #     ['id', 'day', 'month']).mean().reset_index()

    # # export cleaned calendar data to postgres
    # cal_data_grouped.to_sql(("{}").format(
    #     cal_table_to_save), con=conn, if_exists='replace', index=False)

    # read in listing data
    list_data = pd.read_sql_query(
        ('select * from "{}"').format(listing_table_raw), con=conn)

    # create amenities df to be parsed
    amenities_df = list_data[['id', 'amenities']]

    # keep non-descriptor columns
    list_data_new = list_data[['id', 'last_scraped', 'host_since', 'host_listings_count', 'host_is_superhost', 'host_identity_verified', 'neighbourhood_cleansed',
                               'latitude', 'longitude', 'room_type', 'property_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type',
                               'square_feet', 'price', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'number_of_reviews', 
                               'number_of_reviews_ltm', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',  'review_scores_checkin',
                               'review_scores_communication', 'review_scores_location', 'review_scores_value', 'instant_bookable',
                               'is_business_travel_ready', 'cancellation_policy', 'require_guest_profile_picture', 'require_guest_phone_verification',
                               'has_availability', 'guests_included','availability_30','availability_60','availability_90','availability_365','reviews_per_month']]

    # drop the columns with mostly NaN
    list_data_new = list_data_new.drop(
        columns=['weekly_price', 'monthly_price', 'square_feet'])

    #  the following sections change the string $ fields to float
    list_data_new['price'] = list_data_new['price'].str.replace('$', '')
    list_data_new['price'] = list_data_new['price'].str.replace(',', '')
    list_data_new['price'] = list_data_new['price'].astype(float)
    list_data_new['security_deposit'] = list_data_new['security_deposit'].str.replace(
        '$', '')
    list_data_new['security_deposit'] = list_data_new['security_deposit'].str.replace(
        ',', '')
    list_data_new['security_deposit'] = list_data_new['security_deposit'].astype(
        float)
    list_data_new['cleaning_fee'] = list_data_new['cleaning_fee'].str.replace(
        '$', '')
    list_data_new['cleaning_fee'] = list_data_new['cleaning_fee'].str.replace(
        ',', '')
    list_data_new['cleaning_fee'] = list_data_new['cleaning_fee'].astype(float)

    # fill Nans
    list_data_new['security_deposit'] = list_data_new['security_deposit'].fillna(
        0)
    list_data_new['cleaning_fee'] = list_data_new['cleaning_fee'].fillna(0)

    # drop 'beds'  many have 0s and some nans so not descriptive
    list_data_new = list_data_new.drop(columns=['beds'])

    # add new variable called "days_host" which is a calculated value of the difference between the scrape date and the host_since date
    list_data_new[['last_scraped', 'host_since']] = list_data_new[[
        'last_scraped', 'host_since']].apply(pd.to_datetime)  # if conversion required
    list_data_new['days_host'] = (
        list_data_new['last_scraped'] - list_data_new['host_since']).dt.days

    #  replace all NaNs in review columns with 0 - note there are no real 0 reviews and there is a variable is_review to identify the fake 0 values
    cols=['review_scores_value','review_scores_location','review_scores_checkin','review_scores_communication','review_scores_cleanliness','review_scores_rating','reviews_per_month','review_scores_accuracy']
    list_data_new[cols]=list_data_new[cols].fillna(0)

    # Dropping review columns with collinearity above 0.8 besides whether it has reviews or number of reviews:
    list_data_new = list_data_new.drop(columns=['review_scores_communication', 'review_scores_checkin',
                                                'review_scores_cleanliness', 'review_scores_value', 'review_scores_location'])

    # export cleaned lisitng data to postgres
    list_data_new.to_sql(("{}").format(listing_table_to_save),
                         con=conn, if_exists='replace', index=False, method='multi')

    # # Clean the amenities lists to remove spaces, quotes, parenthesis, brackets and capitals.
    # amenities_df['amenities'] = amenities_df['amenities'].str.lower().str.replace(' ', '_').str.replace(
    #     '"', '').str.replace('{', '').str.replace('}', '').str.replace('(', '').str.replace(')', '')

    # # iterate over each row, parse the amenities string and assign 1 for amenities listed and 0 for amenities not listed in each row.
    # for index, row in amenities_df.iterrows():
    #     for amenity in row['amenities'].split(','):
    #         amenities_df.loc[index, amenity] = 1

    # amenities_df.fillna(0, inplace=True)

    # # Drop the amenities column and the column with no name.
    # amenities_df = amenities_df.drop(columns=['amenities', ''])

    # # Create a new "Kitchen_Grouped" column whose values will be the sum of the values from all the kitchen-related amenity columns:
    # amenities_df["Kitchen_Summed"] = amenities_df[["dishes_and_silverware", "refrigerator",
    #                                                "oven", "coffee_maker", "stove", "microwave", "dishwasher", "cooking_basics"]].sum(axis=1)

    # # Any values of the new "Kitchen_Summed" column which are less than 4, replace as 0 and if 4 or more replace as a 1
    # amenities_df["Kitchen_Grouped_Binary"] = amenities_df["Kitchen_Summed"].replace(
    #     {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1})

    # # Drop the old columns:
    # amenities_df = amenities_df.drop(columns=["Kitchen_Summed", "dishes_and_silverware", "refrigerator",
    #                                           "oven", "coffee_maker", "stove", "microwave", "dishwasher", "cooking_basics"])

    # # Sum the values from all the bathroom-related columns into one "Bathroom_Grouped" column:
    # amenities_df["Bathroom_Summed"] = amenities_df[[
    #     "bathroom_essentials", "bath_towel"]].sum(axis=1)

    # # Any values less than 2, replace as 0, if 2 or more, replace with 1:
    # amenities_df["Bathroom_Grouped_Binary"] = amenities_df["Bathroom_Summed"].replace({
    #                                                                                   0: 0, 1: 0, 2: 1})

    # # Drop the old columns:
    # amenities_df = amenities_df.drop(
    #     columns=["Bathroom_Summed", "bathroom_essentials", "bath_towel"])

    # # Create a new "Washer_Dryer_Grouped" column whose values will be the sum of the values from all the kitchen-related amenity columns:
    # amenities_df["Laundry_Summed"] = amenities_df[[
    #     "washer", "dryer"]].sum(axis=1)

    # # Any values less than 2, replace as 0, if 2 or more, replace with 1.  Note, this will only give a 1 if both washer and dryer are present.
    # amenities_df["Laundry_Grouped_Binary"] = amenities_df["Laundry_Summed"].replace({
    #                                                                                 0: 0, 1: 0, 2: 1})

    # # Drop the old columns:
    # amenities_df = amenities_df.drop(
    #     columns=["Laundry_Summed", "washer", "dryer"])

    # # export parsed amenitiy data to postgres
    # amenities_df.to_sql(("{}").format(amenities_table_to_save),
    #                     con=conn, if_exists='replace', index=False)

    print("ETL Complete")
    conn.close ()