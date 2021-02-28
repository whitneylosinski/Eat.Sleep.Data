import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2
import time

def clean_data (calendar_table, table_to_save):
    conn_string = 'postgres://whnpmxwsiccrtg:53c453893549d2b1e6a4ff92e626a2a08ebcaff66678e50d33e3742f66e3e4f4@ec2-52-4-171-132.compute-1.amazonaws.com/d2ajro4cjr10lb'
    db = create_engine(conn_string)
    conn = db.connect()
    data = pd.read_sql_query(('select * from "{}"').format(calendar_table),con=conn)

    # Renaming listing_id column to id to be consistent with other dataframe
    data=data.rename(columns={'listing_id':'id'})
    
    # crate day and month from data df.
    data['date']=pd.to_datetime(data['date'])
    data['day'] = data['date'].dt.day_name()
    data['month'] = data['date'].dt.month

    # Converting day of the week to weekday or weekend
    data.loc[(data.day =="Friday"),"day"]='weekend'
    data.loc[(data.day =="Saturday"),"day"]='weekend'
    data.loc[(data.day =="Monday"),"day"]='weekday'
    data.loc[(data.day =="Tuesday"),"day"]='weekday'
    data.loc[(data.day =="Wednesday"),"day"]='weekday'
    data.loc[(data.day =="Thursday"),"day"]='weekday'
    data.loc[(data.day =="Sunday"),"day"]='weekday'

    # Dropped date, available, adjusted_price, minimum_nights, and maximum_nights column
    data_new = data.drop(['date','available','adjusted_price','minimum_nights','maximum_nights'],axis=1)

    # Remove and replace $ and ,
    data_new['price']=data_new['price'].str.replace('$','')
    data_new['price']=data_new['price'].str.replace(',','')

    # Converting price from object to float
    data_new['price']=data_new['price'].astype(float)

    # Group id, day, and month and calculate mean price
    data_grouped=data_new.groupby(['id','day','month']).mean().reset_index()

    data_grouped.to_sql(("{}").format(table_to_save), con=conn, if_exists='replace', index=False)