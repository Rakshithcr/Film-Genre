# -*- coding: utf-8 -*-
"""Film Genre.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ghpk6wOWnyY0PpQU6DwS4PUP_mdP3k-w
"""

from google.colab import drive
drive.mount('/content/drive')

"""About the data:

This dataset contains genre statistics for movies released between 1995 and 2018.
It provides information on various aspects of the movies, such as gross revenue, tickets sold, and inflation-adjusted figures.
The dataset includes columns for genre, year of release, number of movies released in each genre and year, total gross revenue generated by movies in each genre and year,
total number of tickets sold for movies in each genre and year, inflation-adjusted gross revenue that takes into account changes in the value of money over time, title of the highest-grossing movie in each genre and year,
gross revenue generated by the highest-grossing movie in each genre and year, and inflation-adjusted gross revenue of the highest-grossing movie in each genre and year. This dataset offers insights into film industry trends over a span of more than two decades.

About Columns

Genre: This column represents the genre of each movie.

Year: The year in which the movies were released.

Movies Released: The number of movies released in a particular genre and year.

Gross: The total gross revenue generated by movies in a specific genre and year.

Tickets Sold: The total number of tickets sold for movies in a specific genre and year.

Inflation-Adjusted Gross: The gross revenue adjusted for inflation, taking into account changes in the value of money over time.

Top Movie: The title of the highest-grossing movie in a specific genre and year.

Top Movie Gross (That Year): The gross revenue generated by the

highest-grossing movie in a specific genre and year.

Top Movie Inflation-Adjusted Gross (That Year): The inflation-adjusted gross revenue of the highest-grossing movie in a specific genre and year.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.subplots as sp

df = pd.read_csv("/content/drive/MyDrive/Machine learning/ThrowbackDataThursday Week 11 - Film Genre Stats.csv")

df

df.describe()

df.isnull().sum()

df.info()

"""Genres & Revenue Analysis"""

# To find financial success based on the total gross revenue
genre_gross = df.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head()

# To find financial success based on inflation-adjusted gross revenue
genre_inflation_adjusted_gross = df.groupby('Genre')['Inflation-Adjusted Gross'].sum().sort_values(ascending=False).head()

# To find financial success based on the gross revenue of the top movie in each genre and year
genre_top_movie_gross = df.groupby('Genre')['Top Movie Gross (That Year)'].max().sort_values(ascending=False).head()

# Create subplots
fig = make_subplots(rows=3, cols=1, subplot_titles=['Top Genres by Gross Revenue', 'Top Genres by Inflation-Adjusted Gross Revenue', 'Top Genres by Top Movie Gross (That Year)'])

# Bar chart for Gross Revenue
fig.add_trace(go.Bar(x=genre_gross.index, y=genre_gross.values, name='Gross Revenue', marker_color='skyblue'), row=1, col=1)

# Bar chart for Inflation-Adjusted Gross Revenue
fig.add_trace(go.Bar(x=genre_inflation_adjusted_gross.index, y=genre_inflation_adjusted_gross.values, name='Inflation-Adjusted Gross Revenue', marker_color='lightcoral'), row=2, col=1)

# Bar chart for Top Movie Gross (That Year)
fig.add_trace(go.Bar(x=genre_top_movie_gross.index, y=genre_top_movie_gross.values, name='Top Movie Gross (That Year)', marker_color='lightgreen'), row=3, col=1)

# Update layout
fig.update_layout(height=900, showlegend=False, title_text="Financial Success of Genres")

# Update axis labels
fig.update_xaxes(title_text="Genres", row=3, col=1)
fig.update_yaxes(title_text="Total Gross Revenue", row=1, col=1)
fig.update_yaxes(title_text="Total Inflation-Adjusted Gross Revenue", row=2, col=1)
fig.update_yaxes(title_text="Top Movie Gross (That Year)", row=3, col=1)

# Show the interactive plot
fig.show()

"""Genres Trends & Analysis Over The Years"""

selected_genres = ['Action', 'Comedy', 'Drama', 'Adventure']

filtered_df = df[df['Genre'].isin(selected_genres)]

fig = px.line(filtered_df, x='Year', y='Movies Released', color='Genre',
              title='Movie Releases Over Time for Selected Genres',
              labels={'Movies Released': 'Number of Movies Released'},
              line_shape='linear')

fig.show()

# Create an interactive line chart for gross revenue over different years
fig = px.line(filtered_df, x='Year', y='Gross', color='Genre',
              title='Gross Revenue Over Time for Selected Genres',
              labels={'Gross': 'Total Gross Revenue'},
              line_shape='linear')

# Show the interactive plot
fig.show()

"""Highest-Grossing Movies in Selected Genres Over Time"""

# Selecting a few genres for analysis
selected_genres = ['Action', 'Comedy', 'Drama', 'Adventure']

filtered_df = df[df['Genre'].isin(selected_genres)]

# Create an interactive bar chart to show the highest-grossing movie in each genre and year
fig = px.bar(filtered_df, x='Year', y='Top Movie Gross (That Year)', color='Genre',
             title='Highest-Grossing Movies in Selected Genres Over Time',
             labels={'Top Movie Gross (That Year)': 'Gross Revenue'},
             text='Top Movie', height=500)

fig.update_traces(textposition='outside')
fig.show()

"""Genre Distribution Over the Years"""

# Stacked area chart for genre distribution over the years
fig = px.area(df, x='Year', y='Movies Released', color='Genre',
              title='Genre Distribution Over the Years',
              labels={'Movies Released': 'Number of Movies Released'},
              height=500)
fig.show()

"""Audience Engagement Analysis"""

# Scatter plot for audience engagement
fig = px.scatter(df, x='Tickets Sold', y='Gross', color='Genre',
                 title='Audience Engagement by Genre',
                 labels={'Tickets Sold': 'Number of Tickets Sold', 'Gross': 'Total Gross Revenue'},
                 height=500)
fig.show()

"""Top Movie Performance Over Time"""

# Line chart for the performance of top movies over time
fig = px.line(df, x='Year', y='Top Movie Gross (That Year)', color='Genre',
              title='Top Movie Performance Over Time',
              labels={'Top Movie Gross (That Year)': 'Gross Revenue'},
              height=500)
fig.show()

"""Average Revenue per Movie by Genre"""

# Calculate average revenue per movie by genre
df['Average Revenue per Movie'] = df['Gross'] / df['Movies Released']

# Bar chart for average revenue per movie by genre
fig = px.bar(df, x='Genre', y='Average Revenue per Movie',
             title='Average Revenue per Movie by Genre',
             labels={'Average Revenue per Movie': 'Average Revenue per Movie'},
             height=500)
fig.show()

"""Genre-wise Ticket Sales Distribution"""

# Violin plot for genre-wise ticket sales distribution
fig = px.violin(df, x='Genre', y='Tickets Sold',
                title='Genre-wise Ticket Sales Distribution',
                labels={'Tickets Sold': 'Number of Tickets Sold'},
                height=500)
fig.show()

"""Genre Trends in Inflation-Adjusted Gross Revenue"""

# Line chart for genre trends in inflation-adjusted gross revenue
fig = px.line(df, x='Year', y='Inflation-Adjusted Gross', color='Genre',
              title='Genre Trends in Inflation-Adjusted Gross Revenue',
              labels={'Inflation-Adjusted Gross': 'Inflation-Adjusted Gross Revenue'},
              height=500)
fig.show()

"""Top Movies per Genre and revenues"""

# Count of unique top movies per genre
unique_top_movies_count = df.groupby('Genre')['Top Movie'].nunique().sort_values(ascending=False)

# Top movies with the highest gross revenue
top_movies_gross = df.groupby('Top Movie')['Top Movie Gross (That Year)'].max().sort_values(ascending=False).head(10)

# Box plot for the distribution of gross revenue for top movies
fig = sp.make_subplots(rows=3, cols=1, subplot_titles=['Count of Unique Top Movies per Genre', 'Top Movies with the Highest Gross Revenue', 'Distribution of Gross Revenue for Top Movies'])

# Bar chart for the count of unique top movies per genre
fig.add_trace(go.Bar(x=unique_top_movies_count.index, y=unique_top_movies_count.values),
              row=1, col=1)

# Bar chart for the gross revenue of the top movies
fig.add_trace(go.Bar(x=top_movies_gross.index, y=top_movies_gross.values),
              row=2, col=1)

# Box plot for the distribution of gross revenue for top movies
fig.add_trace(go.Box(x=df['Top Movie'], y=df['Top Movie Gross (That Year)']),
              row=3, col=1)

fig.update_layout(height=1000, showlegend=False, title_text="Top Movie Analysis")
fig.show()

"""Model Creation- Decision Tree"""

## Creating independent and dependent variable
dff = df.copy()
categorical_features = ['Genre']  # Assuming 'Genre' is a categorical variable
numerical_features = ['Year', 'Movies Released']
target_variable = 'Tickets Sold'

# Filter the DataFrame to include only relevant columns
data = df[['Year', 'Movies Released', 'Genre', 'Tickets Sold', 'Gross']]

X = data[['Year', 'Movies Released', 'Genre', 'Gross']] #independent  variables
y = data[target_variable]#dependent  variables

## Balacing the data
from collections import Counter# importing counter to check count of each label
from imblearn.over_sampling import SMOTE #for balancing the data
sm=SMOTE()#object creation
print(Counter(y))# checking count for each class
X_sm, y_sm=sm.fit_resample(X, y) #applying sampling on target variable
print(Counter(y_sm))# checking count after sampling for  each class

