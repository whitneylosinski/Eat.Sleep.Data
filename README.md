
# **Eat.Sleep.Data - Predicting Airbnb Prices in Nashville** 
<hr>

## SUMMARY
The purpose of this project is to analyze historical Airbnb data with machine learning models to predict the optimal rental price of a given space based on location, size, amenities, reviews, host performance, and other relevant variables. This prediction model will be incorporated in a tool for property owners to use to determine the optimal rental price for their space and for customers to identify if the rental price for a listing is a fair value. The model will incorporate seasonal tourism trends and attractions to adjust the suggested price for the dates the space will be listed or rented. Due to the short timeline for this project, the scope will be limited to the Nashville, TN market. 

**Team members:** Alex Conerly, Alex Felice, Betsy Wellington, Hannah Koivisto, Ken Liew, Whitney Losinski
<hr>

## **Project Background** 

Airbnb is a popular internet marketplace for short term room, home and apartment rentals. It allows ordinary people who own properties to list their empty spaces for rent and provides a one stop marketplace for renters who are looking for their perfect short term home.  The site provides a great selection of listings that can be filtered by location, price, size, amenities and more so that renters can narrow down their search to their exact needs.

Although Airbnb provides hosts with general guidelines when listing a property, the site does not provide an easy way for hosts to determine the optimal price of their rental space to ensure they are making maximum profits while also not overcharging or driving renters away from their listing.  There are many current options that allow hosts to determine their optimal rental price but most of them are through third-party websites who charge a hefty price for their resources.  

## **Data Exploration** 
 
Because the Airbnb website no longer allows users to apply for access to their API for collecing data, the team researched several other potential data sources for the project and found that the following sites offer the data the team needs for this project. 
 
1. Inside Airbnb: http://insideairbnb.com/get-the-data.html </br>
   Includes over 7,000 Airbnb listings for 2019 in the Nashville, TN area with more 74 features for each listing.  The dataset includes variables such as listing type, location, neighborhood, number of bedrooms, maximum occupency, amenities, availability, host response time, and reviews.  More current listings, as recent as 2021, are available as well but the team has decided to use 2019 data, as it has not been impacted by travel trends due to COVID-19.
   
2. Tourism trends: 

*  https://data.tn.gov/api/action/datastore_search  
   This data includes tourism related tax receipts by county.  There is a date stamp that we can use to determine seasonality.
   
*  https://www.songkick.com/developer/upcoming-events-for-metro-area 
   This data source includes a calendar of upcoming music events.
*  https://opentripmap.io/product
   This source is a worldwide point of interest database for travel and entertainment.  It is open source so should be free.  We will be exploring this.
*  https://www.visitmusiccity.com/
   This website has all the Nashville attractions by neighborhood.  Using this will require webscraping.
   
   
There are also several other data resources found by the team that were not chosen for various reasons as detailed below.

1. Kaggle US Airbnb Open Dataset: https://www.kaggle.com/kritikseth/us-airbnb-open-data </br>
   Contained over 218,000 listings from Airbnb in 2020 with 17 features for each listing including host information, location, room type, price, minimum number of nights, reviews, availability and city.  This dataset was rejected due to the very limited information on amenities and other features.
   
2. opendatasoft Airbnb Dataset: https://public.opendatasoft.com/explore/dataset/airbnb-listings/table/ </br>
   Includes nearly 500,000 Airbnb listings from all around the world between 2015 and 2017.  This dataset was not chosen becuase the team wanted to use more current data.
   
3. Weather data: https://openweathermap.org/history
   Weather was considered as an additional impact on the optimal price but the team decided to look at tourism trends rather than weather for the model.
   

### Technology

Our initial technology plan includes the following:
1.  Database created with Postgres hosted on Heroku
2.  Programming in Python/Pandas
3.  Visualization with Matplotlib
4.  Statistical evaluation with additional visualizations in R
5.  Web app created using Javascript and deployed on Heroku
6.  Map visualizations using MapBox API and OpenStreetMap

### Communication
 
Our team will be using Discord for messaging with team meetings on Zoom.  We will be doing our programming and collaborative work via Github.  


<a href= "https://trello.com/eatsleepdata">trello link<a>


