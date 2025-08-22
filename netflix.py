import pandas as pd 
import matplotlib.pyplot as plt  

#file import 
df=pd.read_csv('netflix_data.csv')
print(df.head())
print(df.info())
df.drop_duplicates(inplace=True)
df.dropna(subset=['type','rating','duration','genre'])
type_count=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=['purple','pink'])
plt.title('Netflix Shows')
plt.xlabel('TYPE')
plt.ylabel('COUNTS')
plt.tight_layout()
plt.savefig('type of shows.png')


rating_count=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index ,autopct='%1.1f%%',startangle=90)
plt.title(' Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('content_rating.png')
plt.show()

content_year=df.groupby(['genre','type']).size().unstack().fillna(0)
fig, ax =plt.subplots(1,2,figsize=(12,5))
ax[0].plot(content_year.index,content_year['Movie'],color='brown')
ax[0].set_title('Type of movie by genre')
ax[0].set_xlabel('Genre')
ax[0].set_ylabel('Movie')

ax[0].plot(content_year.index,content_year['TV Show'],color='Orange')
ax[0].set_title('Type of TV Show by genre')
ax[0].set_xlabel('Tv')
ax[0].set_ylabel('Movie')
fig.suptitle('Genre of TV shows And Movies')
plt.tight_layout()
plt.savefig('genre_tvmovie.png')
plt.show()



gen=df['genre'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(gen,labels=['Documentary','Action','Thriller','Crime','Adeventure','Comedy','Romance','Horror','Drama'],autopct='%1.1f%%',startangle=90)
plt.title(' Percentage of Content Genre')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('genre.png')
plt.show()

movie_df=df[df['type']=='Movie'].copy()
movie_df = movie_df[movie_df['duration'].str.contains('min', na=False)]
movie_df['duration_int']= movie_df['duration'].str.replace(' min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='green',edgecolor='skyblue')
plt.title('Movies Distribution')
plt.xlabel('Duration(Min)')
plt.ylabel('Numbers of Movies')
plt.tight_layout()
plt.savefig('Movie duration hist.png')
plt.show()
