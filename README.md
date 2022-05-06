# Big-Data-Group4
This project is a part of the ITCS 6100 - Big Data Analytics for Competitive Advantage course from the University of North Carolina at Charlotte.

# Team Members
* Karan Issrani
* Dhruv Jani
* Dhruvil Patel
* Mohit Gupta
* Yaw Frempong

# Communication plan
We plan to communicate 3 times per week through zoom or in-person meetings based on the availability of the group members. The meetings will last for 2-3 hrs each.

# Selection of data
This dataset comprises movie ratings and has 1 lakh entries. This is prescribed by AWS \
https://grouplens.org/datasets/movielens/

# Business Problem or Opportunity, Domain Knowledge
Business Problem/Opportunity - Recommendation algorithms are at the core of the Netflix, Prime and Hulu products. They provide our members with personalised
suggestions to reduce the amount of time and frustration to find something great content to watch. \
Link - https://research.netflix.com/research-area/recommendations

Domain Knowledge - Recommender systems are Machine Learning techniques that serve the best advice for a potential buyer. They suggest the most relevant items to
buy and, as a result, increase a company's revenue. These suggestions are based on users' behaviour and history that contain information on their past preferences.

# Research Objectives and Question(s) 
We plan to preprocess the data and design our own recommendation system, choosing our algorithm. We are trying to describe the taste in movies for an individual based on the previous observations we obtain a trend and predict a movie based on the data we have. For this, we will make use of ML Algorithms in AWS Sagemaker. By doing this we aim to answer the following questions: \
What did the user like in the past ?(describe the user) \
What will the user like in the future? (Prediction) 

# Data Understanding
The Data we have was divided in 4 different files. The link of the data we used is https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
The data is divided into links.csv, movies.csv, tags.csv and ratings.csv

We used the primary key Movie ID to merge these data files and form our data set. Our data
set consists of 100000 entries. The dataset merged_data.csv has all the data in it. Our data
has movieId,imdbId,tmdbId,title,genres,rating,userId,tag,timestamp,userId column names
respectively.

Now we do exploratory data Analysis on our dataset.
## Exploratory Data Analysis
We use AWS Quick sight for our exploratory data analysis.
![image](https://user-images.githubusercontent.com/78280206/164281892-807dc052-e76f-4edb-bc09-d314f9783a41.png)
The graph above is the pie chart for representing the movies by genres. Here we can see
that a large number of movies dont have one unique genre. But lie in the others category.
The others category here represents that a large proportion of movies has more than one
genre.

![image](https://user-images.githubusercontent.com/78280206/164281984-bc898fd3-6bfd-4f78-91e3-31c5929e713a.png)
Here we see the graph of ratings vs tags. The artists who have the highest to lowest ratings
are given below. This gives us an idea of the peoples choice. We can see that in our data
Morgan Freeman has the highest number of ratings. This also gives us an idea that the
graph is skewed. Tags can’t be considered as a feature in our model.

![image](https://user-images.githubusercontent.com/78280206/164282054-956035cc-7d98-43e3-85ee-95cde9ae51c7.png)

Here we plot the pie diagram to represent the number of ratings by genres. This is an
interesting plot which shows us that which genres united together gives the best combination
and has the highest rating. Our data says that the movies having genres like Comedy,
Criminal, Drama and Thriller are the highest rated movies among users. The movies with
Action genre precede these choices. The least preferred genre would be a combination of
Criminal, Mystery, Thriller and Adventure movies. These features give the recommendation
system a clear idea of what the preferences are in similar audience.

![image](https://user-images.githubusercontent.com/78280206/164282102-0b5944a8-d711-4ca8-88c7-2889a5e1a666.png)

The most important relation of all is the title and ratings analysis. This graph shows us the
average ratings for a movie out of 5. The favourites and relevant favourites can be mapped
through this. Our main aim is to take the users input and based on the input give similar
movies that might be the users favourite or are rated similar by the other users.

![image](https://user-images.githubusercontent.com/78280206/164282143-efc1d5e4-0dd1-4cca-acf5-fe6f4473e3f2.png)

Average of Ratings by Genre and Title this tells us the value of these 3 features in our
model. This clearly shows that our data is ready to undergo further process. Each movie can
be distinguished as to which movie belongs to which genre and what rating it scores in its
genre.

## Dashboard
The link to the dashboard is
https://us-east-1.quicksight.aws.amazon.com/sn/accounts/530834130991/dashboards/1b211
208-2faf-4afd-844a-6dc13bcfe64f?directory_alias=yawfrempong

Since it is a private instance. It cant be accessed by others.
The screenshot below will show how the dashboard in Quicksight Looks.
![image](https://user-images.githubusercontent.com/78280206/164282254-8af97564-dcc0-494a-9871-ed69d11f82c8.png)

### Data Preparation
* Step 1 \
We use Sage maker for the data preparation process and data cleaning process. We take
Imports that are required for the process
![image](https://user-images.githubusercontent.com/78280206/164282419-de5ca703-5e1a-4648-9011-4431c5a3f73c.png)

* Step 2 \
We need to Create an S3 bucket where all our csv files will be stored. We write simple
python code to get the csv files. Convert them to dataframes and merge these data frames
to get the required data set.
![image](https://user-images.githubusercontent.com/78280206/164282497-44d0e403-9620-4d53-a249-6abf9bf1ff33.png) \
In this code we check if the region is us-east-1 so that our account location matches the S3
bucket location.
![image](https://user-images.githubusercontent.com/78280206/164282521-2237bf6f-1aa6-4987-b1af-5685ce2cc226.png) \
We get the file merged_data after merging the files we need for our analysis. Here MovieId
is the primary key for movies.csv and a foreign key in all other csvs.

* Step 3 \
Check our S3 folder has been created. This folder will have our S3 repository and all other
data. The folder now also has the newly merged data file.The recommendation-storage is
the bucket we need.
![image](https://user-images.githubusercontent.com/78280206/164282610-0497f2a0-6653-4852-bbdd-86c87beff6f4.png)

* Step 4 \
We can write a json code to take our data
![image](https://user-images.githubusercontent.com/78280206/164282687-b8cd2ce4-06ea-4c50-961e-63c3c9e1e8fc.png)

* Step 5 \
Now we read the newly merged csv file to perform further cleaning of data according to our
needs.
![image](https://user-images.githubusercontent.com/78280206/164282744-13240e36-fdc8-4c61-a91a-373990bb7ac7.png)

* Step 6 \
![image](https://user-images.githubusercontent.com/78280206/164282793-d4b895e5-caf9-4330-90d7-aab5faa1d418.png)

In this step, we define two variables in the dataset to filter out unliked movies and better
simulate data gathered by a video-on-demand (VOD) platform.

Since this is an explicit feedback movie rating dataset, it includes movies rated from 1 to 5. For
this tutorial, we want to include only moves that were "liked" by the users, and simulate a
implicit dataset that is similar to data that is gathered by a video-on-demain (VOD) platform. For
that, you will next filter out all interactions below 2 out of 5, and create two EVENT_TYPE
variables: click and watch. Any movies rated 2 and above are assigned as click, and any
movies rated 4 and above are assigned as click and watch.

This is the final step for our data cleaning. We get the data like we want from here.
Further, We will choose a ML algorithm to do further processes.

The AWS features we used are:- \
AWS S3 \
AWS SAGE MAKER \
AWS QuickSight \

Sources \
https://grouplens.org/datasets/movielens/ \
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html \
https://numpy.org/ 

# Phase 3

## Analytics, Machine Learning

Here, We selected the KMeans Clustering algorithm. k-means clustering is a vector
quantization method that seeks to partition n observations into k clusters, with each
observation belonging to the cluster with the nearest mean (cluster centers or cluster
centroid), which serves as the cluster's prototype. As a result, the data space is partitioned
into Voronoi cells. Within-cluster variances (squared Euclidean distances) are minimized by
k-means clustering, but regular Euclidean distances are not, which is the more difficult
Weber problem: the mean optimizes squared errors, while only the geometric median
reduces Euclidean distances. Using k-medians and k-medoids, for example, better
Euclidean solutions can be obtained.

We made use of the K-means clustering algorithm from sklearn python library.

![image](https://user-images.githubusercontent.com/78280206/167052428-e56aa843-d706-4c89-b682-c2df43a4344d.png)

### Analytics

We also gave our code a front end to make the model interactive. We made use of Streamlit for this UI. 
Streamlit is a python library making it easy to make our Machine Learning models interactive.
Here, we plotted a few analytical graphs and also took the users input to make real-time recommendations.

#### Average Ratings vs types of formats
![image](https://user-images.githubusercontent.com/78280206/167052511-35cde9aa-2fcf-4c64-845a-ad65fb558df0.png)

#### Number of Movies in the dataset with respect to genres
![image](https://user-images.githubusercontent.com/78280206/167052876-935ba2d1-045c-492b-8f06-33eadce21dfe.png)

## Evaluation and Optimization
### Evaluation
We broke the code into three portions to make recommendations.
* Weighted Scores
* Clustering
* The Last Function

To begin, we'll utilize a weighted rating system to assign a rating to each piece of data based on the average rating and number of votes. The following is the formula for calculating weighted rating:
We use the Weighted rating formula for our analysis
W=(v/(v+m) * M) + (m/(m+v) * C)
Where:
M = Mean for the video format
v = number of votes for the video format
m = minimum votes required to be counted
C = the mean vote across the whole dataset

### Optimization
We need a boolean column for all the Genres for that we'll make a new column for each genre and assign a value of 1 or 0 to it based on the value.
There will be a total of 38 columns created.
We'll use a scaler to standardize the data in the all genres column.
It converts the data so that the mean is 0 and the standard deviation is 1.
In a nutshell, it normalizes the data. For data with negative values, standardization is beneficial.
It uses a typical normal distribution to organize the data.
![image](https://user-images.githubusercontent.com/78280206/167053215-4f23c076-ed7b-4019-9154-9dd5b98a2005.png)


## Results
* We make the famous elbow graph for our data and try to see which value of k is feasible for us. 
* When we see the graph we see that we that after k=23 the values go down linearly. For further process, We will make use of K=23. Now we'll utilize the k-means cluster to forecast the clustering result. This will assist us in making genre-based recommendations.
* We consider 5 parameters for our recommendation. At least one argument must be presented. A title is a movie/show name, a type is a video format, a rating is the minimum rating required, a year is a specific year search, and a genre is a genre name, and it will recommend up to 10 titles based on the arguments provided.
![image](https://user-images.githubusercontent.com/78280206/167053300-c7eba80a-1e9c-4817-b442-e697209db4d1.png)
![image](https://user-images.githubusercontent.com/78280206/167053305-0344d1c2-204b-4ba2-837b-d3fc38473415.png)

## Future Work, Comments   
The data we selected was not from Kaggle, but it was the official data from IMDb. The dataset was huge. The free instance of Sagemaker won’t process so much data. So we reduced the size of our data. The datasets were tab spaced versions and had a const id column, making it easy to merge 2 datasets and make a dataset we require.
The dataset we merged had a single column of genres. As we wanted separate values. We added more columns to the dataset and each column represented a genre. The input in these columns was boolean to make it easier for us to process the data. We also removed some null values present in the dataset.
As the dataset was otherwise clean, We didn’t have to deal with outliers of any kind.
The imbd has some movies whose genre is not known. We cant categorize this data and we need further information on these movies to know the genre. We leave them as N for now. \
Some important points.
* Did you create any new additional features/variables?
Yes, We created a few features for our genres.
* What was the process you used for evaluation?  What was the best result?
We used the K-means clustering algorithm till convergence and then we used the clusters for further recommendation analysis.
* What were the problems you faced? How did you solve them?
If this is a funded project then you can freely use the AWS resources. In college-level instances, you can't have a large dataset and you can’t build a pipeline. The data cant is kept in s3 because for every access you will call the S3 storage. This may incur charges on your account. The dataset we choose must have appropriate data. If not, the accuracy of the model declines. To develop a project like this you need to have knowledge of Machine Learning algorithms and AWS. We used a private account for our process and made which caused fewer problems. We selected the datasets which had appropriate data and were from a legitimate source. 
* What future work would you like to do? 
In the future, We can do regression analysis on the data. The dataset had a lot of movies without a genre. We will try to label the data there. We can also shift to graphical databases for processing unstructured data. Further enhancements are possible to give it a professional-looking UI.
* Instructions for individuals that may want to use your work:-
1.	Make sure you install all the necessary python libraries before working on the code.
2.	Find a good dataset with enough rows and relevant columns.
3.	While creating an S3 Bucket and a new notebook instance make sure to use a new IAM role and store data in a random s3 bucket.
4.	Use a good processing instance for higher processing power.
5.	There are 2 Jupyter notebooks. You can use our code on your local machine as well as a notebook for AWS instance.
6.	Read about the boto library for using AWS.
7.	We created a separate python file for Streamlit.
