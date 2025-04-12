# # Netflix Data Analysis
# 
# This notebook analyzes a Netflix dataset to explore trends, patterns, and recommendations based on:
# 1. Show distribution by release year
# 2. Impact of type, country, and genre
# 3. Duration trends
# 4. Frequent actors and directors
# 5. Viewer recommendations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("netflix_titles.xlsx")

# Basic info
df.info()
df.head()

# ## 1. Distribution of Shows by Release Year

sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))
release_year_counts = df['release_year'].value_counts().sort_index()
sns.lineplot(x=release_year_counts.index, y=release_year_counts.values, marker='o', color='crimson')
plt.title("Distribution of Netflix Titles by Release Year", fontsize=16)
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# ## 2. Content Type, Country, and Genre Variety

# Type distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Distribution of Movies vs TV Shows on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.show()

# Top countries
top_countries = df['country'].dropna().str.split(', ', expand=True).stack().value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

# Top genres
genre_series = df['listed_in'].str.split(', ').explode()
top_genres = genre_series.value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='coolwarm')
plt.title('Top 10 Most Common Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()

# ## 3. Duration Trends Over Time

movies = df[df['type'] == 'Movie'].copy()
tv_shows = df[df['type'] == 'TV Show'].copy()
movies['duration_int'] = movies['duration'].str.extract('(\d+)').astype(float)
tv_shows['duration_int'] = tv_shows['duration'].str.extract('(\d+)').astype(float)

# Movies duration trend
plt.figure(figsize=(12, 5))
sns.lineplot(data=movies, x='release_year', y='duration_int', color='navy')
plt.title('Average Movie Duration by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Duration (minutes)')
plt.grid(True)
plt.tight_layout()
plt.show()

# TV Shows season trend
plt.figure(figsize=(12, 5))
sns.lineplot(data=tv_shows, x='release_year', y='duration_int', color='darkgreen')
plt.title('Average Number of Seasons in TV Shows by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Seasons')
plt.grid(True)
plt.tight_layout()
plt.show()

# ## 4. Frequent Actors, Directors, and Genres

# Top Actors
actors_series = df['cast'].dropna().str.split(', ').explode()
top_actors = actors_series.value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_actors.values, y=top_actors.index, palette='magma')
plt.title('Top 10 Most Featured Actors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Actor')
plt.show()

# Top Directors
directors_series = df['director'].dropna().str.split(', ').explode()
top_directors = directors_series.value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_directors.values, y=top_directors.index, palette='cividis')
plt.title('Top 10 Most Featured Directors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

# ## 5. Recommendations Based on Insights

# **Recommendations for Viewers**:
# 
# - Explore **Dramas, International Movies, Comedies** for diverse content.
# - Most content was released between **2017 and 2021** — great for modern storytelling.
# - For regional content:
#   - **USA, UK, Canada** for mainstream English shows
#   - **India** for Bollywood or local shows
#   - **France, Japan, South Korea** for global hits

