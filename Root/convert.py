import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\convert.log', encoding='utf-8', level=logging.DEBUG)

class convert():
    try:
        logger.info('Trying to make a pickle file')
        df = pd.read_csv('Root\Input\AlbanyBiodiversity.csv', index_col='county')
        df.to_pickle('Root\Input\AlbanyBiodiversity.pkl')
    #
    except:
        print("Pickle file import not made")
        logger.debug('Pickle file import not made')
    #
    
