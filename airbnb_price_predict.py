import pandas as pd
import tensorflow as tf
import numpy as np

# def model_loss_accuracy():
#     # Import the model to a new object
#     nn_imported = tf.keras.models.load_model('PricePredictionModel.h5')

#     # Import test data
#     X_test_scaled = np.genfromtxt('X_test_scaled.csv', delimiter=',')
#     y_test = np.genfromtxt('y_test.csv', delimiter=',')

#     # Evaluate the model using the test data
#     model_loss, model_accuracy = nn_imported.evaluate(X_test_scaled,y_test,verbose=2)
#     results = f"Loss: {model_loss}, Accuracy: {model_accuracy}"
#     return results

def predict(district,accommodates, bedrooms, baths, host_listings_count,security_deposit,cleaning_fee,reviews_per_month,number_of_reviews,guests_included):
    # Final Features:
    # 1. 'bathrooms',
    # 2. 'cleaning_fee',
    # 3. 'accommodates',
    # 4. 'host_listings_count',
    # 5. 'bedrooms',
    # 6. 'reviews_per_month',
    # 7. 'neightborhood_cleansed_District 19'
    # 8. 'security_deposit'
    # 9. 'number_of_reviews'
    # 10. 'guests_included'

    # Test opening saved model and run prediction
    import pickle
    filename = 'rfr_model_post_feat_sel_2.pickle'

    with open(filename, 'rb') as file:
        pickle_model = pickle.load(file)

    if (int(district)==19):
        neighbourhood_cleansed_District_19 = 1
    else:
        neighbourhood_cleansed_District_19 = 0

    if (host_listings_count==0):
        host_listings_count=1

    if (guests_included==0):
        guests_included=1
    # Aggregate test data and reshape
    X_test = [host_listings_count, accommodates, baths, bedrooms,security_deposit, cleaning_fee, guests_included,number_of_reviews, reviews_per_month,neighbourhood_cleansed_District_19]
    X_test = np.array(X_test)
    X_test = X_test.reshape(1,-1)
    # Make predictions using the test data
    result = pickle_model.predict(X_test)
    return int(round(result[0],0))

# def addition(input1, input2):
#     result = input1 + input2
#     return result

# def summarize_inputs(districts, property_type, room_type, accommodates, bedrooms, beds, baths):
#     # result = f"Address:{address}\nNeighborhood: {neighborhood}\nProperty Type: {property_type}\nRoom Type: {room_type}\nBedrooms: {bedrooms}\nBeds: {beds}\nBaths: {baths}"
#     result = pd.DataFrame(  
#                         data=[districts, property_type, room_type, bedrooms, beds, baths], 
#                         index=['Districts', 'Property Type', 'Room Type',  'Bedrooms', 'Beds', 'Baths'],
#                         columns=["Inputs"]
#                         )                  
#     return result
