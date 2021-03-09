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
    district = request.form['selDistrict']
    accommodates = request.form['selAccommodates']
    bedrooms = request.form['selBedrooms']
    baths = request.form['selBaths']
    host_listings_count = request.form['host_listings_count']
    security_deposit = request.form['security_deposit']
    cleaning_fee = request.form['cleaning_fee']
    reviews_ltm = request.form['reviews_ltm']
    host_days = request.form['host_days']
    essentials_chk = request.form['essentials_chk']
    # result = airbnb_price_predict.addition(input1, input2)
    result = airbnb_price_predict.predict(district,accommodates, bedrooms, baths, host_listings_count,security_deposit,cleaning_fee,reviews_ltm,host_days,essentials_chk)
    return render_template(
        "index.html",
        result = result
    )

if __name__ == "__main__":
    app.run()