from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run()