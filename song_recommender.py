from pandas import read_csv
from scipy.spatial.distance import euclidean

data = 'https://gist.githubusercontent.com/jackbandy/5cd988ab5c3d95b79219364dce7ee5ae/raw/731ecdbecc7b33030f23cd919e6067dfbaf42feb/song-ratings.csv'

ratings = read_csv(data,index_col=0)
ratings = ratings.fillna(0)

def distance(p1, p2):
    return euclidean(p1,p2)

def most_similar(name):
    p1 = ratings.loc[name]
    closest_dist = float("inf")
    closest_p = ""

    for p2 in ratings.itertuples():
      if p2.Index != name:
          dist = distance(p1, ratings.loc[p2.Index])
          
          if dist < closest_dist:
              closest_dist = dist
              closest_p = p2.Index
              
    return most_similar_persons_rating(closest_p)

def most_similar_persons_rating(p):
    #need to return list of ratings from closest person
    
print(most_similar("Jack"))
