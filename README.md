# **Eat.Sleep.Data - Predicting Airbnb Prices in Nashville** 
<hr>

**Team members:** Alex Conerly, Alex Felice, Betsy Wellington, Hannah Koivisto, Ken Liew, Whitney Losinski
<hr>

## **Project Background and Objectives** 

Airbnb is a popular internet marketplace for short term home and apartment rentals. It allows ordinary people who own properties to list their empty spaces for rent and provides a one stop marketplace to renters who are looking for their perfect short term home.  The site provides a great selection of listings that can be filtered by locations, price, size, amenities and more so that renters can narrow down their search to their exact needs.

Although Airbnb provides hosts with general guidelines when listing a property, the site does not provide an easy way for hosts to determine the optimal price of their rental space to ensure they are making maximum profits while also not overcharging or driving renters away from their listing.  There are many current options that allow hosts to determine their optimal rental price but most of them are through third-party websites who charge a hefty price for their resources.  

The purpose of this project is to utilize historical Airbnb data with machine learning models to predict the optimal rental price of a given space based on location, size, amenities, reviews, host performance, etc. This prediction can be framed not only as a tool for a property owner to determine the optimal rental price for their space, but also as a tool for potential customers to identify if the asking price for a listing they are interested in is a fair value. The model will also incorporate seasonal tourism trends, automatically adjusting the suggested price based on historical tourism trends for the dates the space will be listed/rented. Due to the short timeline for this project, the scope will be limited to only the Nashville, TN area and its surrounding suburbs. 

## **Data Exploration** 
 
Because the Airbnb website no longer allows users to apply for access to their API for collecing data, the team researched several other potential data sources for the project and found that the following sites offer the data the team needs for this project. 
 
1. Inside Airbnb: http://insideairbnb.com/get-the-data.html </br>
   Includes over 7,000 Airbnb listings for 2019 in the Nashville, TN area with more than [est. number of columns] features for each listing.  The dataset includes features such as listing type, location, neighborhood, number of bedrooms, maximum occupency, amenities, availability, host response time, reviews, etc.  More current listings, as recent as 2021, are available as well but the team has decided to use 2019 data, as it has not been impacted by travel trends due to COVID-19.
   
2. Tourism trends: 
   

There were also several other data resources found by the team that were not chosen for various reasons as detailed below.

1. Kaggle US Airbnb Open Dataset: https://www.kaggle.com/kritikseth/us-airbnb-open-data </br>
   Contained over 218,000 listings from Airbnb in 2020 with 17 features for each listing including host information, location, room type, price, minimum number of nights, reviews, availability and city.  This dataset was rejected due to the very limited information on amenities and other features.
   
2. opendatasoft Airbnb Dataset: https://public.opendatasoft.com/explore/dataset/airbnb-listings/table/ </br>
   Includes nearly 500,000 Airbnb listings from all around the world between 2015 and 2017.  This dataset was not chosen becuase the team wanted to use more current data.
   
3. Weather data: https://openweathermap.org/history
   Weather was considered as an additional impact on the optimal price but the team decided to look at tourism trends rather than weather for the model.
   





## **User Inputs** 

City (choose between 3 options) 

Number of Rooms 

Number of Beds 

Number of Bathrooms 

Neighborhood within chosen city 

Month 


