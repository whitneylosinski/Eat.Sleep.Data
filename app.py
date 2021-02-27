from flask import Flask, render_template, request
import airbnb_price_predict

app = Flask(__name__)

# Define the routes for the HTML page

# Default route
@app.route("/")
def index():
    return render_template("index.html")

# Make prediction using ml model
@app.route("/predict")
def predict():
    price_prediction = airbnb_price_predict.predict()
    return price_prediction

# Get accuracy/loss info about ml model
@app.route("/info")
def get_model_info():
    model_info = airbnb_price_predict.model_loss_accuracy()
    return model_info

@app.route('/', methods=['POST'])
def my_form_post():
    # my_input1 = request.form['input1']
    # my_input2 = request.form['input2']
    # input1 = int(my_input1)
    # input2 = int(my_input2)
    address = request.form['address']
    neighborhood = request.form['neighborhood']
    property_type = request.form['selPropertyType']
    room_type = request.form['selRoomType']
    bedrooms = request.form['selBedrooms']
    beds = request.form['selBeds']
    baths = request.form['selBaths']
    # result = airbnb_price_predict.addition(input1, input2)
    result = airbnb_price_predict.summarize_inputs(address, neighborhood, property_type, room_type, bedrooms, beds, baths)
    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run()