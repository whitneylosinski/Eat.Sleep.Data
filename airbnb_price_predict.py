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

def predict(districts, property_type, room_type, accommodates, bedrooms, beds, baths):
    # Clean inputs from webpage
    
    # Test opening saved model and run prediction
    import pickle
    filename = 'rfr_model_post_feat_sel.pickle'

    with open(filename, 'rb') as file:
        pickle_model = pickle.load(file)

    # Aggregate test data and reshape
    X_test = [1,accommodates,baths,bedrooms,0,50,2.5,1,1,1,0,1,1,6,0,0,0,1,0,1]
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
