import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\scientificCategory.log', encoding='utf-8', level=logging.DEBUG)

class scientificCategory():
    def __init__(self, config):
        super(config)
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []
        self.config = ()
    #
    try:
        logger.info('Reading csv file and storing into a dataframe...')
        dataframeCSV = pd.read_csv('Root\Input\YatesBiodiversity.csv',sep=',', index_col=0)
        logger.info('Reading csv file and storing into a dataframe successful!')
    except:
        print('Not loading csv file.')
        logger.debug('Not loading csv file.')
    #
    try:
        logger.info('Reading pickle file and storing into a dataframe...')
        dafaframePickle = pd.read_pickle('Root\Input\AlbanyBiodiversity.pkl',sep=',', index_col=0)
        dataPickle = pd.DataFrame(dafaframePickle)
        logger.info('Reading pickle file and storing into a dataframe successful!')
    except:
        print('Not loading pickle file.')
        logger.debug('Not loading pickle file.')
    #
    
    def violinPlot(data):
        try:
            logger.info('Displaying data as violin plot...')
            seaborn.set(style='whitegrid')
            dataset = seaborn.load_dataset(data)
            #seaborn.violinplot(x="an x-axis value" , y = "an y-axis value" data=dataset) //something is wrong with this line
        #
        except:
            print('Violin plot not working.')
            logger.debug('Violin plot not working.')
        #
    #
 
    def whiskerBoxPlot():
        data = [10, 15, 20, 25, 30, 35, 40]
        try:
            logger.info('Displaying data as whisker-box plot...')
            seaborn.boxplot(data=data, notch=True, sym='b+', orient='vertical', whis=1.5)
            plt.xlabel("Category")
            plt.ylabel("Values")
            plt.title("Box-and-Whisker Plot (Seaborn)")
            plt.show()
        #
        except:
            print('Whisker-box plot not working.')
            logger.debug('Whisker-box plot not working.')
        #
	#
    
 
    def scatterPlot():
        try:
            logger.info('Visualize data distributions in a scatter plot...')
            try:
                sciCat = pd.read_csv('Root\Input\YatesBiodiversity.csv', index_col="Scientific Category")
                try:
                    freq_counts = sciCat.index.value_counts() 
                    freq_counts_sorted = freq_counts.sort_index() 
                    n = len(freq_counts)
                    x = np.arange(1,n+1)
                    y = freq_counts_sorted
                    plt.scatter(x, y)
                    plt.title('Scatter Plot of Yates Biodiversity')
                    plt.xlabel('Scientific Category')
                    plt.ylabel('Scientific Category Frequency')
                    plt.savefig('Root\Output\scatterPlot.png', dpi=300)
                    plt.show()
                    plt.savefig('Root\Output\scatterPlot.png')
                    logger.info('Completed scatter plot...')
                #
                except:
                    print("Not displaying scatter plot.")
                    logger.debug('Not displaying scatter plot.')
                #
            #
            except:
                print("Not reading dataset.")
                logger.debug('Not reading dataset.')
            #
        #
        except:
            print('Scatter plot not working.')
            logger.debug('Scatter plot not working.')
        #
    #
    
    #calculations section 
    
    def calculateJointCounts(self,holder):
        try:
            logger.info('Calculating the joint counts...')
            ##will calculate joint counts and return result
            return holder
        #
        except:
            print('Not calculating the joint counts.')
            logger.debug('Not calculating the joint counts.')
        #
	#

    def calculateJointProbabilities():
        try:
            logger.info('Calculating the joint probabilities...')
            A = np.random.normal(size=100)
            B = np.random.normal(size=100)
            df = pd.DataFrame({'A': A, 'B': B})
            s = seaborn.jointplot(data = df, x ='A', y='B',kind="scatter", height=6, ratio=5)
            s.show()
        #
        except:
            print('Not calculating the joint probabilities.')
            logger.debug('Not calculating the joint probabilities.')
        #
	#
    
    
    def calculateConditionalProbabilities(self, holder):
        try:
            logger.info('Calculating the conditional probabilities...')
            ##will calculate conditional probabilities and return result
            return holder
        #
        except:
            print('Not calculating the conditional probabilities.')
            logger.debug('Not calculating the conditional probabilities.')
        #
    #
    
    def calculations():
        try:
            sciCat = pd.read_csv('Root\Input\YatesBiodiversity.csv',index_col="Scientific Category")
            try: 
                print("The mean is: ")
                print(sciCat.mean())

                print("The median is: ")
                print(sciCat.median())

                print("The standard deviation is ")
                print(sciCat.std())

            except:
                print('Caluculating mean, median, and standard deviation is not working.')
                logger.debug('Caluculating mean, median, and standard deviation is not working.')
        #
        except:
            print("Not reading dataset.")
            logger.debug('Not reading dataset.')
        #
    #

    #categorial attribute section

    def obtainSpecificValue(self, askedValue):
        try:
            logger.info('Obtaining a specific value...')
            ##will return the asked value
            return askedValue
        #
        except:
            print('Not obtaining a specific value.')
            logger.debug('Not obtaining a specific value.')
        #
	#
    
    def generatePermutationsOfNames(self, holder):
        try:
            logger.info('Generating ordered arrangement of names...')
            ##will return an ordered arrangement of names
            return holder
        #
        except:
            print('Not generating ordered arrangement of names.')
            logger.debug('Not generating ordered arrangement of names.')
        #
    #

    def generateCombinationsOfNames(self, holder):
        try:
            logger.info('Generating unordered arrangement of names...')
            ##will return a unordered arrangement of names
            return holder
        #
        except:
            print('Not generating unordered arrangement of names.')
            logger.debug('Not generating unordered arrangement of names.')
        #
	#
    
    def findOrganisim(self, userInput):
        try:
            logger.info('Querying search function...')
            #this function will return an organisim that user wants or will return 'NOT FOUND' if not in dataset
            return userInput 
        #
        except:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #
	#
    scatterPlot()
    calculations()
    calculateJointProbabilities()  
    whiskerBoxPlot()
#