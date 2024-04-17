import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='fileLog.log', encoding='utf-8', level=logging.DEBUG)

class scientificCategory:
    logger.info('Reading csv file and storing into a dataframe...')
    dataFrameCSV = pd.read_csv('Root\Input\YatesBiodiversity.csv')
    logger.info('Reading pickle file and storing into a dataframe...')
    dataFramePickle = pd.to_pickle(dataFrameCSV)
    dataFramePickle = pd.read_pickle('Root\Input\Biodiversity_of_Yates_-_Distribution_of_Animals__Plants_and_Natural_Communities.pl')

    # Utilize configuration constants

#