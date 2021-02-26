
# **Eat.Sleep.Data - Predicting Airbnb Prices in Nashville** 
<hr>

## Project Overview
The purpose of this project is to analyze historical Airbnb data with machine learning models to predict the expected rental price of a given space based on location, size, amenities, reviews, host performance, and other relevant variables. This prediction model will be incorporated in a tool for property owners to use to determine the suggested rental price for their space. The model will incorporate seasonal trends and weekday versus weekend premiums to adjust the suggested price for the dates the space will be listed. Due to the short timeline for this project, the scope will be limited to the Nashville, TN market. 

**Team members:** Alex Conerly, Alex Felice, Betsy Wellington, Hannah Koivisto, Ken Liew, Whitney Losinski
<hr>

## Project Proposal
Click the following link to view the full initial project proposal.  Note that the current scope of project has been changed from the initial proposal after data and technical exploration. 
- <a href= "https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/Project-Proposal">Project Proposal</a>

## Reason for Selecting this Topic:
In order to find a project, the team scoured Kaggle datasets and other internet sources of data to find potential projects that were of interest to each member.  These potential projects and the associated datasets were added to a shared spreadsheet.  After collecting a number of potential projects, team members voted on the ones they were most interested in, ranking their top three choices.  The project that received the highest score was the Airbnb proposal.  This was initially proposed by a member who mentioned they had been thinking about hosting an Airbnb in their home and thought it might be interesting to find out how much rent they could get for it.  The abundance of data available in open sources for Airbnb also makes this a more manageable project to develop.  

## Questions we Hope to Answer with the Data:
Looking at the wide variety of data available, the team is interested in exploring how the price charged relates to various features of the dataset.  While we are initially exploring all of the variables available, the big question is what really makes a difference in the price that an Airbnb can command.  Here are some of the biggest features we hope to sort out:

* Neighborhood
*  Room Type
*  Number of bedrooms/beds
*  Kitchen
*  Pet friendly
*  Time of year or day of week
*  etc.

## Description of Data Source:
Click the following link to see a detailed description of the data sources being using for the project.  Additional information about our data exploration can be found in the project proposal above.
- <a href= "https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/ETL">Data Source</a>

## Drafts of Machine Learning Model:
Our preliminary model testing before the feature reduction process included two separate tests.  Our first pass at an MLM used a linearRegressor model with multiple variables, thus becoming multiple regression.  A description and link to viewing this model can be found here:

- <a href= "https://github.com/whitneylosinski/Eat.Sleep.Data/blob/mlr_model/mlr_model.ipynb">MLR Model</a>

The output label for the input data (screenshot of predicted "y") for the MLR model can be viewed as follows:

- <a href= "https://github.com/whitneylosinski/Eat.Sleep.Data/blob/main/PNGs/baseline_MLR_predicted_y.png">Preliminary MLR predicted "y"</a>

This initial model produced an R-squared value 0.57, which is not high enough for predictive reliability.  As such, we decided to also try a random forest regressor.  Since our data set has a large number of input variables, the RF model should be able to better separate the predictors from the non-predictors.  Some additional motivations for using a random forest regression model were as follows:

* They can sometimes be less prone to overfitting
*  Can be used to rank the importance of input variables in a natural way.
*  Can handle thousands of input variables without variable deletion.
*  Are robust to outliers and nonlinear data.
*  Run efficiently on large datasets

From the random forest regressor, we achieved an R-squared value from a testing set of about 0.95 which was suspiciously high.  Hence, we also calculated the "adjusted" R-squared value which penalizes the original R-squared value for having excess features but even after incorporating the adjustment formula, the numerical difference from the original R-squared value was neglible.  Finally, we ran an additional calculation to determine the mean squared error which resulted in a value of about 2983.10.  This means that, on average, this model's price prediction was off by about $53.86.

To view this preliminary Random Forest Regressor model, follow the link below:
- <a href = "https://github.com/whitneylosinski/Eat.Sleep.Data/blob/Baseline_Model_Testing/Baseline_Model_Testing_files/Baseline_Random_Forest_Regressor.ipynb">Random Forest Model</a>


Following these two baseline tests, additional tests are in the planning stage, including tweaking of the hyperparameters, to further reduce predictive errors as well as minimize overfitting to the models.  Furthermore, the group collaborated on producing a multi-collinearity matrix which revealed numerous variables in the dataset with significantly high collinearity.  With the aid of this matrix, we have begun the process of re-examining the input variables to fine-tune the feature selection and reduction process.

For a more indepth discussion of the MLMs, follow this link:

- <a href = "https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/Machine-Learning-Model-Development">MLM_wiki_link</a>

## Connection of draft model to Postgres Database:

Both the draft models are linked to the Heroku postgres database and running properly as shown in the following image:

- <a href = "https://github.com/whitneylosinski/Eat.Sleep.Data/wiki/Database">Postgres Database Example</a>

## Communication Protocols:
Our team is using the following mediums for communication purposes:
 - **Discord** - for messaging and basic communication.  Our discord board includes a "general" tab for informational messages, a "data-discovery" tab for information on datasets, and "important_and_useful_links" for the links to the sourced database, the Postgres database, the web app and any other important links.  We also have the ever important "off-topic" tab for general socializing.
 - **Zoom** - for team meetings and video conferencing.  Our zoom calls consist of both scheduled and impromptu meetings set up through our Discord channel.
 - **Trello** - for organizing and documenting tasks.  Our board can be viewed <a href= "https://trello.com/eatsleepdata">here.</a>
 - **Github** - for programming and collaborative work. 
   *   Branches - team members have decided to forgo individual named branches and create topic based branches.  Any member named branches are used for their own discovery and scribbles. 


## Presentation

We are using google slides for our presentation.  This is not something that is compatible with uploading to Github so click on the link below to access the working draft of the presentation:

{google_docs}https://docs.google.com/presentation/d/e/2PACX-1vSXOcxM3okHa9elmUrgC4XSIVFDAI0BqpKFPFavd9fuoEGvCoXLyWOU1hlPmIZydc78vxWU6Wf-O15u/pub?start=false&loop=false&delayms=3000{/google_docs}



