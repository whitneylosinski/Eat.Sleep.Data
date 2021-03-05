from Data_Cleaning_Func import clean_airbnb_data

cal_table_raw = 'calendar'
listing_table_raw = 'listings_full'
cal_table_to_save = 'calendar_py_test'
listing_table_to_save = 'clean_listing_remove_somereviews'
amenities_table_to_save = 'amenities_py_test'

clean_airbnb_data(cal_table_raw, listing_table_raw, cal_table_to_save, listing_table_to_save, amenities_table_to_save)