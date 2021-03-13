from flask import Flask, render_template, request
import airbnb_price_predict

app = Flask(__name__)

# Define the routes for the HTML page

# Default route
@app.route("/")
def index():
    return render_template(
        "index.html",
        district = 1,
        accommodates = 1,
        bedrooms = 1,
        baths = 1,
        host_listings_count = 0,
        security_deposit = 100,
        cleaning_fee = 50,
        reviews_per_month = 0,
        number_of_reviews = 0,
        guests_included = 1
        )


@app.route('/', methods=['POST'])
def my_form_post():
    # my_input1 = request.form['input1']
    # my_input2 = request.form['input2']
    # input1 = int(my_input1)
    # input2 = int(my_input2)
    district = int(request.form['selDistrict'])
    accommodates = int(request.form['selAccommodates'])
    bedrooms = int(request.form['selBedrooms'])
    baths = float(request.form['selBaths'])
    host_listings_count = int(request.form['host_listings_count'])
    security_deposit = int(request.form['security_deposit'])
    cleaning_fee = int(request.form['cleaning_fee'])
    reviews_per_month = int(request.form['reviews_per_month'])
    number_of_reviews = int(request.form['number_of_reviews'])
    guests_included = int(request.form['guests_included'])
    # result = airbnb_price_predict.addition(input1, input2)
    result = airbnb_price_predict.predict(district,accommodates, bedrooms, baths, host_listings_count,security_deposit,cleaning_fee,reviews_per_month,number_of_reviews,guests_included)
    return render_template(
        "index.html",
        result = result,
        district = district,
        accommodates = accommodates,
        bedrooms = bedrooms,
        baths = baths,
        host_listings_count = host_listings_count,
        security_deposit = security_deposit,
        cleaning_fee = cleaning_fee,
        reviews_per_month = reviews_per_month,
        number_of_reviews = number_of_reviews,
        guests_included = guests_included
    )

if __name__ == "__main__":
    app.run()