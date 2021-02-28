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
    property_type = request.form['selPropertyType']
    room_type = request.form['selRoomType']
    accommodates = request.form['selAccommodates']
    bedrooms = request.form['selBedrooms']
    beds = request.form['selBeds']
    baths = request.form['selBaths']
    # result = airbnb_price_predict.addition(input1, input2)
    result = airbnb_price_predict.predict(district, property_type, room_type,accommodates, bedrooms, beds, baths)
    return render_template(
        "index.html",
        result = result
    )

if __name__ == "__main__":
    app.run()