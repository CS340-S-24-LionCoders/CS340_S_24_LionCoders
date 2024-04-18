import pandas as pd
import matplotlib as plt
import seaborn
import logging
from Root.organism import organism

logger = logging.getLogger(__name__)
logging.basicConfig(filename='fileLog.log', encoding='utf-8', level=logging.DEBUG)

class scientificCategory(organism):
    def __init__(self, config):
        super(config)
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []
        self.config = ()
    #
    
    logger.info('Reading csv file and storing into a dataframe...')
    df = pd.read_csv('Input\Biodiversity_by_County_-_Distribution_of_Animals_Plants_and_Natural_Communities.csv', index_col='county')
    data = pd.DataFrame(df)
    
    def violinPlot():
        logger.info('Displaying data as violin plot...')
        seaborn.set(style='whitegrid')
        dataset = seaborn.load_dataset(data)
        #seaborn.violinplot(x="an x-axis value" , y = "an y-axis value" data=dataset) //something is wrong with this line
	#
 
    def whiskerBoxPlot():
        logger.info('Displaying data as whisker-box plot...')
        plt.boxplot(dataset)
        plt.show()
	#
 
    def scatterPlot():
        logger.info('Displaying data as scatter plot...')
        plt.scatter(x,y)
        plt.show()
    #
    
    #calculations section 
    
    def calculateJointCounts(self,holder):
        logger.info('Calculating the joint counts...')
		##will calculate joint counts and return result
        return holder
	#
    
    def calculateJointCounts(self, holder):
        logger.info('Calculating the joint counts...')
		##will calculate joint counts and return result
        return holder 
    #
    
    def calculateJointProbabilities(self, holder):
        logger.info('Calculating the joint probabilities...')
		##will calculate joint probabilities and return result
        return holder
	#
    
    def calculateConditionalProbabilities(self, holder):
        logger.info('Calculating the conditional probabilities...')
		##will calculate conditional probabilities and return result
        return holder
    #
    
    def calculateMean(self, holder):
        logger.info('Calculating the mean...')
		##will calculate mean and return result
        return holder
    #
    
    def calculateMedian(self, holder):
        logger.info('Calculating the median...')
		##will calculate median and return result
        return holder
    #
    
    def calculateSTD(self, holder):
        logger.info('Calculating the standard deviation...')
		##will calculate STD and return result
        return holder 
    #

    #categorial attribute section

    def obtainSpecificValue(self, askedValue):
        logger.info('Obtaining a specific value...')
		##will return the asked value
        return askedValue
	#
    
    def generatePermutationsOfNames(self, holder):
        logger.info('Generating ordered arrangement of names...')
		##will return an ordered arrangement of names
        return holder
    #

    def generateCombinationsOfNames(self, holder):
        logger.info('Generating unordered arrangement of names...')
		##will return a unordered arrangement of names
        return holder
	#
    
    def findOrganisim(self, userInput):
        logger.info('Querying search function...')
        #this function will return an organisim that user wants or will return 'NOT FOUND' if not in dataset
        return userInput 
	#
#