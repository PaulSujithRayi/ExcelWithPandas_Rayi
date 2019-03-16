#We will be performing our data analysis using pandas
#We are now installing a number of python modules which will be helpful for data analysis
#First let us import pandas into our local namespace
import pandas as pd
#Now let us import dataframe data structures from pandas. This will be used for our data analysis.
from pandas import DataFrame
#Next we will be importing matplotlib.pyplot module which will be used in data visualization
import matplotlib.pyplot as plt
#Next we will be importing NumPy package for numerical data functionality
import numpy as np 
#Next we will be importing xlrd package for reading excel data
import xlrd 
#Next we will be importing xlwt package for writing excel data
import xlwt
#We are now storing our excel dataset in a variable
excel_file = 'suicides.xlsx'
#Now we are using the pandas' read_excel method to read in the dataset and stroe it in a variable called suicides
suicides = pd.read_excel(excel_file)
#Let us look at the first ten rows of our data set using the head function and print the output to console
print(suicides.head(10))
#Let us look at the number of rows and columns in our data frame using shape function and printing it to the console
print(suicides.shape)
#If you look at the output in the console, you can decipher that there are 27820 rows and 12 columns
#Now let us look at the names of all our columns using columns attribute and print function
print(suicides.columns)
#Now let us delete some unwanted columns which I think we do not need for analysis
suicides.drop(['population','suicides/100k pop','country-year','HDI for year',' gdp_for_year ($) ','gdp_per_capita ($)'], axis = 1, inplace = True)
#Now let us start exploring the data using some functions
#Let us use the tail and print functions to look at the last ten rows of data
print(suicides.tail(10))
#As you can see from the output in the console, we are left with only 6 columns after we deleted the unwanted ones
#Let us look at unique values in some of our columns using unique function and printing them to console
print(suicides.country.unique())
print(suicides.year.unique())
print(suicides.age.unique())
print(suicides.generation.unique())
#Now let us do some sorting to our dataset. Let us sort the dataset based on the number of suicides column 'suicides_no'
#This sorting is done using the sort_values method
sorted_by_suicidesnumber = suicides.sort_values('suicides_no', ascending=False)
#Now let us look at our sorted dataframe
#We can see the first ten countries, years and other columns in which the suicides were the highest
print(sorted_by_suicidesnumber.head(10))
#After looking at the ouput it is clear that most number of suicides happended in Russian Federation, and it was predominantly
#men who committed the suicide and the age range is also constant with 35-54 being the range. And also all the men who committed
#suicide belonged to the Boomers generation
#Let us do a little visualization now depicting the output just produced.
#We will draw a horizontal bar plot where each plot represents a top ten number of suicides
#We will do this by calling the plot method and setting the arguement kind to bar
sorted_by_suicidesnumber['suicides_no'].head(10).plot(kind = 'barh')
plt.show()
#The above horixontal bar chart opens in a new window as we call the plot using the show function and, you can save it or 
#share it with others
#A new window will open and if you maximize it, it shows our output in a colorful bar chart
#Let's do some statistical analysis with our data now
print(suicides.describe())
#The describe function above gives us statistical summary of numerical value columns in our data. Some of the summarization parameters
#which describe method gives include count, mean, standard deviation, minimum value etc.
#Let us do some summarization now and see how we can aggregate our dataset in different ways so that we can look at it different
#ways
#Let us take the columns country, sex and suicides number and concatenate them to form a new subset dataset
suicides_subset1 = suicides[['country', 'sex', 'suicides_no']]
#Now let us look at the top ten rows of our newly created subset dataset
print(suicides_subset1.head(10))
#As you can see in the console, values pertaining to only the three columns which we put in our new subset dataset are displayed
#Let's create a pivot table which takes country and sex as the index and the vaues being number of suicides
suicides_per_country_sex = suicides_subset1.pivot_table(index = ['country', 'sex'], aggfunc = 'sum')
#Now let us look at our newly created pivot table
print(suicides_per_country_sex)
#As you can see in the console, the number of suicides have been summarized by the sum for each sex by country. This summarization
#feature is an important characteristic of the pivot table
#Now let us visualize the first 20 rows of our newly created pivot table using a bar plot
suicides_per_country_sex.head(20).plot(kind = 'bar', figsize = (20,12))
plt.show()
#The above bar chart opens in a new window as we call the plot using the show function and, you can save it or share it 
#with others
#Visualizations such as a bar chart beautify the way you present data to poeple
#Now let us out output the pivot table just produced to an excel file
#We do this using the to_excel method
suicides_per_country_sex.to_excel('output1.xlsx', index = True)
#After you run the program till here, you will have an excel file saved/writen in the same working directory as you stored 
#this python script
#You can now open the file which was wrtien/saved to the working directory and view the data in it which is our pivot table
#and it is nicely formatted in the same way as we have seen the output in the console with header row being our columns
#Just how we looked at country, sex and suicides_no data. Now let us look at year, age and suicides_no columns
suicides_subset2 = suicides[['year', 'age', 'suicides_no']]
#Now let us look at the top ten rows of our newly created subset dataset
print(suicides_subset2.head(10))
#As you can see in the console, values pertaining to only the three columns which we put in our new subset dataset are displayed
#Let's create a pivot table which takes year and age as the index and the vaues being number of suicides
suicides_per_year_age = suicides_subset2.pivot_table(index = ['year', 'age'], aggfunc = 'sum')
#Now let us look at our newly created pivot table
print(suicides_per_year_age)
#As you can see in the console, the number of suicides have been summarized by the sum for each age by year. This summarization
#feature is an important characteristic of the pivot table
#Now let us visualize the first 48 rows of our newly created pivot table using a line plot
suicides_per_year_age.head(48).plot()
plt.show()
#The above line chart opens in a new window as we call the plot using the show function and, you can save it or share it 
#with others
#Now let us output the pivot table just produced to an excel file
#We do this using the to_excel method
suicides_per_year_age.to_excel('output2.xlsx', index = True)
#After you run the program till here, you will have another excel file saved/writen in the same working directory as you stored 
#this python script
#You can now open the file which was wrtien/saved to the working directory and view the data in it which is our pivot table
#and it is nicely formatted in the same way as we have seen the output in the console with header row being our columns
#Now let us look at country, generation and suicides_no columns
suicides_subset3 = suicides[['country', 'generation', 'suicides_no']]
#Now let us look at the top ten rows of our newly created subset dataset
print(suicides_subset3.head(10))
#As you can see in the console, values pertaining to only the three columns which we put in our new subset dataset are displayed
#Let's create a pivot table which takes country and generation as the index and the values being number of suicides
suicides_per_country_generation = suicides_subset3.pivot_table(index = ['country', 'generation'], aggfunc = 'sum')
#Now let us look at our newly created pivot table
print(suicides_per_country_generation)
#As you can see in the console, the number of suicides have been summarized by the sum for each age by year. This summarization
#feature is an important characteristic of the pivot table
#Now let us visualize the first 48 rows of our newly created pivot table using a line plot
suicides_per_country_generation.head(48).plot(y = 'suicides_no', kind = 'pie', figsize = (20,12))
plt.show()
#The above pie chart opens in a new window as we call the plot using the show function and, you can save it or share it 
#with others
#Now let us output the pivot table just produced to an excel file
#We do this using the to_excel method
suicides_per_country_generation.to_excel('output3.xlsx', index = True)
#After you run the program till here, you will have a third excel file saved/writen in the same working directory as you stored 
#this python script
#You can now open the file which was wrtien/saved to the working directory and view the data in it which is our pivot table
#and it is nicely formatted in the same way as we have seen the output in the console with header row being our columns