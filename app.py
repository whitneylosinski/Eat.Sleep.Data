from flask import Flask, render_template, request
import airbnb_price_predict

app = Flask(__name__)

# Define the routes for the HTML page

# Default route
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    # my_input1 = request.form['input1']
    # my_input2 = request.form['input2']
    # input1 = int(my_input1)
    # input2 = int(my_input2)
    accommodates = request.form['selAccommodates']
    bedrooms = request.form['selBedrooms']
    baths = request.form['selBaths']
    # result = airbnb_price_predict.addition(input1, input2)
    result = airbnb_price_predict.predict(accommodates, bedrooms, baths)
    return render_template(
        "index.html",
        result = result
    )

if __name__ == "__main__":
    app.run()