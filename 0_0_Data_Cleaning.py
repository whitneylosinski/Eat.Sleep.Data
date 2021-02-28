import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import time
import datetime

def clean_data (cal_table_raw, cal_table_to_save,listing_table_raw,lisitng_table_to_save):
    conn_string = 'postgres://whnpmxwsiccrtg:53c453893549d2b1e6a4ff92e626a2a08ebcaff66678e50d33e3742f66e3e4f4@ec2-52-4-171-132.compute-1.amazonaws.com/d2ajro4cjr10lb'
    db = create_engine(conn_string)
    conn = db.connect()
    
    #read in calendar data from postgres
    cal_data = pd.read_sql_query(('select * from "{}"').format(cal_table_raw),con=conn)

    # Renaming listing_id column to id to be consistent with other dataframe
    cal_data=cal_data.rename(columns={'listing_id':'id'})
    
    # crate day and month from data df.
    cal_data['date']=pd.to_datetime(cal_data['date'])
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

    # Dropped date, available, adjusted_price, minimum_nights, and maximum_nights column
    cal_data_new = cal_data.drop(['date','available','adjusted_price','minimum_nights','maximum_nights'],axis=1)

    # Remove and replace $ and ,
    cal_data_new['price']=cal_data_new['price'].str.replace('$','')
    cal_data_new['price']=cal_data_new['price'].str.replace(',','')

    # Converting price from object to float
    cal_data_new['price']=cal_data_new['price'].astype(float)

    # Group id, day, and month and calculate mean price
    cal_data_grouped=cal_data_new.groupby(['id','day','month']).mean().reset_index()

    #export cleaned calendar data to postgres
    cal_data_grouped.to_sql(("{}").format(cal_table_to_save), con=conn, if_exists='replace', index=False)


    #read in listing data
    list_data = pd.read_sql_query(('select * from "{}"').format(listing_table_raw),con=conn)

    #keep non-descriptor columns
    liast_data_new = list_data[['id','last_scraped','host_since','host_listings_count','host_is_superhost','host_identity_verified','neighbourhood_cleansed',\
    'latitude','longitude','room_type','property_type','accommodates','bathrooms','bedrooms','beds','bed_type',\
    'square_feet','price','weekly_price','monthly_price','security_deposit','cleaning_fee','review_scores_rating',
    'number_of_reviews','review_scores_cleanliness',\
    'review_scores_location','review_scores_communication','review_scores_checkin','review_scores_value','instant_bookable',\
    'is_business_travel_ready','cancellation_policy','require_guest_profile_picture','require_guest_phone_verification',\
    'has_availability' ]]    

    # drop the columns with mostly NaN
    list_data_new=list_data_new.drop(columns=['weekly_price','monthly_price','square_feet'])  

    #  the following sections change the string $ fields to float
    list_data_new['price']=list_data_new['price'].str.replace('$','')
    list_data_new['price']=list_data_new['price'].str.replace(',','')
    list_data_new['price']=list_data_new['price'].astype(float)
    list_data_new['security_deposit']=list_data_new['security_deposit'].str.replace('$','')
    list_data_new['security_deposit']=list_data_new['security_deposit'].str.replace(',','')
    list_data_new['security_deposit']=list_data_new['security_deposit'].astype(float)
    list_data_new['cleaning_fee']=list_data_new['cleaning_fee'].str.replace('$','')
    list_data_new['cleaning_fee']=list_data_new['cleaning_fee'].str.replace(',','')
    list_data_new['cleaning_fee']=list_data_new['cleaning_fee'].astype(float)

    #fill Nans
    list_data_new['security_deposit']=list_data_new['security_deposit'].fillna(0)
    list_data_new['cleaning_fee']=list_data_new['cleaning_fee'].fillna(0)

    # drop 'beds'  many have 0s and some nans so not descriptive
    list_data_new=list_data_new.drop(columns=['beds'])

    # create new variable yes or no as to reviews so if this is no and the review is 0
    # reviews range from 2 to 10 there are no real 0 reviews
    list_data_new['is_review'] = np.where(list_data_new['review_scores_rating']>0,True,False)

    #  replace all NaNs in review columns with 0 - note there are no real 0 reviews and there is a variable is_review to identify the fake 0 values
    cols=['review_scores_value','review_scores_location','review_scores_checkin','review_scores_communication','review_scores_cleanliness','review_scores_rating']
    list_data_new[cols]=list_data_new[cols].fillna(0)

    # Calculate number of days hosted
    date1=list_data_new['last_scraped'][0]
    date2=list_data_new['host_since'][0]
    mdate1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
    rdate1 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
    delta =  (mdate1 - rdate1).days

    # add new variable called "days_host" which is a calculated value of the difference between the scrape date and the host_since date
    list_data_new[['last_scraped','host_since']] = list_data_new[['last_scraped','host_since']].apply(pd.to_datetime) #if conversion required
    list_data_new['days_host'] = (list_data_new['last_scraped'] - list_data_new['host_since']).dt.days

    #export cleaned lisitng data to postgres
    list_data_new.to_sql(("{}").format(lisitng_table_to_save), con=conn, if_exists='replace', index=False)
