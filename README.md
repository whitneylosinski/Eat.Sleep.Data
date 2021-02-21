
# **Eat.Sleep.Data - Predicting Airbnb Prices in Nashville** 
<hr>

### Summary
The purpose of this project is to analyze historical Airbnb data with machine learning models to predict the expected rental price of a given space based on location, size, amenities, reviews, host performance, and other relevant variables. This prediction model will be incorporated in a tool for property owners to use to determine the suggested rental price for their space. The model will incorporate seasonal trends and weekday versus weekend premiums to adjust the suggested price for the dates the space will be listed. Due to the short timeline for this project, the scope will be limited to the Nashville, TN market. 

**Team members:** Alex Conerly, Alex Felice, Betsy Wellington, Hannah Koivisto, Ken Liew, Whitney Losinski
<hr>

### Project proposal
Click the following link to view the full initial project proposal.  Note that the current scope of project has been changed from the initial proposal after data and technical exploration. 
- <a href= "https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/Project-Proposal">Project Proposal</a>

### Reason for selecting this topic
In order to find a project, the team scoured Kaggle datasets and other internet sources of data to find potential projects that were of interest to each member.  These potential projects and the associated datasets were added to a shared spreadsheet.  After collecting a number of potential projects, team members voted on the ones they were most interested in, ranking their top three choices.  The project that received the highest score was the Airbnb proposal.  This was initially proposed by a member who mentioned they had been thinking about hosting an Airbnb in their home and thought it might be interesting to find out how much rent they could get for it.  The abundance of data available in open sources for Airbnb also makes this a more manageable project to develop.  

### Questions we hope to answer with the data
Looking at the wide variety of data available, the team is interested in exploring how the price charged relates to various features of the dataset.  While we are initially exploring all of the variables available, the big question is what really makes a difference in the price that an Airbnb can command.  Here are some of the biggest features we hope to sort out:

*  Neighborhood
*  Room Type
*  Number of bedrooms/beds
*  Kitchen
*  Pet friendly
*  Time of year or day of week
*  etc.

### Description of Data Source
Click the following link to see a detailed description of the data sources being using for the project.  Additional information about our data exploration can be found in the project proposal above.
- <a href= "https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/ETL">Data Source</a>

### Preliminary Machine Learning Model
Our first pass at an MLM uses a linearRegressor model with multiple variables thus becoming  a multiple regression.  A description and link to this model can be found here:

![MLR Model](https://github.com/whitneylosinski/Eat.Sleep.Data/blob/mlr_model/mlr_model.ipynb)

Because the initial model came in with an R2 score of .57 which is not high enough, we ran a multi-collinearity matrix and found there are numerous variables with significant collinearity.  We have begun the process of re-examining the input variables to correct for this.

In addition, we are trying a Random Forest model because this type of model:

*  Is robust against overfitting because the weak learners are trained on different pieces of the data.
*  Can be used to rank the importance of input variables in a natural way.
*  Can handle thousands of input variables without variable deletion.
*  Is robust to outliers and nonlinear data.
*  Run efficiently on large datasets

Since our data set has a large number of input variables, the RF model should be able to better separate the predictors from the non-predictors.  

A link to our preliminary model is here:

![RF Model](https://github.com/whitneylosinski/Eat.Sleep.Data/blob/mlr_model/mlr_model_Random_Forest_Regressor%20copy.ipynb)

For more indepth discussion of the MLMs, click on this link:

![MLM Wiki page](https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/Machine-Learning-Model-Development)

### Communication Protocols
Our team is using the following mediums for communication purposes:
 - **Discord** - for messaging and basic communication.  Our discord board includes a "general" tab for informational messages, a "data-discovery" tab for information on datasets, and "important_and_useful_links" for the links to the sourced database, the Postgres database, the web app and any other important links.  We also have the ever important "off-topic" tab for general socializing. 
 - **Zoom** - for team meetings and video conferencing.  Our zoom calls consist of both scheduled and impromptu meetings set up through our Discord channel.
 - **Trello** - for organizing and documenting tasks.  Our board can be viewed <a href= "https://trello.com/eatsleepdata">here.</a>
 - **Github** - for programming and collaborative work. 
   *   Branches - team members have decided to forgo individual named branches and create topic based branches.  Any member named branches are used for their own discovery and scribbles. 


