import pandas as pd
import tensorflow as tf
import numpy as np

def model_loss_accuracy():
    # Import the model to a new object
    nn_imported = tf.keras.models.load_model('PricePredictionModel.h5')

    # Import test data
    X_test_scaled = np.genfromtxt('X_test_scaled.csv', delimiter=',')
    y_test = np.genfromtxt('y_test.csv', delimiter=',')

    # Evaluate the model using the test data
    model_loss, model_accuracy = nn_imported.evaluate(X_test_scaled,y_test,verbose=2)
    results = f"Loss: {model_loss}, Accuracy: {model_accuracy}"
    return results

def predict(district,accommodates, bedrooms, baths, host_listings_count,security_deposit,cleaning_fee,reviews_ltm,host_days,essentials_chk):
    # Clean inputs from webpage
    # ['host_listings_count', 'accommodates', 'bathrooms', 'bedrooms',
    #    'security_deposit', 'cleaning_fee', 'number_of_reviews_ltm',
    #    'reviews_per_month', 'days_host', 'essentials',
    #    'neighbourhood_cleansed_District 19']
    # Test opening saved model and run prediction
    import pickle
    filename = 'rfr_model_post_feat_sel_2.pickle'

    with open(filename, 'rb') as file:
        pickle_model = pickle.load(file)

    if (district==19):
        neighbourhood_cleansed_District_19 = 1
    else:
        neighbourhood_cleansed_District_19 = 0

    if (host_listings_count==0):
        host_listings_count=1

    if (host_days==0):
        host_days=2
    
    if (essentials_chk == 'essentials'):
        essentials = 1
    else:
        essentials = 0
    #  host_listings_count = 76
    # security_deposit = 183
    # cleaning_fee = 96
    # number_of_reviews_ltm = 23
    reviews_per_month = int(reviews_ltm)/12
    # days_host = 1199
    # essentials = 1
    neighbourhood_cleansed_District_19 = 0
    # Aggregate test data and reshape
    X_test = [host_listings_count,accommodates,baths,bedrooms,security_deposit,cleaning_fee,reviews_ltm,reviews_per_month,host_days,essentials,neighbourhood_cleansed_District_19]
    X_test = np.array(X_test)
    X_test = X_test.reshape(1,-1)
    # Make predictions using the test data
    result = pickle_model.predict(X_test)
    return round(result[0],2)

def addition(input1, input2):
    result = input1 + input2
    return result

def summarize_inputs(districts, property_type, room_type, accommodates, bedrooms, beds, baths):
    # result = f"Address:{address}\nNeighborhood: {neighborhood}\nProperty Type: {property_type}\nRoom Type: {room_type}\nBedrooms: {bedrooms}\nBeds: {beds}\nBaths: {baths}"
    result = pd.DataFrame(  
                        data=[districts, property_type, room_type, bedrooms, beds, baths], 
                        index=['Districts', 'Property Type', 'Room Type',  'Bedrooms', 'Beds', 'Baths'],
                        columns=["Inputs"]
                        )                  
    return result
