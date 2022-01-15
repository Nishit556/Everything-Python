import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
columns_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names= columns_names)
print(df.head())
movie_titles = pd.read_csv('Movie_Id_Titles')
movie_titles.head()
print(df.head())
df = pd.merge(df, movie_titles, on='item_id')
print(df.head())
sns.set_style('white')
df.groupby('title')['rating'].mean().sort_values(ascending=False)
print(df.head())
df.groupby('title')['rating'].count().sort_values(ascending=False)
print(df.head())
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
print(ratings.head())
ratings['Number of Ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings['rating'].hist(bins=70)
sns.jointplot(x='rating', y='Number of Ratings', data=ratings, alpha=0.5, color='red')
plt.show()

# Building the recommender system

moviemat = df.pivot_table(index= 'user_id', columns= 'title', values= 'ratings')
print(moviemat.head())
starwar_user_ratings = moviemat['Star Wars (1997)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
print(starwar_user_ratings.head())
similar_to_starwars = moviemat.corrwith(starwar_user_ratings)
print(liarliar_user_ratings.head())
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)
corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars = corr_starwars.join(ratings['Number of Ratings'])
pd2 = corr_starwars[corr_starwars['Number of Rai=tings']>100].sort_values('Correlation', asscending= False)
print(pd2.head())
