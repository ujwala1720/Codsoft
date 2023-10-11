import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
df_movies = pd.read_csv("/kaggle/input/tmdb-movie-metadata/tmdb_5000_movies.csv")
df_credits = pd.read_csv("/kaggle/input/tmdb-movie-metadata/tmdb_5000_credits.csv")
df_movies.head()

df_movies['overview']
tfidf = TfidfVectorizer(stop_words="english")
df_movies['overview'] = df_movies['overview'].fillna("")
tfidf_matrix = tfidf.fit_transform(df_movies['overview'])


df_credits.head()
cos_sim = linear_kernel(tfidf_matrix,tfidf_matrix)
indices = pd.Series(df_movies.index,index= df_movies['original_title']).drop_duplicates()
indices
indices['Avatar']
def get_recommendations(title,cos_sim =cos_sim):
    idx= indices[title]
    sim_scores = enumerate(cos_sim[idx])
    sim_scores = sorted(sim_scores, key= lambda x:x[1],reverse= True)
    for i in sim_scores:
        print(i)
    
get_recommendations('Avatar')

    
    
    
    
   
    
    
