import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='fileLog.log', encoding='utf-8', level=logging.DEBUG)

class tempConvert():
    try:
        logger.info('Trying to make a pickle file')
        df = pd.read_csv('Input\emp.csv', index_col='county')
        # dataframeCSV.to_pickle('Input\A.pkl')
    #
    except:
        print("Pickle file import not made")
        logger.debug('Pickle file import not made')
    #
    
