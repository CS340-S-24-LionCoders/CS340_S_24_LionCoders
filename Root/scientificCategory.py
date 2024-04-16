import pandas as pd

class scientificCategory:
    # Read data from a csv file and Store into a dataframe.
    df = pd.read_csv('YatesBiodiversity.csv')
    dataFrameCSV = pd.DataFrame(df)
    print(dataFrameCSV)
    # dataFramePickle = pd.read_pickle('Biodiversity_of_Yates_-_Distribution_of_Animals__Plants_and_Natural_Communities.pl', index_col='county')
    # Utilize configuration constants

#