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

def predict():
    # Import the model to a new object
    nn_imported = tf.keras.models.load_model('PricePredictionModel.h5')

    # Import test data
    X_test_scaled = np.genfromtxt('X_test_scaled.csv', delimiter=',')

    # Make predictions using the test data
    results = pd.DataFrame(nn_imported.predict(X_test_scaled))
    html = results.to_html()
    return html

def addition(input1, input2):
    result = input1 + input2
    return result

def summarize_inputs(address, neighborhood, property_type, room_type, bedrooms, beds, baths):
    # result = f"Address:{address}\nNeighborhood: {neighborhood}\nProperty Type: {property_type}\nRoom Type: {room_type}\nBedrooms: {bedrooms}\nBeds: {beds}\nBaths: {baths}"
    result = pd.DataFrame(  
                        data=[address, neighborhood, property_type, room_type, bedrooms, beds, baths], 
                        index=['Address', 'Neighborhood', 'Property Type', 'Room Type', 'Bedrooms', 'Beds', 'Baths'],
                        columns=["Inputs"]
                        )   

    html = result.to_html()                    
    return html
